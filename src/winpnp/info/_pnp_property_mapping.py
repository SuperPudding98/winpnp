from collections.abc import Mapping
from ctypes import (
    POINTER,
    GetLastError,
    WinError,
    byref,
    c_ubyte,
    c_uint32,
    cast,
    create_string_buffer,
)
from typing import Any, Iterator, Protocol, TypeVar

from winerror import ERROR_INSUFFICIENT_BUFFER, ERROR_NOT_FOUND

from winpnp._setupapi import DEVPROPKEY, GUID
from winpnp.properties.pnp_property import PnpProperty, PnpPropertyKey, PnpPropertyType

T = TypeVar("T")


class QueryValueFunc(Protocol):
    def __call__(
        self,
        PropertyKey,
        PropertyType,
        PropertyBuffer,
        PropertyBufferSize,
        RequiredSize,
    ) -> bool: ...


class QueryKeysFunc(Protocol):
    def __call__(
        self, PropertyKeyArray, PropertyKeyCount, RequiredPropertyKeyCount
    ) -> bool: ...


class PnpPropertyMapping(Mapping[PnpPropertyKey[T], PnpProperty[T]]):
    def __init__(
        self,
        description: str,
        query_value_func: QueryValueFunc,
        query_keys_func: QueryKeysFunc,
    ) -> None:
        super().__init__()

        self.description = description
        self.query_value = query_value_func
        self.query_keys = query_keys_func

    def __getitem__(self, key: PnpPropertyKey[T]) -> PnpProperty[T]:
        if not isinstance(key, PnpPropertyKey):
            raise KeyError(key)

        win_prop_key = DEVPROPKEY(GUID.from_uuid(key.category), key.property_id)
        type_id = c_uint32()
        required_size = c_uint32()

        if self.query_value(
            byref(win_prop_key),
            byref(type_id),
            None,
            0,
            byref(required_size),
        ):
            return self.__build_property(key, PnpPropertyType(type_id.value), b"")

        error = GetLastError()
        if error == ERROR_NOT_FOUND:
            raise KeyError(key)
        if error != ERROR_INSUFFICIENT_BUFFER:
            raise WinError(error)

        value_buffer = create_string_buffer(required_size.value)
        if not self.query_value(
            byref(win_prop_key),
            byref(type_id),
            cast(value_buffer, POINTER(c_ubyte)),
            required_size,
            None,
        ):
            raise WinError()

        return self.__build_property(
            key, PnpPropertyType(type_id.value), value_buffer.raw
        )

    def __len__(self) -> int:
        required_count = c_uint32()
        if self.query_keys(None, 0, byref(required_count)):
            return 0

        error = GetLastError()
        if error != ERROR_INSUFFICIENT_BUFFER:
            raise WinError(error)

        return required_count.value

    def __iter__(self) -> Iterator[PnpPropertyKey[T]]:
        keys = (DEVPROPKEY * len(self))()
        if not self.query_keys(keys, len(keys), None):
            raise WinError()

        for key in keys:
            yield PnpPropertyKey(key.fmtid.to_uuid(), key.pid)

    def __build_property(
        self,
        key: PnpPropertyKey[T],
        actual_type: PnpPropertyType[Any],
        data: bytes,
    ) -> PnpProperty[T]:
        if (
            key.allowed_types is not None
            and actual_type.type_id not in key.allowed_types
        ):
            raise ValueError(
                f"Property {key} of {self.description} has type {actual_type}, which is not expected."
            )

        if key.allowed_types is not None:
            # Prefer key from allowed_types over original actual_type in case the one from allowed_types has a custom decoder
            actual_type = key.allowed_types[actual_type.type_id]

        return PnpProperty(actual_type.decode(data), actual_type)
