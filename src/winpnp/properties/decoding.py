import ctypes
from array import array
from ctypes import FormatError, Structure, byref, c_int32, c_uint16, sizeof, windll
from dataclasses import dataclass, field
from datetime import datetime, timezone, tzinfo
from itertools import takewhile
from typing import TYPE_CHECKING, Any, Literal, Optional
from uuid import UUID

from more_itertools import sliced

from winpnp import _setupapi

if TYPE_CHECKING:
    # Import only if type checking to avoid circular import
    from .pnp_property import PnpPropertyKey, PnpPropertyType

_GUID_BYTE_SIZE = 16
_FILETIME_BYTE_SIZE = 8

_ArrayIntTypeCode = Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
_ArrayFloatTypeCode = Literal["f", "d"]


class _SYSTEMTIME(Structure):
    _fields_ = (
        ("wYear", c_uint16),
        ("wMonth", c_uint16),
        ("wDayOfWeek", c_uint16),
        ("wDay", c_uint16),
        ("wHour", c_uint16),
        ("wMinute", c_uint16),
        ("wSecond", c_uint16),
        ("wMilliseconds", c_uint16),
    )

    def to_datetime(self, time_zone: Optional[tzinfo] = None) -> datetime:
        return datetime(
            self.wYear,
            self.wMonth,
            self.wDay,
            self.wHour,
            self.wMinute,
            self.wSecond,
            self.wMilliseconds * 1000,
            time_zone,
        )


@dataclass(frozen=True)
class Win32Error:
    code: int
    description: str = field(init=False, compare=False)

    def __post_init__(self) -> None:
        # using object.__setattr__ because self is frozen
        object.__setattr__(self, "description", FormatError(c_int32(self.code).value))


@dataclass(frozen=True)
class NtStatus:
    code: int
    description: str = field(init=False, compare=False)

    def __post_init__(self) -> None:
        # using object.__setattr__ because self is frozen
        object.__setattr__(
            self,
            "description",
            FormatError(c_int32(windll.ntdll.RtlNtStatusToDosError(self.code)).value),
        )


def decode_raw(data: bytes) -> bytes:
    return data


def decode_integers(data: bytes, typecode: _ArrayIntTypeCode) -> list[int]:
    return list(array(typecode, data))


def decode_floats(data: bytes, typecode: _ArrayFloatTypeCode) -> list[float]:
    return list(array(typecode, data))


def decode_guids(data: bytes) -> list[UUID]:
    return [UUID(bytes_le=x) for x in sliced(data, _GUID_BYTE_SIZE, strict=True)]


def decode_filetimes(data: bytes) -> list[datetime]:
    output = []
    systemtime = _SYSTEMTIME()

    for filetime in sliced(data, _FILETIME_BYTE_SIZE, strict=True):
        if not windll.kernel32.FileTimeToSystemTime(filetime, byref(systemtime)):
            raise ctypes.WinError()
        output.append(systemtime.to_datetime(timezone.utc))

    return output


def decode_booleans(data: bytes) -> list[bool]:
    return [x != 0 for x in data]


def decode_string(data: bytes) -> str:
    string = data.decode("utf-16-le")
    return "".join(takewhile(lambda char: char != "\0", string))


def decode_strings(data: bytes) -> list[str]:
    strings = data.decode("utf-16-le").split("\0")
    return list(takewhile(lambda x: len(x) > 0, strings))


def decode_property_keys(data: bytes) -> list["PnpPropertyKey[Any]"]:
    # Import in function to avoid circular import
    from .pnp_property import PnpPropertyKey

    count = len(data) // sizeof(_setupapi.DEVPROPKEY)
    keys = (_setupapi.DEVPROPKEY * count).from_buffer_copy(data)
    return [PnpPropertyKey(key.fmtid.to_uuid(), key.pid) for key in keys]


def decode_property_types(data: bytes) -> list["PnpPropertyType[Any]"]:
    # Import in function to avoid circular import
    from .pnp_property import PnpPropertyType

    return [PnpPropertyType(type_id) for type_id in decode_integers(data, "L")]


def decode_win32_errors(data: bytes) -> list[Win32Error]:
    return [Win32Error(code) for code in array("L", data)]


def decode_nt_statuses(data: bytes) -> list[NtStatus]:
    return [NtStatus(code) for code in array("L", data)]
