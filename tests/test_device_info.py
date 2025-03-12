from contextlib import AbstractContextManager, nullcontext
from typing import Any, Iterator, Optional, Union, cast
from uuid import UUID

from pytest import raises
from pytest_cases import fixture, parametrize_with_cases

from winpnp.info.device import DeviceInfo
from winpnp.properties import kinds
from winpnp.properties.keys.device import INSTANCE_ID
from winpnp.properties.pnp_property import PnpProperty, PnpPropertyKey, PnpPropertyType

ROOT_INSTANCE_ID = "HTREE\\ROOT\\0"


@fixture(scope="function")  # type: ignore
def device() -> Iterator[DeviceInfo]:
    # Using the root of the device tree, since it should always exist
    with DeviceInfo.of_instance_id(ROOT_INSTANCE_ID) as d:
        yield d


def case_success_with_valid_key() -> (
    tuple[Any, AbstractContextManager[Any], Optional[PnpProperty[Any]]]
):
    return (
        INSTANCE_ID,
        nullcontext(),
        PnpProperty(ROOT_INSTANCE_ID, kinds.STRING),
    )


def case_success_when_allowed_types_not_specified() -> (
    tuple[Any, AbstractContextManager[Any], Optional[PnpProperty[Any]]]
):
    return (
        PnpPropertyKey(
            INSTANCE_ID.category, INSTANCE_ID.property_id, allowed_types=None
        ),
        nullcontext(),
        PnpProperty(ROOT_INSTANCE_ID, kinds.STRING),
    )


def case_success_with_multiple_allowed_types() -> (
    tuple[Any, AbstractContextManager[Any], Optional[PnpProperty[Any]]]
):
    return (
        PnpPropertyKey(
            INSTANCE_ID.category,
            INSTANCE_ID.property_id,
            allowed_types=(
                cast(
                    PnpPropertyType[Union[int, list[int], str]],
                    kinds.UINT32,
                ),
                cast(
                    PnpPropertyType[Union[int, list[int], str]],
                    kinds.INT64_ARRAY,
                ),
                cast(
                    PnpPropertyType[Union[int, list[int], str]],
                    kinds.STRING,
                ),
            ),
        ),
        nullcontext(),
        PnpProperty(ROOT_INSTANCE_ID, kinds.STRING),
    )


def case_raise_value_error_if_return_type_does_not_match_allowed_types() -> (
    tuple[Any, AbstractContextManager[Any], Optional[PnpProperty[Any]]]
):
    return (
        PnpPropertyKey(
            INSTANCE_ID.category, INSTANCE_ID.property_id, allowed_types=(kinds.UINT32,)
        ),
        raises(ValueError),
        None,
    )


def case_raise_key_error_if_key_is_missing() -> (
    tuple[Any, AbstractContextManager[Any], Optional[PnpProperty[Any]]]
):
    return (
        PnpPropertyKey(UUID(int=0), 0),
        raises(KeyError),
        None,
    )


def case_raise_key_error_if_key_has_incorrect_type() -> (
    tuple[Any, AbstractContextManager[Any], Optional[PnpProperty[Any]]]
):
    return (
        object(),
        raises(KeyError),
        None,
    )


@parametrize_with_cases(
    ("key", "expected_exception_context", "expected_result"), cases="."
)
def test_getitem(
    device: DeviceInfo,
    key: Any,
    expected_exception_context: AbstractContextManager[Any],
    expected_result: Optional[PnpProperty[Any]],
) -> None:
    actual_result = None

    with expected_exception_context:
        actual_result = device[key]

    assert actual_result == expected_result
