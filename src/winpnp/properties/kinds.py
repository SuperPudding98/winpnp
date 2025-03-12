from more_itertools import one

from winpnp._setupapi import DEVPROP_TYPE, DEVPROP_TYPEMOD

from .decoding import (
    decode_booleans,
    decode_filetimes,
    decode_floats,
    decode_guids,
    decode_integers,
    decode_nt_statuses,
    decode_property_keys,
    decode_property_types,
    decode_raw,
    decode_string,
    decode_strings,
    decode_win32_errors,
)
from .pnp_property import PnpPropertyType

NULL = PnpPropertyType.register_new(int(DEVPROP_TYPE.NULL), "NULL", lambda _: None)
"""The property exists, but it has no value."""

SBYTE = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.SBYTE), "SBYTE", lambda x: one(decode_integers(x, "b"))
)
"""8-bit signed integer"""

SBYTE_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.SBYTE | DEVPROP_TYPEMOD.ARRAY),
    "SBYTE_ARRAY",
    lambda x: decode_integers(x, "b"),
)
"""Array of 8-bit signed integers"""

BYTE = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.BYTE), "BYTE", lambda x: one(decode_integers(x, "B"))
)
"""8-bit unsigned integer"""

BYTE_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.BYTE | DEVPROP_TYPEMOD.ARRAY),
    "BYTE_ARRAY",
    lambda x: decode_integers(x, "B"),
)
"""Array of 8-bit unsigned integers (used for custom binary data)"""

INT16 = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.INT16), "INT16", lambda x: one(decode_integers(x, "h"))
)
"""16-bit signed integer"""

INT16_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.INT16 | DEVPROP_TYPEMOD.ARRAY),
    "INT16_ARRAY",
    lambda x: decode_integers(x, "h"),
)
"""Array of 16-bit signed integers"""

UINT16 = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.UINT16), "UINT16", lambda x: one(decode_integers(x, "H"))
)
"""16-bit unsigned integer"""

UINT16_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.UINT16 | DEVPROP_TYPEMOD.ARRAY),
    "UINT16_ARRAY",
    lambda x: decode_integers(x, "H"),
)
"""Array of 16-bit unsigned integers"""

INT32 = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.INT32), "INT32", lambda x: one(decode_integers(x, "l"))
)
"""32-bit signed integer"""

INT32_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.INT32 | DEVPROP_TYPEMOD.ARRAY),
    "INT32_ARRAY",
    lambda x: decode_integers(x, "l"),
)
"""Array of 32-bit signed integers"""

UINT32 = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.UINT32), "UINT32", lambda x: one(decode_integers(x, "L"))
)
"""32-bit unsigned integer"""

UINT32_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.UINT32 | DEVPROP_TYPEMOD.ARRAY),
    "UINT32_ARRAY",
    lambda x: decode_integers(x, "L"),
)
"""Array of 32-bit unsigned integers"""

INT64 = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.INT64), "INT64", lambda x: one(decode_integers(x, "q"))
)
"""64-bit signed integer"""

INT64_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.INT64 | DEVPROP_TYPEMOD.ARRAY),
    "INT64_ARRAY",
    lambda x: decode_integers(x, "q"),
)
"""Array of 64-bit signed integers"""

UINT64 = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.UINT64), "UINT64", lambda x: one(decode_integers(x, "Q"))
)
"""64-bit unsigned integer"""

UINT64_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.UINT64 | DEVPROP_TYPEMOD.ARRAY),
    "UINT64_ARRAY",
    lambda x: decode_integers(x, "Q"),
)
"""Array of 64-bit unsigned integers"""

FLOAT = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.FLOAT), "FLOAT", lambda x: one(decode_floats(x, "f"))
)
"""32-bit floating-point number"""

FLOAT_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.FLOAT | DEVPROP_TYPEMOD.ARRAY),
    "FLOAT_ARRAY",
    lambda x: decode_floats(x, "f"),
)
"""Array of 32-bit floating-point numbers"""

DOUBLE = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DOUBLE), "DOUBLE", lambda x: one(decode_floats(x, "d"))
)
"""64-bit floating-point number"""

DOUBLE_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DOUBLE | DEVPROP_TYPEMOD.ARRAY),
    "DOUBLE_ARRAY",
    lambda x: decode_floats(x, "d"),
)
"""Array of 64-bit floating-point numbers"""

DECIMAL = PnpPropertyType.register_new(int(DEVPROP_TYPE.DECIMAL), "DECIMAL", decode_raw)
"""Windows DECIMAL structure. For now, decoded as raw bytes."""

DECIMAL_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DECIMAL | DEVPROP_TYPEMOD.ARRAY),
    "DECIMAL_ARRAY",
    decode_raw,
)
"""Array of Windows DECIMAL structures. For now, decoded as raw bytes."""

GUID = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.GUID), "GUID", lambda x: one(decode_guids(x))
)
"""128-bit unique identifier"""

GUID_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.GUID | DEVPROP_TYPEMOD.ARRAY), "GUID_ARRAY", decode_guids
)
"""Array of 128-bit unique identifiers"""

CURRENCY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.CURRENCY), "CURRENCY", decode_raw
)
"""Windows CURRENCY structure. For now, decoded as raw bytes."""

CURRENCY_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.CURRENCY | DEVPROP_TYPEMOD.ARRAY),
    "CURRENCY_ARRAY",
    decode_raw,
)
"""Array of Windows CURRENCY structures. For now, decoded as raw bytes."""

DATE = PnpPropertyType.register_new(int(DEVPROP_TYPE.DATE), "DATE", decode_raw)
"""64-bit floating-point number (double) that specifies the number of days since December 31, 1899. For now, decoded as raw bytes."""

DATE_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DATE | DEVPROP_TYPEMOD.ARRAY), "DATE_ARRAY", decode_raw
)
"""Array of doubles that specify the number of days since December 31, 1899. For now, decoded as raw bytes."""

FILETIME = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.FILETIME), "FILETIME", lambda x: one(decode_filetimes(x))
)
"""Windows FILETIME structure."""

FILETIME_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.FILETIME | DEVPROP_TYPEMOD.ARRAY),
    "FILETIME_ARRAY",
    decode_filetimes,
)
"""Array of Windows file time structures."""

BOOLEAN = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.BOOLEAN), "BOOLEAN", lambda x: one(decode_booleans(x))
)
"""8-bit boolean"""

BOOLEAN_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.BOOLEAN | DEVPROP_TYPEMOD.ARRAY), "BOOLEAN_ARRAY", decode_booleans
)
"""Array of 8-bit booleans"""

STRING = PnpPropertyType.register_new(int(DEVPROP_TYPE.STRING), "STRING", decode_string)
"""Null-terminated UTF-16-LE string."""

STRING_LIST = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.STRING | DEVPROP_TYPEMOD.LIST), "STRING_LIST", decode_strings
)
"""Multi-string: sequence of null-terminated UTF-16-LE string, followed by an empty string."""

SECURITY_DESCRIPTOR = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.SECURITY_DESCRIPTOR), "SECURITY_DESCRIPTOR", decode_raw
)
"""Self-relative binary security descriptor. For now, decoded as raw bytes."""

SECURITY_DESCRIPTOR_STRING = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.SECURITY_DESCRIPTOR_STRING),
    "SECURITY_DESCRIPTOR_STRING",
    decode_string,
)
"""Null-terminated UTF-16-LE string that contains a security descriptor in the Security Descriptor Definition Language (SDDL) format."""

SECURITY_DESCRIPTOR_STRING_LIST = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.SECURITY_DESCRIPTOR_STRING | DEVPROP_TYPEMOD.LIST),
    "SECURITY_DESCRIPTOR_STRING_LIST",
    decode_strings,
)
"""Multi-string of strings that contain a security descriptor in the Security Descriptor Definition Language (SDDL) format."""

DEVPROPKEY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DEVPROPKEY), "DEVPROPKEY", lambda x: one(decode_property_keys(x))
)
"""Device property key."""

DEVPROPKEY_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DEVPROPKEY | DEVPROP_TYPEMOD.ARRAY),
    "DEVPROPKEY_ARRAY",
    decode_property_keys,
)
"""Array of device property keys."""

DEVPROPTYPE = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DEVPROPTYPE),
    "DEVPROPTYPE",
    lambda x: one(decode_property_types(x)),
)
"""Device property type."""

DEVPROPTYPE_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.DEVPROPTYPE | DEVPROP_TYPEMOD.ARRAY),
    "DEVPROPTYPE_ARRAY",
    decode_property_types,
)
"""Array of device property types."""

ERROR = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.ERROR), "ERROR", lambda x: one(decode_win32_errors(x))
)
"""32-bit Win32 system error code."""

ERROR_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.ERROR | DEVPROP_TYPEMOD.ARRAY), "ERROR_ARRAY", decode_win32_errors
)
"""Array of 32-bit Win32 system error codes."""

NTSTATUS = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.NTSTATUS), "NTSTATUS", lambda x: one(decode_nt_statuses(x))
)
"""32-bit NTSTATUS code."""

NTSTATUS_ARRAY = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.NTSTATUS | DEVPROP_TYPEMOD.ARRAY),
    "NTSTATUS_ARRAY",
    decode_nt_statuses,
)
"""Array of 32-bit NTSTATUS codes."""

STRING_INDIRECT = PnpPropertyType.register_new(
    int(DEVPROP_TYPE.STRING_INDIRECT), "STRING_INDIRECT", decode_string
)
"""Null-terminated UTF-16-LE string that contains an indirect string reference."""
