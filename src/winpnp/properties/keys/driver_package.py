from uuid import UUID

from winpnp.properties import kinds
from winpnp.properties.pnp_property import PnpPropertyKey

MODEL = PnpPropertyKey.register_new(
    UUID("{cf73bb51-3abf-44a2-85e09a3dc7a12132}"), 2, "DrvPkg_Model", (kinds.STRING,)
)

VENDOR_WEB_SITE = PnpPropertyKey.register_new(
    UUID("{cf73bb51-3abf-44a2-85e09a3dc7a12132}"),
    3,
    "DrvPkg_VendorWebSite",
    (kinds.STRING,),
)

DETAILED_DESCRIPTION = PnpPropertyKey.register_new(
    UUID("{cf73bb51-3abf-44a2-85e09a3dc7a12132}"),
    4,
    "DrvPkg_DetailedDescription",
    (kinds.STRING,),
)

DOCUMENTATION_LINK = PnpPropertyKey.register_new(
    UUID("{cf73bb51-3abf-44a2-85e09a3dc7a12132}"),
    5,
    "DrvPkg_DocumentationLink",
    (kinds.STRING,),
)

ICON = PnpPropertyKey.register_new(
    UUID("{cf73bb51-3abf-44a2-85e09a3dc7a12132}"),
    6,
    "DrvPkg_Icon",
    (kinds.STRING_LIST,),
)

BRANDING_ICON = PnpPropertyKey.register_new(
    UUID("{cf73bb51-3abf-44a2-85e09a3dc7a12132}"),
    7,
    "DrvPkg_BrandingIcon",
    (kinds.STRING_LIST,),
)
