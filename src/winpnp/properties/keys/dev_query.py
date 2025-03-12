from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

OBJECT_TYPE = PnpPropertyKey.register_new(
    UUID("{13673f42-a3d6-49f6-b4daae46e0c5237c}"),
    2,
    "DevQuery_ObjectType",
    (kinds.UINT32,),
)
