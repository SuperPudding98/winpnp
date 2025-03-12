from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

DEVICE_ADDRESS = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    1,
    "Bluetooth_DeviceAddress",
    (kinds.STRING,),
)

SERVICE_GUID = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    2,
    "Bluetooth_ServiceGUID",
    (kinds.GUID,),
)

DEVICE_FLAGS = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    3,
    "Bluetooth_DeviceFlags",
    (kinds.UINT32,),
)

DEVICE_MANUFACTURER = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    4,
    "Bluetooth_DeviceManufacturer",
    (kinds.STRING,),
)

DEVICE_MODEL_NUMBER = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    5,
    "Bluetooth_DeviceModelNumber",
    (kinds.STRING,),
)

DEVICE_VID_SOURCE = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    6,
    "Bluetooth_DeviceVIDSource",
    (kinds.BYTE,),
)

DEVICE_VID = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    7,
    "Bluetooth_DeviceVID",
    (kinds.UINT16,),
)

DEVICE_PID = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    8,
    "Bluetooth_DevicePID",
    (kinds.UINT16,),
)

DEVICE_PRODUCT_VERSION = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    9,
    "Bluetooth_DeviceProductVersion",
    (kinds.UINT16,),
)

CLASS_OF_DEVICE = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    10,
    "Bluetooth_ClassOfDevice",
    (kinds.UINT32,),
)

LAST_CONNECTED_TIME = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    11,
    "Bluetooth_LastConnectedTime",
    (kinds.FILETIME,),
)

LAST_SEEN_TIME = PnpPropertyKey.register_new(
    UUID("{2bd67d8b-8beb-48d5-87e06cda3428040a}"),
    12,
    "Bluetooth_LastSeenTime",
    (kinds.FILETIME,),
)
