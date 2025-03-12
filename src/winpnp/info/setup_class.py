from collections.abc import Mapping
from ctypes import WinError, byref, c_uint32, create_unicode_buffer
from typing import Any, Iterator, TypeVar
from uuid import UUID

from winpnp._setupapi import (
    DICLASSPROP,
    GUID,
    SetupDiBuildClassInfoList,
    SetupDiClassGuidsFromNameW,
    SetupDiGetClassPropertyKeys,
    SetupDiGetClassPropertyW,
)
from winpnp.properties import keys
from winpnp.properties.pnp_property import PnpProperty, PnpPropertyKey

from ._pnp_property_mapping import PnpPropertyMapping

T = TypeVar("T")


class SetupClassInfo(Mapping[PnpPropertyKey[Any], PnpProperty[Any]]):
    """
    Represents information about a single PnP setup class.

    Can be used as a `Mapping`, with `PnpPropertyKey`s as keys and `PnpProperty` as values.

    For example:
    >>> from uuid import UUID
    >>> from winpnp.properties.keys.device_class import CLASS_NAME
    ...
    >>> SetupClassInfo(UUID("36fc9e60-c465-11cf-8056-444553540000"))[CLASS_NAME]
    PnpProperty(value='USB', kind=PnpPropertyType(type_id=18, name='STRING'))
    """

    def __init__(self, guid: UUID) -> None:
        super().__init__()

        self._guid = guid

        self._properties: PnpPropertyMapping[Any] = PnpPropertyMapping(
            description="<uninitialized SetupClassInfo>",
            query_value_func=lambda PropertyKey, PropertyType, PropertyBuffer, PropertyBufferSize, RequiredSize: SetupDiGetClassPropertyW(
                byref(GUID.from_uuid(self._guid)),
                PropertyKey,
                PropertyType,
                PropertyBuffer,
                PropertyBufferSize,
                RequiredSize,
                DICLASSPROP.INSTALLER,
            ),
            query_keys_func=lambda PropertyKeyArray, PropertyKeyCount, RequiredPropertyKeyCount: SetupDiGetClassPropertyKeys(
                byref(GUID.from_uuid(self._guid)),
                PropertyKeyArray,
                PropertyKeyCount,
                RequiredPropertyKeyCount,
                DICLASSPROP.INSTALLER,
            ),
        )

        self._name: str = self._properties[keys.device_class.CLASS_NAME].value
        # Update description now that instance_id is known
        self._properties.description = repr(self)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(guid={repr(self._guid)}, name={repr(self._name)})"
        )

    def __getitem__(self, key: PnpPropertyKey[T]) -> PnpProperty[T]:
        return self._properties[key]

    def __len__(self) -> int:
        return len(self._properties)

    def __iter__(self) -> Iterator[PnpPropertyKey]:
        return iter(self._properties)

    @property
    def guid(self) -> UUID:
        return self._guid

    @classmethod
    def of_class_name(cls, name: str) -> Iterator["SetupClassInfo"]:
        name_buffer = create_unicode_buffer(name)
        required_size = c_uint32()
        if SetupDiClassGuidsFromNameW(name_buffer, None, 0, byref(required_size)):
            return

        guids = (GUID * required_size.value)()
        if not SetupDiClassGuidsFromNameW(
            name_buffer, guids, required_size, byref(required_size)
        ):
            raise WinError()

        for guid in guids:
            yield cls(guid.to_uuid())

    @classmethod
    def of_all_classes(cls) -> Iterator["SetupClassInfo"]:
        required_size = c_uint32()
        if SetupDiBuildClassInfoList(0, None, 0, byref(required_size)):
            return

        guids = (GUID * required_size.value)()
        if not SetupDiBuildClassInfoList(0, guids, required_size, byref(required_size)):
            raise WinError()

        for guid in guids:
            yield cls(guid.to_uuid())
