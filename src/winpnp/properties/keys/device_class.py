from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

UPPER_FILTERS = PnpPropertyKey.register_new(
    UUID("{4321918b-f69e-470d-a5de4d88c75ad24b}"),
    19,
    "DeviceClass_UpperFilters",
    (kinds.STRING_LIST,),
)

LOWER_FILTERS = PnpPropertyKey.register_new(
    UUID("{4321918b-f69e-470d-a5de4d88c75ad24b}"),
    20,
    "DeviceClass_LowerFilters",
    (kinds.STRING_LIST,),
)

SECURITY = PnpPropertyKey.register_new(
    UUID("{4321918b-f69e-470d-a5de4d88c75ad24b}"),
    25,
    "DeviceClass_Security",
    (kinds.SECURITY_DESCRIPTOR,),
)

SECURITY_SDS = PnpPropertyKey.register_new(
    UUID("{4321918b-f69e-470d-a5de4d88c75ad24b}"),
    26,
    "DeviceClass_SecuritySDS",
    (kinds.SECURITY_DESCRIPTOR_STRING,),
)

DEV_TYPE = PnpPropertyKey.register_new(
    UUID("{4321918b-f69e-470d-a5de4d88c75ad24b}"),
    27,
    "DeviceClass_DevType",
    (kinds.UINT32,),
)

EXCLUSIVE = PnpPropertyKey.register_new(
    UUID("{4321918b-f69e-470d-a5de4d88c75ad24b}"),
    28,
    "DeviceClass_Exclusive",
    (kinds.BOOLEAN,),
)

CHARACTERISTICS = PnpPropertyKey.register_new(
    UUID("{4321918b-f69e-470d-a5de4d88c75ad24b}"),
    29,
    "DeviceClass_Characteristics",
    (kinds.UINT32,),
)

NAME = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    2,
    "DeviceClass_Name",
    (kinds.STRING,),
)

CLASS_NAME = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    3,
    "DeviceClass_ClassName",
    (kinds.STRING,),
)

ICON = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    4,
    "DeviceClass_Icon",
    (kinds.STRING,),
)

CLASS_INSTALLER = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    5,
    "DeviceClass_ClassInstaller",
    (kinds.STRING,),
)

PROP_PAGE_PROVIDER = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    6,
    "DeviceClass_PropPageProvider",
    (kinds.STRING,),
)

NO_INSTALL_CLASS = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    7,
    "DeviceClass_NoInstallClass",
    (kinds.BOOLEAN,),
)

NO_DISPLAY_CLASS = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    8,
    "DeviceClass_NoDisplayClass",
    (kinds.BOOLEAN,),
)

SILENT_INSTALL = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    9,
    "DeviceClass_SilentInstall",
    (kinds.BOOLEAN,),
)

NO_USE_CLASS = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    10,
    "DeviceClass_NoUseClass",
    (kinds.BOOLEAN,),
)

DEFAULT_SERVICE = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    11,
    "DeviceClass_DefaultService",
    (kinds.STRING,),
)

ICON_PATH = PnpPropertyKey.register_new(
    UUID("{259abffc-50a7-47ce-af0868c9a7d73366}"),
    12,
    "DeviceClass_IconPath",
    (kinds.STRING_LIST,),
)

DHP_REBALANCE_OPT_OUT = PnpPropertyKey.register_new(
    UUID("{d14d3ef3-66cf-4ba2-9d380ddb37ab4701}"),
    2,
    "DeviceClass_DHPRebalanceOptOut",
    (kinds.BOOLEAN,),
)

CLASS_CO_INSTALLERS = PnpPropertyKey.register_new(
    UUID("{713d1703-a2e2-49f5-921456472ef3da5c}"),
    2,
    "DeviceClass_ClassCoInstallers",
    (kinds.STRING_LIST,),
)
