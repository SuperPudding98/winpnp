from typing import Union, cast
from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey, PnpPropertyType

ADDRESS = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    51,
    "DeviceContainer_Address",
    (
        cast(PnpPropertyType[Union[str, list[str]]], kinds.STRING),
        cast(PnpPropertyType[Union[str, list[str]]], kinds.STRING_LIST),
    ),
)

DISCOVERY_METHOD = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    52,
    "DeviceContainer_DiscoveryMethod",
    (kinds.STRING_LIST,),
)

IS_ENCRYPTED = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    53,
    "DeviceContainer_IsEncrypted",
    (kinds.BOOLEAN,),
)

IS_AUTHENTICATED = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    54,
    "DeviceContainer_IsAuthenticated",
    (kinds.BOOLEAN,),
)

IS_CONNECTED = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    55,
    "DeviceContainer_IsConnected",
    (kinds.BOOLEAN,),
)

IS_PAIRED = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    56,
    "DeviceContainer_IsPaired",
    (kinds.BOOLEAN,),
)

ICON = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    57,
    "DeviceContainer_Icon",
    (kinds.STRING,),
)

VERSION = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    65,
    "DeviceContainer_Version",
    (kinds.STRING,),
)

LAST_SEEN = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    66,
    "DeviceContainer_Last_Seen",
    (kinds.FILETIME,),
)

LAST_CONNECTED = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    67,
    "DeviceContainer_Last_Connected",
    (kinds.FILETIME,),
)

IS_SHOW_IN_DISCONNECTED_STATE = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    68,
    "DeviceContainer_IsShowInDisconnectedState",
    (kinds.BOOLEAN,),
)

IS_LOCAL_MACHINE = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    70,
    "DeviceContainer_IsLocalMachine",
    (kinds.BOOLEAN,),
)

METADATA_PATH = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    71,
    "DeviceContainer_MetadataPath",
    (kinds.STRING,),
)

IS_METADATA_SEARCH_IN_PROGRESS = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    72,
    "DeviceContainer_IsMetadataSearchInProgress",
    (kinds.BOOLEAN,),
)

METADATA_CHECKSUM = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    73,
    "DeviceContainer_MetadataChecksum",
    (kinds.BYTE_ARRAY,),
)

IS_NOT_INTERESTING_FOR_DISPLAY = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    74,
    "DeviceContainer_IsNotInterestingForDisplay",
    (kinds.BOOLEAN,),
)

LAUNCH_DEVICE_STAGE_ON_DEVICE_CONNECT = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    76,
    "DeviceContainer_LaunchDeviceStageOnDeviceConnect",
    (kinds.BOOLEAN,),
)

LAUNCH_DEVICE_STAGE_FROM_EXPLORER = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    77,
    "DeviceContainer_LaunchDeviceStageFromExplorer",
    (kinds.BOOLEAN,),
)

BASELINE_EXPERIENCE_ID = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    78,
    "DeviceContainer_BaselineExperienceId",
    (kinds.GUID,),
)

IS_DEVICE_UNIQUELY_IDENTIFIABLE = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    79,
    "DeviceContainer_IsDeviceUniquelyIdentifiable",
    (kinds.BOOLEAN,),
)

ASSOCIATION_ARRAY = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    80,
    "DeviceContainer_AssociationArray",
    (kinds.STRING_LIST,),
)

DEVICE_DESCRIPTION1 = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    81,
    "DeviceContainer_DeviceDescription1",
    (kinds.STRING,),
)

DEVICE_DESCRIPTION2 = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    82,
    "DeviceContainer_DeviceDescription2",
    (kinds.STRING,),
)

HAS_PROBLEM = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    83,
    "DeviceContainer_HasProblem",
    (kinds.BOOLEAN,),
)

IS_SHARED_DEVICE = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    84,
    "DeviceContainer_IsSharedDevice",
    (kinds.BOOLEAN,),
)

IS_NETWORK_DEVICE = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    85,
    "DeviceContainer_IsNetworkDevice",
    (kinds.BOOLEAN,),
)

IS_DEFAULT_DEVICE = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    86,
    "DeviceContainer_IsDefaultDevice",
    (kinds.BOOLEAN,),
)

METADATA_CABINET = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    87,
    "DeviceContainer_MetadataCabinet",
    (kinds.STRING,),
)

REQUIRES_PAIRING_ELEVATION = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    88,
    "DeviceContainer_RequiresPairingElevation",
    (kinds.BOOLEAN,),
)

EXPERIENCE_ID = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    89,
    "DeviceContainer_ExperienceId",
    (kinds.GUID,),
)

CATEGORY = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    90,
    "DeviceContainer_Category",
    (kinds.STRING_LIST,),
)

CATEGORY_DESC_SINGULAR = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    91,
    "DeviceContainer_Category_Desc_Singular",
    (kinds.STRING_LIST,),
)

CATEGORY_DESC_PLURAL = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    92,
    "DeviceContainer_Category_Desc_Plural",
    (kinds.STRING_LIST,),
)

CATEGORY_ICON = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    93,
    "DeviceContainer_Category_Icon",
    (kinds.STRING,),
)

CATEGORY_GROUP_DESC = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    94,
    "DeviceContainer_CategoryGroup_Desc",
    (kinds.STRING_LIST,),
)

CATEGORY_GROUP_ICON = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    95,
    "DeviceContainer_CategoryGroup_Icon",
    (kinds.STRING,),
)

PRIMARY_CATEGORY = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    97,
    "DeviceContainer_PrimaryCategory",
    (kinds.STRING,),
)

UNPAIR_UNINSTALL = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    98,
    "DeviceContainer_UnpairUninstall",
    (kinds.BOOLEAN,),
)

REQUIRES_UNINSTALL_ELEVATION = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    99,
    "DeviceContainer_RequiresUninstallElevation",
    (kinds.BOOLEAN,),
)

DEVICE_FUNCTION_SUB_RANK = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    100,
    "DeviceContainer_DeviceFunctionSubRank",
    (kinds.UINT32,),
)

ALWAYS_SHOW_DEVICE_AS_CONNECTED = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    101,
    "DeviceContainer_AlwaysShowDeviceAsConnected",
    (kinds.BOOLEAN,),
)

CONFIG_FLAGS = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    105,
    "DeviceContainer_ConfigFlags",
    (kinds.UINT32,),
)

PRIVILEGED_PACKAGE_FAMILY_NAMES = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    106,
    "DeviceContainer_PrivilegedPackageFamilyNames",
    (kinds.STRING_LIST,),
)

CUSTOM_PRIVILEGED_PACKAGE_FAMILY_NAMES = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    107,
    "DeviceContainer_CustomPrivilegedPackageFamilyNames",
    (kinds.STRING_LIST,),
)

IS_REBOOT_REQUIRED = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    108,
    "DeviceContainer_IsRebootRequired",
    (kinds.BOOLEAN,),
)

FRIENDLY_NAME = PnpPropertyKey.register_new(
    UUID("{656A3BB3-ECC0-43FD-84774AE0404A96CD}"),
    12288,
    "DeviceContainer_FriendlyName",
    (kinds.STRING,),
)

MANUFACTURER = PnpPropertyKey.register_new(
    UUID("{656A3BB3-ECC0-43FD-84774AE0404A96CD}"),
    8192,
    "DeviceContainer_Manufacturer",
    (kinds.STRING,),
)

MODEL_NAME = PnpPropertyKey.register_new(
    UUID("{656A3BB3-ECC0-43FD-84774AE0404A96CD}"),
    8194,
    "DeviceContainer_ModelName",
    (kinds.STRING,),
)

MODEL_NUMBER = PnpPropertyKey.register_new(
    UUID("{656A3BB3-ECC0-43FD-84774AE0404A96CD}"),
    8195,
    "DeviceContainer_ModelNumber",
    (kinds.STRING,),
)

INSTALL_IN_PROGRESS = PnpPropertyKey.register_new(
    UUID("{83da6326-97a6-4088-9453a1923f573b29}"),
    9,
    "DeviceContainer_InstallInProgress",
    (kinds.BOOLEAN,),
)
