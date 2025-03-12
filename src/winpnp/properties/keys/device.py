from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

DEVICE_DESC = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    2,
    "Device_DeviceDesc",
    (kinds.STRING,),
)

HARDWARE_IDS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    3,
    "Device_HardwareIds",
    (kinds.STRING_LIST,),
)


COMPATIBLE_IDS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    4,
    "Device_CompatibleIds",
    (kinds.STRING_LIST,),
)

SERVICE = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"), 6, "Device_Service", (kinds.STRING,)
)

CLASS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"), 9, "Device_Class", (kinds.STRING,)
)

CLASS_GUID = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"), 10, "Device_ClassGuid", (kinds.GUID,)
)

DRIVER = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"), 11, "Device_Driver", (kinds.STRING,)
)

CONFIG_FLAGS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    12,
    "Device_ConfigFlags",
    (kinds.UINT32,),
)

MANUFACTURER = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    13,
    "Device_Manufacturer",
    (kinds.STRING,),
)

FRIENDLY_NAME = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    14,
    "Device_FriendlyName",
    (kinds.STRING,),
)

LOCATION_INFO = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    15,
    "Device_LocationInfo",
    (kinds.STRING,),
)

PDO_NAME = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"), 16, "Device_PDOName", (kinds.STRING,)
)

CAPABILITIES = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    17,
    "Device_Capabilities",
    (kinds.UINT32,),
)

UI_NUMBER = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    18,
    "Device_UINumber",
    (kinds.UINT32,),
)

UPPER_FILTERS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    19,
    "Device_UpperFilters",
    (kinds.STRING_LIST,),
)

LOWER_FILTERS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    20,
    "Device_LowerFilters",
    (kinds.STRING_LIST,),
)

BUS_TYPE_GUID = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    21,
    "Device_BusTypeGuid",
    (kinds.GUID,),
)

LEGACY_BUS_TYPE = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    22,
    "Device_LegacyBusType",
    (kinds.UINT32,),
)

BUS_NUMBER = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    23,
    "Device_BusNumber",
    (kinds.UINT32,),
)

ENUMERATOR_NAME = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    24,
    "Device_EnumeratorName",
    (kinds.STRING,),
)

SECURITY = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    25,
    "Device_Security",
    (kinds.SECURITY_DESCRIPTOR,),
)

SECURITY_SDS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    26,
    "Device_SecuritySDS",
    (kinds.SECURITY_DESCRIPTOR_STRING,),
)

DEV_TYPE = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"), 27, "Device_DevType", (kinds.UINT32,)
)

EXCLUSIVE = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    28,
    "Device_Exclusive",
    (kinds.BOOLEAN,),
)

CHARACTERISTICS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    29,
    "Device_Characteristics",
    (kinds.UINT32,),
)

ADDRESS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"), 30, "Device_Address", (kinds.UINT32,)
)

UI_NUMBER_DESC_FORMAT = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    31,
    "Device_UINumberDescFormat",
    (kinds.STRING,),
)

POWER_DATA = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    32,
    "Device_PowerData",
    (kinds.BYTE_ARRAY,),
)

REMOVAL_POLICY = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    33,
    "Device_RemovalPolicy",
    (kinds.UINT32,),
)

REMOVAL_POLICY_DEFAULT = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    34,
    "Device_RemovalPolicyDefault",
    (kinds.UINT32,),
)

REMOVAL_POLICY_OVERRIDE = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    35,
    "Device_RemovalPolicyOverride",
    (kinds.UINT32,),
)

INSTALL_STATE = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    36,
    "Device_InstallState",
    (kinds.UINT32,),
)

LOCATION_PATHS = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    37,
    "Device_LocationPaths",
    (kinds.STRING_LIST,),
)

BASE_CONTAINER_ID = PnpPropertyKey.register_new(
    UUID("{a45c254e-df1c-4efd-802067d146a850e0}"),
    38,
    "Device_BaseContainerId",
    (kinds.GUID,),
)

INSTANCE_ID = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"),
    256,
    "Device_InstanceId",
    (kinds.STRING,),
)

DEV_NODE_STATUS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    2,
    "Device_DevNodeStatus",
    (kinds.UINT32,),
)

PROBLEM_CODE = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    3,
    "Device_ProblemCode",
    (kinds.UINT32,),
)

EJECTION_RELATIONS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    4,
    "Device_EjectionRelations",
    (kinds.STRING_LIST,),
)

REMOVAL_RELATIONS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    5,
    "Device_RemovalRelations",
    (kinds.STRING_LIST,),
)

POWER_RELATIONS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    6,
    "Device_PowerRelations",
    (kinds.STRING_LIST,),
)

BUS_RELATIONS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    7,
    "Device_BusRelations",
    (kinds.STRING_LIST,),
)

PARENT = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"), 8, "Device_Parent", (kinds.STRING,)
)

CHILDREN = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    9,
    "Device_Children",
    (kinds.STRING_LIST,),
)

SIBLINGS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    10,
    "Device_Siblings",
    (kinds.STRING_LIST,),
)

TRANSPORT_RELATIONS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    11,
    "Device_TransportRelations",
    (kinds.STRING_LIST,),
)

PROBLEM_STATUS = PnpPropertyKey.register_new(
    UUID("{4340a6c5-93fa-4706-972c7b648008a5a7}"),
    12,
    "Device_ProblemStatus",
    (kinds.NTSTATUS,),
)

REPORTED = PnpPropertyKey.register_new(
    UUID("{80497100-8c73-48b9-aad9ce387e19c56e}"),
    2,
    "Device_Reported",
    (kinds.BOOLEAN,),
)

LEGACY = PnpPropertyKey.register_new(
    UUID("{80497100-8c73-48b9-aad9ce387e19c56e}"), 3, "Device_Legacy", (kinds.BOOLEAN,)
)

CONTAINER_ID = PnpPropertyKey.register_new(
    UUID("{8c7ed206-3f8a-4827-b3abae9e1faefc6c}"),
    2,
    "Device_ContainerId",
    (kinds.GUID,),
)

IN_LOCAL_MACHINE_CONTAINER = PnpPropertyKey.register_new(
    UUID("{8c7ed206-3f8a-4827-b3abae9e1faefc6c}"),
    4,
    "Device_InLocalMachineContainer",
    (kinds.BOOLEAN,),
)

MODEL = PnpPropertyKey.register_new(
    UUID("{78c34fc8-104a-4aca-9ea4524d52996e57}"), 39, "Device_Model", (kinds.STRING,)
)

MODEL_ID = PnpPropertyKey.register_new(
    UUID("{80d81ea6-7473-4b0c-8216efc11a2c4c8b}"), 2, "Device_ModelId", (kinds.GUID,)
)

FRIENDLY_NAME_ATTRIBUTES = PnpPropertyKey.register_new(
    UUID("{80d81ea6-7473-4b0c-8216efc11a2c4c8b}"),
    3,
    "Device_FriendlyNameAttributes",
    (kinds.UINT32,),
)

MANUFACTURER_ATTRIBUTES = PnpPropertyKey.register_new(
    UUID("{80d81ea6-7473-4b0c-8216efc11a2c4c8b}"),
    4,
    "Device_ManufacturerAttributes",
    (kinds.UINT32,),
)

PRESENCE_NOT_FOR_DEVICE = PnpPropertyKey.register_new(
    UUID("{80d81ea6-7473-4b0c-8216efc11a2c4c8b}"),
    5,
    "Device_PresenceNotForDevice",
    (kinds.BOOLEAN,),
)

SIGNAL_STRENGTH = PnpPropertyKey.register_new(
    UUID("{80d81ea6-7473-4b0c-8216efc11a2c4c8b}"),
    6,
    "Device_SignalStrength",
    (kinds.INT32,),
)

IS_ASSOCIATEABLE_BY_USER_ACTION = PnpPropertyKey.register_new(
    UUID("{80d81ea6-7473-4b0c-8216efc11a2c4c8b}"),
    7,
    "Device_IsAssociateableByUserAction",
    (kinds.BOOLEAN,),
)

SHOW_IN_UNINSTALL_UI = PnpPropertyKey.register_new(
    UUID("{80d81ea6-7473-4b0c-8216efc11a2c4c8b}"),
    8,
    "Device_ShowInUninstallUI",
    (kinds.BOOLEAN,),
)

COMPANION_APPS = PnpPropertyKey.register_new(
    UUID("{6a742654-d0b2-4420-a523e068352ac1df}"),
    2,
    "Device_CompanionApps",
    (kinds.STRING_LIST,),
)

PRIMARY_COMPANION_APP = PnpPropertyKey.register_new(
    UUID("{6a742654-d0b2-4420-a523e068352ac1df}"),
    3,
    "Device_PrimaryCompanionApp",
    (kinds.STRING,),
)

NUMA_PROXIMITY_DOMAIN = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    1,
    "Device_Numa_Proximity_Domain",
    (kinds.UINT32,),
)

DHP_REBALANCE_POLICY = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    2,
    "Device_DHP_Rebalance_Policy",
    (kinds.UINT32,),
)

NUMA_NODE = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    3,
    "Device_Numa_Node",
    (kinds.UINT32,),
)

BUS_REPORTED_DEVICE_DESC = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    4,
    "Device_BusReportedDeviceDesc",
    (kinds.STRING,),
)

IS_PRESENT = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    5,
    "Device_IsPresent",
    (kinds.BOOLEAN,),
)

HAS_PROBLEM = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    6,
    "Device_HasProblem",
    (kinds.BOOLEAN,),
)

CONFIGURATION_ID = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    7,
    "Device_ConfigurationId",
    (kinds.STRING,),
)

REPORTED_DEVICE_IDS_HASH = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    8,
    "Device_ReportedDeviceIdsHash",
    (kinds.UINT32,),
)

PHYSICAL_DEVICE_LOCATION = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    9,
    "Device_PhysicalDeviceLocation",
    (kinds.BYTE_ARRAY,),
)

BIOS_DEVICE_NAME = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    10,
    "Device_BiosDeviceName",
    (kinds.STRING,),
)

DRIVER_PROBLEM_DESC = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    11,
    "Device_DriverProblemDesc",
    (kinds.STRING,),
)

DEBUGGER_SAFE = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    12,
    "Device_DebuggerSafe",
    (kinds.UINT32,),
)

POST_INSTALL_IN_PROGRESS = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    13,
    "Device_PostInstallInProgress",
    (kinds.BOOLEAN,),
)

STACK = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    14,
    "Device_Stack",
    (kinds.STRING_LIST,),
)

EXTENDED_CONFIGURATION_IDS = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    15,
    "Device_ExtendedConfigurationIds",
    (kinds.STRING_LIST,),
)

IS_REBOOT_REQUIRED = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    16,
    "Device_IsRebootRequired",
    (kinds.BOOLEAN,),
)

FIRMWARE_DATE = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    17,
    "Device_FirmwareDate",
    (kinds.FILETIME,),
)

FIRMWARE_VERSION = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    18,
    "Device_FirmwareVersion",
    (kinds.STRING,),
)

FIRMWARE_REVISION = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    19,
    "Device_FirmwareRevision",
    (kinds.STRING,),
)

DEPENDENCY_PROVIDERS = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    20,
    "Device_DependencyProviders",
    (kinds.STRING_LIST,),
)

DEPENDENCY_DEPENDENTS = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    21,
    "Device_DependencyDependents",
    (kinds.STRING_LIST,),
)

SOFT_RESTART_SUPPORTED = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    22,
    "Device_SoftRestartSupported",
    (kinds.BOOLEAN,),
)

EXTENDED_ADDRESS = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    23,
    "Device_ExtendedAddress",
    (kinds.UINT64,),
)

ASSIGNED_TO_GUEST = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    24,
    "Device_AssignedToGuest",
    (kinds.BOOLEAN,),
)

CREATOR_PROCESS_ID = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    25,
    "Device_CreatorProcessId",
    (kinds.UINT32,),
)

FIRMWARE_VENDOR = PnpPropertyKey.register_new(
    UUID("{540b947e-8b40-45bc-a8a26a0b894cbda2}"),
    26,
    "Device_FirmwareVendor",
    (kinds.STRING,),
)

SESSION_ID = PnpPropertyKey.register_new(
    UUID("{83da6326-97a6-4088-9453a1923f573b29}"),
    6,
    "Device_SessionId",
    (kinds.UINT32,),
)

INSTALL_DATE = PnpPropertyKey.register_new(
    UUID("{83da6326-97a6-4088-9453a1923f573b29}"),
    100,
    "Device_InstallDate",
    (kinds.FILETIME,),
)

FIRST_INSTALL_DATE = PnpPropertyKey.register_new(
    UUID("{83da6326-97a6-4088-9453a1923f573b29}"),
    101,
    "Device_FirstInstallDate",
    (kinds.FILETIME,),
)

LAST_ARRIVAL_DATE = PnpPropertyKey.register_new(
    UUID("{83da6326-97a6-4088-9453a1923f573b29}"),
    102,
    "Device_LastArrivalDate",
    (kinds.FILETIME,),
)

LAST_REMOVAL_DATE = PnpPropertyKey.register_new(
    UUID("{83da6326-97a6-4088-9453a1923f573b29}"),
    103,
    "Device_LastRemovalDate",
    (kinds.FILETIME,),
)

DRIVER_DATE = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    2,
    "Device_DriverDate",
    (kinds.FILETIME,),
)

DRIVER_VERSION = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    3,
    "Device_DriverVersion",
    (kinds.STRING,),
)

DRIVER_DESC = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    4,
    "Device_DriverDesc",
    (kinds.STRING,),
)

DRIVER_INF_PATH = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    5,
    "Device_DriverInfPath",
    (kinds.STRING,),
)

DRIVER_INF_SECTION = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    6,
    "Device_DriverInfSection",
    (kinds.STRING,),
)

DRIVER_INF_SECTION_EXT = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    7,
    "Device_DriverInfSectionExt",
    (kinds.STRING,),
)

MATCHING_DEVICE_ID = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    8,
    "Device_MatchingDeviceId",
    (kinds.STRING,),
)

DRIVER_PROVIDER = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    9,
    "Device_DriverProvider",
    (kinds.STRING,),
)

DRIVER_PROP_PAGE_PROVIDER = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    10,
    "Device_DriverPropPageProvider",
    (kinds.STRING,),
)

DRIVER_CO_INSTALLERS = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    11,
    "Device_DriverCoInstallers",
    (kinds.STRING_LIST,),
)

RESOURCE_PICKER_TAGS = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    12,
    "Device_ResourcePickerTags",
    (kinds.STRING,),
)

RESOURCE_PICKER_EXCEPTIONS = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    13,
    "Device_ResourcePickerExceptions",
    (kinds.STRING,),
)

DRIVER_RANK = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    14,
    "Device_DriverRank",
    (kinds.UINT32,),
)

DRIVER_LOGO_LEVEL = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    15,
    "Device_DriverLogoLevel",
    (kinds.UINT32,),
)

NO_CONNECT_SOUND = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    17,
    "Device_NoConnectSound",
    (kinds.BOOLEAN,),
)

GENERIC_DRIVER_INSTALLED = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    18,
    "Device_GenericDriverInstalled",
    (kinds.BOOLEAN,),
)

ADDITIONAL_SOFTWARE_REQUESTED = PnpPropertyKey.register_new(
    UUID("{a8b865dd-2e3d-4094-ad97e593a70c75d6}"),
    19,
    "Device_AdditionalSoftwareRequested",
    (kinds.BOOLEAN,),
)

SAFE_REMOVAL_REQUIRED = PnpPropertyKey.register_new(
    UUID("{afd97640-86a3-4210-b67c289c41aabe55}"),
    2,
    "Device_SafeRemovalRequired",
    (kinds.BOOLEAN,),
)

SAFE_REMOVAL_REQUIRED_OVERRIDE = PnpPropertyKey.register_new(
    UUID("{afd97640-86a3-4210-b67c289c41aabe55}"),
    3,
    "Device_SafeRemovalRequiredOverride",
    (kinds.BOOLEAN,),
)
