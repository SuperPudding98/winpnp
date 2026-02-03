from dataclasses import dataclass, field
from typing import Any, Callable, ClassVar, Generic, Iterable, Optional, TypeVar
from uuid import UUID

from .decoding import decode_raw

T = TypeVar("T")
U = TypeVar("U")


@dataclass(init=False)
class PnpPropertyType(Generic[T]):
    """
    Represents a type of PnP properties. This is an abstraction over the Windows DEVPROP_TYPE constants.
    """

    _DERIVED_DATA: ClassVar[dict[int, tuple[str, Callable[[bytes], Any]]]] = {}

    type_id: int
    name: Optional[str] = field(compare=False)
    _decoder: Callable[[bytes], T] = field(repr=False, compare=False)

    def __init__(
        self,
        type_id: int,
        name: Optional[str] = None,
        decoder: Optional[Callable[[bytes], T]] = None,
    ) -> None:
        derived_name, derived_decoder = self._DERIVED_DATA.get(
            type_id, (None, decode_raw)
        )

        self.type_id = type_id
        self.name = name if name is not None else derived_name
        self._decoder = decoder if decoder is not None else derived_decoder

    @staticmethod
    def register(kind: "PnpPropertyType[U]") -> None:
        """
        Registers the name and decoder of the specified `PnpPropertyType` as the default name and decoder for other instances with the same `type_id`.
        """
        if kind.name is None:
            raise ValueError(f"Cannot register {repr(kind)} because it is unnamed.")

        if kind.type_id in PnpPropertyType._DERIVED_DATA:
            raise ValueError(
                f"Cannot register {repr(kind)} because its type_id is already registered with name {PnpPropertyType._DERIVED_DATA[kind.type_id][0]}"
            )

        PnpPropertyType._DERIVED_DATA[kind.type_id] = (kind.name, kind._decoder)

    @staticmethod
    def register_new(
        type_id: int,
        name: str,
        decoder: Callable[[bytes], U],
    ) -> "PnpPropertyType[U]":
        """
        Creates a new `PnpPropertyType`, registers it, and returns it.
        """
        kind = PnpPropertyType(type_id, name, decoder)
        PnpPropertyType.register(kind)
        return kind

    def decode(self, data: bytes) -> T:
        """
        Decodes raw bytes to the actual python type that this `PnpPropertyType` represents.
        """
        return self._decoder(data)


@dataclass(init=False, frozen=True)
class PnpPropertyKey(Generic[T]):
    """
    A key that specifies a PnP property. This is an abstraction over the Windows DEVPROPKEY struct. Can be used as key for `__getitem__` of various winpnp classes.
    """

    _NAMES: ClassVar[dict[tuple[UUID, int], str]] = {}

    category: UUID
    property_id: int
    name: Optional[str] = field(compare=False)
    allowed_types: Optional[dict[int, PnpPropertyType[T]]] = field(compare=False)

    def __init__(
        self,
        category: UUID,
        property_id: int,
        name: Optional[str] = None,
        allowed_types: Optional[Iterable[PnpPropertyType[T]]] = None,
    ) -> None:
        # Using object.__setattr__ because the class is frozen
        object.__setattr__(self, "category", category)
        object.__setattr__(self, "property_id", property_id)
        object.__setattr__(
            self,
            "name",
            name if name is not None else self._NAMES.get((category, property_id)),
        )
        object.__setattr__(
            self,
            "allowed_types",
            (
                {kind.type_id: kind for kind in allowed_types}
                if allowed_types is not None
                else None
            ),
        )

    @staticmethod
    def register(key: "PnpPropertyKey[U]") -> None:
        """
        Registers the name and of the specified `PnpPropertyKey` as the default name for other instances with the same `(category, property_id) pair`.
        """
        if key.name is None:
            raise ValueError(f"Cannot register {repr(key)} because it is unnamed.")

        _id = (key.category, key.property_id)
        if _id in PnpPropertyKey._NAMES:
            raise ValueError(
                f"Cannot register {repr(key)} because its (category, property_id) pair is already registered with name {repr(PnpPropertyKey._NAMES[_id])}"
            )

        PnpPropertyKey._NAMES[_id] = key.name

    @staticmethod
    def register_new(
        category: UUID,
        property_id: int,
        name: str,
        allowed_types: Optional[Iterable[PnpPropertyType[U]]] = None,
    ) -> "PnpPropertyKey[U]":
        """
        Creates a new `PnpPropertyKey`, registers it, and returns it.
        """
        key = PnpPropertyKey(category, property_id, name, allowed_types)
        PnpPropertyKey.register(key)
        return key


@dataclass()
class PnpProperty(Generic[T]):
    """
    Holds the value and type of a PnP property.
    """

    value: T
    kind: PnpPropertyType[T]
