from collections.abc import Mapping
from contextlib import contextmanager
from ctypes import GetLastError, WinError, byref, create_unicode_buffer, sizeof
from typing import Any, Iterable, Iterator, TypeVar

from winerror import ERROR_NO_MORE_ITEMS

from winpnp._setupapi import (
    DIGCF,
    HDEVINFO,
    INVALID_HANDLE_VALUE,
    SP_DEVINFO_DATA,
    SetupDiCreateDeviceInfoList,
    SetupDiDestroyDeviceInfoList,
    SetupDiEnumDeviceInfo,
    SetupDiGetClassDevsW,
    SetupDiGetDevicePropertyKeys,
    SetupDiGetDevicePropertyW,
    SetupDiOpenDeviceInfoW,
)
from winpnp.properties import keys
from winpnp.properties.pnp_property import PnpProperty, PnpPropertyKey

from ._pnp_property_mapping import PnpPropertyMapping

T = TypeVar("T")


class DeviceInfo(Mapping[PnpPropertyKey[Any], PnpProperty[Any]]):
    """
    Represents information about a single PnP device node.

    This class should not be instantiated directly. Instead, use one of the factory methods: `of_instance_id`, `of_all_devices`, `of_present_devices`:

    Can be used as a `Mapping`, with `PnpPropertyKey`s as keys and `PnpProperty` as values.

    For example:
    >>> from winpnp.properties.keys.device import INSTANCE_ID
    ...
    >>> with DeviceInfo.of_instance_id("HTREE\\ROOT\\0") as device:
    ...     instance_id = device[INSTANCE_ID]
    ...
    >>> instance_id
    PnpProperty(value='HTREE\\ROOT\\0', kind=PnpPropertyType(type_id=18, name='STRING'))
    """

    __init_token = object()

    def __init__(self, handle: HDEVINFO, data: SP_DEVINFO_DATA, *, _token=None) -> None:
        """
        This function should not be called directly, instead use one of the factory methods: `of_instance_id`, `of_all_devices`, `of_present_devices`.
        """
        if _token is not self.__init_token:
            raise TypeError(
                f"{type(self).__name__} should not be instantiated directly. You should use one of the factory methods: `of_instance_id`, `of_all_devices`, `of_present_devices`"
            )

        super().__init__()

        self._handle = handle
        self._data = data

        self._properties: PnpPropertyMapping[Any] = PnpPropertyMapping(
            description="<uninitialized DeviceInfo>",
            query_value_func=lambda PropertyKey, PropertyType, PropertyBuffer, PropertyBufferSize, RequiredSize: SetupDiGetDevicePropertyW(
                self._handle,
                byref(self._data),
                PropertyKey,
                PropertyType,
                PropertyBuffer,
                PropertyBufferSize,
                RequiredSize,
                0,
            ),
            query_keys_func=lambda PropertyKeyArray, PropertyKeyCount, RequiredPropertyKeyCount: SetupDiGetDevicePropertyKeys(
                self._handle,
                byref(self._data),
                PropertyKeyArray,
                PropertyKeyCount,
                RequiredPropertyKeyCount,
                0,
            ),
        )

        self._instance_id: str = self._properties[keys.device.INSTANCE_ID].value
        # Update description now that instance_id is known
        self._properties.description = repr(self)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(instance_id={repr(self._instance_id)})"

    def __getitem__(self, key: PnpPropertyKey[T]) -> PnpProperty[T]:
        return self._properties[key]

    def __len__(self) -> int:
        return len(self._properties)

    def __iter__(self) -> Iterator[PnpPropertyKey[Any]]:
        return iter(self._properties)

    @classmethod
    def __enumerate_device_info_set(cls, handle: HDEVINFO) -> Iterator["DeviceInfo"]:
        index = 0
        data = SP_DEVINFO_DATA()
        data.cbSize = sizeof(data)

        while SetupDiEnumDeviceInfo(handle, index, byref(data)):
            yield cls(
                handle, SP_DEVINFO_DATA.from_buffer_copy(data), _token=cls.__init_token
            )
            index += 1

        error = GetLastError()
        if error != ERROR_NO_MORE_ITEMS:
            raise WinError(error)

    @classmethod
    @contextmanager
    def __create_using_SetupDiGetClassDevsW(
        cls, flags: DIGCF
    ) -> Iterator[Iterable["DeviceInfo"]]:
        handle: HDEVINFO = SetupDiGetClassDevsW(None, None, None, flags)
        if handle == INVALID_HANDLE_VALUE:
            raise WinError()

        try:
            yield cls.__enumerate_device_info_set(handle)
        finally:
            SetupDiDestroyDeviceInfoList(handle)

    @classmethod
    @contextmanager
    def of_instance_id(cls, instance_id: str) -> Iterator["DeviceInfo"]:
        """
        Opens information of the device with the specified instance id.
        """
        handle: HDEVINFO = SetupDiCreateDeviceInfoList(None, None)
        if handle == INVALID_HANDLE_VALUE:
            raise WinError()

        try:
            data = SP_DEVINFO_DATA()
            data.cbSize = sizeof(data)
            if not SetupDiOpenDeviceInfoW(
                handle, create_unicode_buffer(instance_id), None, 0, byref(data)
            ):
                raise WinError()

            yield cls(handle, data, _token=cls.__init_token)
        finally:
            SetupDiDestroyDeviceInfoList(handle)

    @classmethod
    @contextmanager
    def of_all_devices(cls) -> Iterator[Iterable["DeviceInfo"]]:
        """
        Opens information of all devices known to Windows, including ones that are no longer present.
        """
        with cls.__create_using_SetupDiGetClassDevsW(DIGCF.ALLCLASSES) as devices:
            yield devices

    @classmethod
    @contextmanager
    def of_present_devices(cls) -> Iterator[Iterable["DeviceInfo"]]:
        """
        Opens information of all devices that are currently present.
        """
        with cls.__create_using_SetupDiGetClassDevsW(
            DIGCF.ALLCLASSES | DIGCF.PRESENT
        ) as devices:
            yield devices
