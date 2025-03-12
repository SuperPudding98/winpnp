from ctypes import (
    POINTER,
    Structure,
    c_bool,
    c_ubyte,
    c_uint16,
    c_uint32,
    c_void_p,
    c_wchar_p,
    windll,
)
from enum import IntFlag
from uuid import UUID

INVALID_HANDLE_VALUE = -1

HDEVINFO = c_void_p


class DIGCF(IntFlag):
    DEFAULT = 0x00000001
    PRESENT = 0x00000002
    ALLCLASSES = 0x00000004
    PROFILE = 0x00000008
    DEVICEINTERFACE = 0x00000010


class DICLASSPROP(IntFlag):
    INSTALLER = 0x00000001
    INTERFACE = 0x00000002


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


class SP_DEVINFO_DATA(Structure):
    _fields_ = (
        ("cbSize", c_uint32),
        ("ClassGuid", GUID),
        ("DevInst", c_uint32),
        ("Reserved", c_void_p),
    )


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


SetupDiCreateDeviceInfoList = windll.setupapi.SetupDiCreateDeviceInfoList
SetupDiCreateDeviceInfoList.restype = HDEVINFO
SetupDiCreateDeviceInfoList.argtypes = (
    POINTER(GUID),  # [in, optional] ClassGuid
    c_void_p,  # [in, optional] hwndParent
)

SetupDiDestroyDeviceInfoList = windll.setupapi.SetupDiDestroyDeviceInfoList
SetupDiDestroyDeviceInfoList.restype = c_bool
SetupDiDestroyDeviceInfoList.argtypes = (HDEVINFO,)  # [in] DeviceInfoSet

SetupDiGetClassDevsW = windll.setupapi.SetupDiGetClassDevsW
SetupDiGetClassDevsW.restype = HDEVINFO
SetupDiGetClassDevsW.argtypes = (
    POINTER(GUID),  # [in, optional] ClassGuid
    c_wchar_p,  # [in, optional] Enumerator
    c_void_p,  # [in, optional] hwndParent
    c_uint32,  # [in] Flags
)

SetupDiEnumDeviceInfo = windll.setupapi.SetupDiEnumDeviceInfo
SetupDiEnumDeviceInfo.restype = c_bool
SetupDiEnumDeviceInfo.argtypes = (
    HDEVINFO,  # [in] DeviceInfoSet
    c_uint32,  # [in] MemberIndex
    POINTER(SP_DEVINFO_DATA),  # [out] DeviceInfoData
)

SetupDiOpenDeviceInfoW = windll.setupapi.SetupDiOpenDeviceInfoW
SetupDiOpenDeviceInfoW.restype = c_bool
SetupDiOpenDeviceInfoW.argtypes = (
    HDEVINFO,  # [in] DeviceInfoSet
    c_wchar_p,  # [in] DeviceInstanceId
    c_void_p,  # [in, optional] hwndParent
    c_uint32,  # [in] OpenFlags
    POINTER(SP_DEVINFO_DATA),  # [out, optional] DeviceInfoData
)

SetupDiGetDevicePropertyW = windll.setupapi.SetupDiGetDevicePropertyW
SetupDiGetDevicePropertyW.restype = c_bool
SetupDiGetDevicePropertyW.argtypes = (
    HDEVINFO,  # [in] DeviceInfoSet
    POINTER(SP_DEVINFO_DATA),  # [in] DeviceInfoData
    POINTER(DEVPROPKEY),  # [in] PropertyKey
    POINTER(c_uint32),  # [out] PropertyType
    POINTER(c_ubyte),  # [out, optional] PropertyBuffer
    c_uint32,  # [in] PropertyBufferSize
    POINTER(c_uint32),  # [out, optional] RequiredSize
    c_uint32,  # [in] Flags
)

SetupDiGetDevicePropertyKeys = windll.setupapi.SetupDiGetDevicePropertyKeys
SetupDiGetDevicePropertyKeys.restype = c_bool
SetupDiGetDevicePropertyKeys.argtypes = (
    HDEVINFO,  # [in] DeviceInfoSet
    POINTER(SP_DEVINFO_DATA),  # [in] DeviceInfoData
    POINTER(DEVPROPKEY),  # [out, optional] PropertyKeyArray
    c_uint32,  # [in] PropertyKeyCount
    POINTER(c_uint32),  # [out, optional] RequiredPropertyKeyCount
    c_uint32,  # [in] Flags
)

SetupDiBuildClassInfoList = windll.setupapi.SetupDiBuildClassInfoList
SetupDiBuildClassInfoList.restype = c_bool
SetupDiBuildClassInfoList.argtypes = (
    c_uint32,  # [in] Flags
    POINTER(GUID),  # [out, optional] ClassGuidList
    c_uint32,  # [in] ClassGuidListSize
    POINTER(c_uint32),  # [out] RequiredSize
)

SetupDiClassGuidsFromNameW = windll.setupapi.SetupDiClassGuidsFromNameW
SetupDiClassGuidsFromNameW.restype = c_bool
SetupDiClassGuidsFromNameW.argtypes = (
    c_wchar_p,  # [in] ClassName,
    POINTER(GUID),  # [out] ClassGuidList,
    c_uint32,  # [in]  ClassGuidListSize,
    POINTER(c_uint32),  # [out] RequiredSize
)

SetupDiGetClassPropertyW = windll.setupapi.SetupDiGetClassPropertyW
SetupDiGetClassPropertyW.restype = c_bool
SetupDiGetClassPropertyW.argtypes = (
    POINTER(GUID),  # [in] ClassGuid,
    POINTER(DEVPROPKEY),  # [in] PropertyKey,
    POINTER(c_uint32),  # [out] PropertyType,
    POINTER(c_ubyte),  # [out] PropertyBuffer,
    c_uint32,  # [in] PropertyBufferSize,
    POINTER(c_uint32),  # [out, optional] RequiredSize,
    c_uint32,  # [in] Flags
)

SetupDiGetClassPropertyKeys = windll.setupapi.SetupDiGetClassPropertyKeys
SetupDiGetClassPropertyKeys.restype = c_bool
SetupDiGetClassPropertyKeys.argtypes = (
    POINTER(GUID),  # [in] ClassGuid,
    POINTER(DEVPROPKEY),  # [out, optional] PropertyKeyArray,
    c_uint32,  # [in] PropertyKeyCount,
    POINTER(c_uint32),  # [out, optional] RequiredPropertyKeyCount,
    c_uint32,  # [in] Flags
)
