from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

FRIENDLY_NAME = PnpPropertyKey.register_new(
    UUID("{026e516e-b814-414b-83cd856d6fef4822}"),
    2,
    "DeviceInterface_FriendlyName",
    (kinds.STRING,),
)

ENABLED = PnpPropertyKey.register_new(
    UUID("{026e516e-b814-414b-83cd856d6fef4822}"),
    3,
    "DeviceInterface_Enabled",
    (kinds.BOOLEAN,),
)

CLASS_GUID = PnpPropertyKey.register_new(
    UUID("{026e516e-b814-414b-83cd856d6fef4822}"),
    4,
    "DeviceInterface_ClassGuid",
    (kinds.GUID,),
)

REFERENCE_STRING = PnpPropertyKey.register_new(
    UUID("{026e516e-b814-414b-83cd856d6fef4822}"),
    5,
    "DeviceInterface_ReferenceString",
    (kinds.STRING,),
)

RESTRICTED = PnpPropertyKey.register_new(
    UUID("{026e516e-b814-414b-83cd856d6fef4822}"),
    6,
    "DeviceInterface_Restricted",
    (kinds.BOOLEAN,),
)

UNRESTRICTED_APP_CAPABILITIES = PnpPropertyKey.register_new(
    UUID("{026e516e-b814-414b-83cd856d6fef4822}"),
    8,
    "DeviceInterface_UnrestrictedAppCapabilities",
    (kinds.STRING_LIST,),
)

SCHEMATIC_NAME = PnpPropertyKey.register_new(
    UUID("{026e516e-b814-414b-83cd856d6fef4822}"),
    9,
    "DeviceInterface_SchematicName",
    (kinds.STRING,),
)
