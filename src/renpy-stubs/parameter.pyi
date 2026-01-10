import renpy
from _typeshed import Incomplete as Incomplete
from renpy.object import Object as Object
from typing import Any, Literal, Sequence, Iterable

class Parameter:
    __slots__: str | tuple[str, ...]
    POSITIONAL_ONLY: Literal[0]
    POSITIONAL_OR_KEYWORD: Literal[1]
    VAR_POSITIONAL: Literal[2]
    KEYWORD_ONLY: Literal[3]
    VAR_KEYWORD: Literal[4]
    empty: None
    name: str
    kind: int
    default: Incomplete | None
    def __init__(self, name: str, kind: int, *, default: Incomplete | None = ...) -> None: ...
    @property
    def has_default(self) -> bool: ...
    def default_value(self, locals: dict[str, Any] | None = None, globals: dict[str, Any] | None = None) -> Any: ...
    def replace(self, **kwargs) -> Parameter: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...

class ValuedParameter(Parameter):
    __slots__: str | tuple[str, ...]
    class empty: ...

    def __init__(self, name: str, kind: int, *, default: Incomplete | None = ...) -> None: ...
    def default_value(self, *args, **kwargs) -> Incomplete | None: ...
    def __str__(self) -> str: ...

class Signature:
    __slots__: str | tuple[str, ...]
    parameters: dict[str, Parameter]
    def __init__(self, parameters: list[Parameter] | None = None) -> None: ...
    @staticmethod
    def legacy_params(
        parameters: list[tuple[str, Any]],
        positional: list[str],
        extrapos: str | None,
        extrakw: str | None,
        last_posonly: str | None = None,
        first_kwonly: str | None = None,
    ) -> list[Parameter]: ...
    def __setstate__(self, state: dict[str, Any] | tuple[dict[str, Any] | None, dict[str, Any] | None]) -> None: ...
    def apply_defaults(self, mapp: dict[str, Any], scope: dict[str, Any] | None = None) -> None: ...
    def with_pos_only_as_pos_or_kw(self) -> Signature: ...
    def apply(
        self,
        args: Iterable[Any],
        kwargs: dict[str, Any],
        ignore_errors: bool = False,
        partial: bool = False,
        apply_defaults: bool = True,
    ) -> dict[str, Any]: ...
    def __eq__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

ParameterInfo = Signature

def apply_arguments(
    parameters: Signature | None, args: tuple[Any, ...], kwargs: dict[str, Any], ignore_errors: bool = False
) -> dict[str, Any]: ...

class ArgumentInfo(renpy.object.Object):
    __version__: int
    starred_indexes: set[int]
    doublestarred_indexes: set[int]
    def after_upgrade(self, version: int) -> None: ...
    arguments: Sequence[tuple[str | None, str]]
    def __init__(
        self,
        arguments: Sequence[tuple[str | None, str]],
        starred_indexes: set[int] | None = None,
        doublestarred_indexes: set[int] | None = None,
    ) -> None: ...
    def evaluate(
        self, scope: dict[str, Any] | None = None
    ) -> tuple[tuple[Any, ...], renpy.revertable.RevertableDict[str, Any]]: ...
    def get_code(self) -> str: ...
    __str__ = get_code
    def __repr__(self) -> str: ...

EMPTY_PARAMETERS: Signature
EMPTY_ARGUMENTS: ArgumentInfo
