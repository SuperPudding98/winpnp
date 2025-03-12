from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

from . import (
    dev_query,
    device,
    device_class,
    device_container,
    device_interface,
    device_interface_class,
    driver_package,
)

NAME = PnpPropertyKey.register_new(
    UUID("{b725f130-47ef-101a-a5f102608c9eebac}"), 10, "NAME", (kinds.STRING,)
)
