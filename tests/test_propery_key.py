from typing import Any, Iterator, Optional
from uuid import UUID

from pytest_cases import fixture, parametrize_with_cases

from winpnp.properties.pnp_property import PnpPropertyKey, PnpPropertyType

TEST_KEY_NAME = "test_property_key"
TEST_KEY_CATEGORY = UUID("{00000000-0000-0000-0000000000000000}")
TEST_KEY_PROP_ID = 0
TEST_TYPE_ID = 0xFFFFFFFF


KeyTestParams = tuple[
    Optional[PnpPropertyKey[Any]],
    bool,
    Optional[str],
    Optional[dict[int, PnpPropertyType[Any]]],
]


@fixture(scope="function")  # type: ignore
def registered_key() -> Iterator[PnpPropertyKey[None]]:
    key = PnpPropertyKey.register_new(
        TEST_KEY_CATEGORY,
        TEST_KEY_PROP_ID,
        TEST_KEY_NAME,
        (PnpPropertyType(TEST_TYPE_ID),),
    )
    try:
        yield key
    finally:
        del PnpPropertyKey._NAME_TO_ID[TEST_KEY_NAME]
        del PnpPropertyKey._DERIVED_DATA[(TEST_KEY_CATEGORY, TEST_KEY_PROP_ID)]


def case_lookup_not_registered_by_id() -> KeyTestParams:
    return PnpPropertyKey(TEST_KEY_CATEGORY, TEST_KEY_PROP_ID), False, None, None


def case_lookup_not_registered_by_name() -> KeyTestParams:
    return PnpPropertyKey.from_name(TEST_KEY_NAME), True, None, None


def case_lookup_registered_by_id(registered_key: PnpPropertyKey[None]) -> KeyTestParams:
    return (
        PnpPropertyKey(TEST_KEY_CATEGORY, TEST_KEY_PROP_ID),
        False,
        TEST_KEY_NAME,
        None,
    )


def case_lookup_registered_by_name(
    registered_key: PnpPropertyKey[None],
) -> KeyTestParams:
    return (
        PnpPropertyKey.from_name(TEST_KEY_NAME),
        False,
        TEST_KEY_NAME,
        {TEST_TYPE_ID: PnpPropertyType(TEST_TYPE_ID)},
    )


@parametrize_with_cases(
    ("key", "should_be_none", "expected_name", "expected_allowed_types"), cases="."
)
def test_registration(
    key: Optional[PnpPropertyKey[Any]],
    should_be_none: bool,
    expected_name: Optional[str],
    expected_allowed_types: Optional[dict[int, PnpPropertyType[Any]]],
) -> None:
    assert (key is None) == should_be_none

    if key is not None:
        assert key.name == expected_name
        assert key.allowed_types == expected_allowed_types
