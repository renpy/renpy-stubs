from collections.abc import Iterable, Mapping, Sequence
from typing import Any, Final, Literal, TypedDict, Unpack

import renpy
from renpy.object import Object as Object

class _ReplaceKwargs(TypedDict, total=False):
    name: str
    kind: int
    default: Any

class Parameter:
    POSITIONAL_ONLY: Literal[0]
    POSITIONAL_OR_KEYWORD: Literal[1]
    VAR_POSITIONAL: Literal[2]
    KEYWORD_ONLY: Literal[3]
    VAR_KEYWORD: Literal[4]
    empty: Final[None]
    name: str
    kind: int
    default: str | None
    def __init__(self, name: str, kind: int, *, default: str | None = ...) -> None: ...
    @property
    def has_default(self) -> bool: ...
    def default_value(self, locals: dict[str, Any] | None = None, globals: dict[str, Any] | None = None) -> Any: ...
    def replace(self, **kwargs: Unpack[_ReplaceKwargs]) -> Parameter: ...
    def __eq__(self, other: object) -> bool: ...

class ValuedParameter(Parameter):
    class empty: ...

    def __init__(self, name: str, kind: int, *, default: Any = ...) -> None: ...
    def default_value(self, *args: Any, **kwargs: Any) -> Any: ...

class Signature:
    parameters: dict[str, Parameter]
    def __init__(self, parameters: Iterable[Parameter] | None = None) -> None: ...
    @staticmethod
    def legacy_params(
        parameters: Iterable[tuple[str, str | None]],
        positional: Iterable[str],
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
        kwargs: Mapping[str, Any],
        ignore_errors: bool = False,
        partial: bool = False,
        apply_defaults: bool = True,
    ) -> dict[str, Any]: ...
    def __eq__(self, other: object) -> bool: ...

ParameterInfo = Signature

def apply_arguments(
    parameters: Signature | None, args: Iterable[Any], kwargs: Mapping[str, Any], ignore_errors: bool = False
) -> dict[str, Any]: ...

class ArgumentInfo(renpy.object.Object):
    __version__: int
    arguments: Sequence[tuple[str | None, str]]
    starred_indexes: Iterable[int]
    doublestarred_indexes: Iterable[int]
    def after_upgrade(self, version: int) -> None: ...
    def __init__(
        self,
        arguments: Sequence[tuple[str | None, str]],
        starred_indexes: Iterable[int] | None = None,
        doublestarred_indexes: Iterable[int] | None = None,
    ) -> None: ...
    def evaluate(
        self, scope: dict[str, Any] | None = None
    ) -> tuple[tuple[Any, ...], renpy.revertable.RevertableDict[str, Any]]: ...
    def get_code(self) -> str: ...
    __str__ = get_code

EMPTY_PARAMETERS: Signature
EMPTY_ARGUMENTS: ArgumentInfo
