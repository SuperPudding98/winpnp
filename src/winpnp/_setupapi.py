from ctypes import Structure, c_ubyte, c_uint16, c_uint32
from enum import IntFlag
from uuid import UUID


class GUID(Structure):
    _fields_ = (
        ("Data1", c_uint32),
        ("Data2", c_uint16),
        ("Data3", c_uint16),
        ("Data4", c_ubyte * 8),
    )

    def __str__(self) -> str:
        return str(self.to_uuid())

    def __repr__(self) -> str:
        return f"{type(self).__name__}({{{str(self.to_uuid())}}})"

    @classmethod
    def from_uuid(cls, guid: UUID) -> "GUID":
        return cls.from_buffer_copy(guid.bytes_le)

    def to_uuid(self) -> UUID:
        return UUID(bytes_le=bytes(self))


class DEVPROPKEY(Structure):
    _fields_ = (
        ("fmtid", GUID),
        ("pid", c_uint32),
    )


class DEVPROP_TYPEMOD(IntFlag):
    NONE = 0x00000000
    ARRAY = 0x00001000  # array of fixed-sized data elements
    LIST = 0x00002000  # list of variable-sized data elements


class DEVPROP_TYPE(IntFlag):
    EMPTY = 0x00000000  # nothing, no property data
    NULL = 0x00000001  # null property data
    SBYTE = 0x00000002  # 8-bit signed int (SBYTE)
    BYTE = 0x00000003  # 8-bit unsigned int (BYTE)
    INT16 = 0x00000004  # 16-bit signed int (SHORT)
    UINT16 = 0x00000005  # 16-bit unsigned int (USHORT)
    INT32 = 0x00000006  # 32-bit signed int (LONG)
    UINT32 = 0x00000007  # 32-bit unsigned int (ULONG)
    INT64 = 0x00000008  # 64-bit signed int (LONG64)
    UINT64 = 0x00000009  # 64-bit unsigned int (ULONG64)
    FLOAT = 0x0000000A  # 32-bit floating-point (FLOAT)
    DOUBLE = 0x0000000B  # 64-bit floating-point (DOUBLE)
    DECIMAL = 0x0000000C  # 128-bit data (DECIMAL)
    GUID = 0x0000000D  # 128-bit unique identifier (GUID)
    CURRENCY = 0x0000000E  # 64 bit signed int currency value (CURRENCY)
    DATE = 0x0000000F  # date (DATE)
    FILETIME = 0x00000010  # file time (FILETIME)
    BOOLEAN = 0x00000011  # 8-bit boolean (DEVPROP_BOOLEAN)
    STRING = 0x00000012  # null-terminated string
    STRING_LIST = STRING | DEVPROP_TYPEMOD.LIST  # multi-sz string list
    SECURITY_DESCRIPTOR = 0x00000013  # self-relative binary SECURITY_DESCRIPTOR
    SECURITY_DESCRIPTOR_STRING = 0x00000014  # security descriptor string (SDDL format)
    DEVPROPKEY = 0x00000015  # device property key (DEVPROPKEY)
    DEVPROPTYPE = 0x00000016  # device property type (DEVPROPTYPE)
    BINARY = BYTE | DEVPROP_TYPEMOD.ARRAY  # custom binary data
    ERROR = 0x00000017  # 32-bit Win32 system error code
    NTSTATUS = 0x00000018  # 32-bit NTSTATUS code
    STRING_INDIRECT = 0x00000019  # string resource (@[path\]<dllname>,-<strId>)
