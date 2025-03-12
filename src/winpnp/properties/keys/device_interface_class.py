from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

DEFAULT_INTERFACE = PnpPropertyKey.register_new(
    UUID("{14c83a99-0b3f-44b7-be4ca178d3990564}"),
    2,
    "DeviceInterfaceClass_DefaultInterface",
    (kinds.STRING,),
)

NAME = PnpPropertyKey.register_new(
    UUID("{14c83a99-0b3f-44b7-be4ca178d3990564}"),
    3,
    "DeviceInterfaceClass_Name",
    (kinds.STRING,),
)
