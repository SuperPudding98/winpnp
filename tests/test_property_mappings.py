from collections.abc import Mapping
from contextlib import AbstractContextManager, nullcontext
from dataclasses import dataclass
from typing import Any, Iterator, Optional, cast
from uuid import UUID

from pytest import raises
from pytest_cases import fixture, parametrize, parametrize_with_cases

from winpnp.info.device import DeviceInfo
from winpnp.info.setup_class import SetupClassInfo
from winpnp.properties import keys, kinds
from winpnp.properties.pnp_property import PnpProperty, PnpPropertyKey, PnpPropertyType

ROOT_INSTANCE_ID = "HTREE\\ROOT\\0"
UNKNOWN_CLASS_GUID = UUID("4d36e97e-e325-11ce-bfc1-08002be10318")
UNKNOWN_CLASS_NAME = "Unknown"

GetitemTestParams = tuple[
    Mapping[PnpPropertyKey[Any], PnpProperty[Any]],
    Any,
    Optional[PnpProperty[Any]],
    AbstractContextManager[Any],
]


@dataclass()
class PnpMappingTestData:
    mapping: Mapping[PnpPropertyKey[Any], PnpProperty[Any]]
    valid_key: PnpPropertyKey[Any]
    expected_value: PnpProperty[Any]


@fixture(scope="function")  # type: ignore
def device() -> Iterator[PnpMappingTestData]:
    # Using the root of the device tree, since it should always exist
    with DeviceInfo.of_instance_id(ROOT_INSTANCE_ID) as d:
        yield PnpMappingTestData(
            d, keys.device.INSTANCE_ID, PnpProperty(ROOT_INSTANCE_ID, kinds.STRING)
        )


@fixture(scope="function")  # type: ignore
def setup_class() -> PnpMappingTestData:
    return PnpMappingTestData(
        SetupClassInfo(UNKNOWN_CLASS_GUID),
        keys.device_class.CLASS_NAME,
        PnpProperty(UNKNOWN_CLASS_NAME, kinds.STRING),
    )


@parametrize("data", (device, setup_class))
def case_success_with_valid_key(
    data: PnpMappingTestData,
) -> GetitemTestParams:
    return data.mapping, data.valid_key, data.expected_value, nullcontext()


@parametrize("data", (device, setup_class))
def case_success_when_allowed_types_not_specified(
    data: PnpMappingTestData,
) -> GetitemTestParams:
    return (
        data.mapping,
        PnpPropertyKey(
            data.valid_key.category, data.valid_key.property_id, allowed_types=None
        ),
        data.expected_value,
        nullcontext(),
    )


@parametrize("data", (device, setup_class))
def case_success_with_multiple_allowed_types(
    data: PnpMappingTestData,
) -> GetitemTestParams:
    return (
        data.mapping,
        PnpPropertyKey(
            data.valid_key.category,
            data.valid_key.property_id,
            allowed_types=(
                cast(PnpPropertyType[Any], kinds.UINT32),
                cast(PnpPropertyType[Any], kinds.INT16_ARRAY),
                data.expected_value.kind,
            ),
        ),
        data.expected_value,
        nullcontext(),
    )


@parametrize("data", (device, setup_class))
def case_raise_value_error_if_return_type_does_not_match_allowed_types(
    data: PnpMappingTestData,
) -> GetitemTestParams:
    return (
        data.mapping,
        PnpPropertyKey(
            data.valid_key.category,
            data.valid_key.property_id,
            allowed_types=(kinds.NULL,),
        ),
        None,
        raises(ValueError),
    )


@parametrize("data", (device, setup_class))
def case_raise_key_error_if_key_is_missing(
    data: PnpMappingTestData,
) -> GetitemTestParams:
    return data.mapping, PnpPropertyKey(UUID(int=0), 0), None, raises(KeyError)


@parametrize("data", (device, setup_class))
def case_raise_key_error_if_key_has_incorrect_type(
    data: PnpMappingTestData,
) -> GetitemTestParams:
    return data.mapping, object(), None, raises(KeyError)


@parametrize_with_cases(
    ("mapping", "key", "expected_result", "expected_exception_context"), cases="."
)
def test_getitem(
    mapping: Mapping[PnpPropertyKey[Any], PnpProperty[Any]],
    key: Any,
    expected_result: Optional[PnpProperty[Any]],
    expected_exception_context: AbstractContextManager[Any],
) -> None:
    actual_result = None

    with expected_exception_context:
        actual_result = mapping[key]

    assert actual_result == expected_result
