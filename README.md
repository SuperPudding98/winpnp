# winpnp

This is a package for interacting with Windows Plug and Play (PnP) entities (devices, setup classes, etc.)

It can be used to query properties of PnP devices using the `winpnp.info.device.DeviceInfo` class.<br/>
Instances of this class can be used as mappings, with keys of type `winpnp.properties.pnp_property.PnpPropertyKey`.<br/>
For your convenience, commonly used property keys are defined in `winpnp.properties.keys`.

Here is an example usage:
```python
from winpnp.info.device import DeviceInfo
from winpnp.properties.keys.device import INSTANCE_ID

with DeviceInfo.of_instance_id("HTREE\\ROOT\\0") as device:
    instance_id = device[INSTANCE_ID]

instance_id
```
Output: `PnpProperty(value='HTREE\\ROOT\\0', kind=PnpPropertyType(type_id=18, name='STRING'))`
