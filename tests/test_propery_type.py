from typing import Any, Callable, Iterator, Optional

from pytest_cases import fixture, parametrize_with_cases

from winpnp.properties.decoding import decode_raw
from winpnp.properties.pnp_property import PnpPropertyType

TEST_TYPE_NAME = "test_property_type"
TEST_TYPE_ID = 0xFFFFFFFF

TypeTestParams = tuple[
    Optional[PnpPropertyType[Any]], bool, Optional[str], Callable[[bytes], Any]
]


def _test_decoder(data: bytes) -> None:
    return None


@fixture(scope="function")  # type: ignore
def registered_type() -> Iterator[PnpPropertyType[None]]:
    kind = PnpPropertyType.register_new(TEST_TYPE_ID, TEST_TYPE_NAME, _test_decoder)
    try:
        yield kind
    finally:
        del PnpPropertyType._NAME_TO_ID[TEST_TYPE_NAME]
        del PnpPropertyType._DERIVED_DATA[TEST_TYPE_ID]


def case_lookup_not_registered_by_id() -> TypeTestParams:
    return PnpPropertyType(TEST_TYPE_ID), False, None, decode_raw


def case_lookup_not_registered_by_name() -> TypeTestParams:
    return PnpPropertyType.from_name(TEST_TYPE_NAME), True, None, decode_raw


def case_lookup_registered_by_id(
    registered_type: PnpPropertyType[None],
) -> TypeTestParams:
    return PnpPropertyType(TEST_TYPE_ID), False, TEST_TYPE_NAME, _test_decoder


def case_lookup_registered_by_name(
    registered_type: PnpPropertyType[None],
) -> TypeTestParams:
    return (
        PnpPropertyType.from_name(TEST_TYPE_NAME),
        False,
        TEST_TYPE_NAME,
        _test_decoder,
    )


@parametrize_with_cases(
    ("kind", "should_be_none", "expected_name", "expected_decoder"), cases="."
)
def test_registration(
    kind: Optional[PnpPropertyType[Any]],
    should_be_none: bool,
    expected_name: Optional[str],
    expected_decoder: Callable[[bytes], Any],
) -> None:
    assert (kind is None) == should_be_none

    if kind is not None:
        assert kind.name == expected_name
        assert kind._decoder is expected_decoder
