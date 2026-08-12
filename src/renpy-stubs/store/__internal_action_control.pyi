from _typeshed import Incomplete
from typing import Any, Literal

import renpy
from renpy.ui import Action
from renpy.store import DictEquality

class NullAction(Action, DictEquality):
    def __call__(self) -> None: ...

class Return(Action, DictEquality):
    value: Any
    def __init__(self, value: Any = None) -> None: ...
    def __call__(self) -> Literal[True] | Any | None: ...

class Jump(Action, DictEquality):
    label: renpy.ast.NodeName
    def __init__(self, label: renpy.ast.NodeName) -> None: ...
    def __call__(self) -> None: ...

class Call(Action, DictEquality):
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    label: renpy.ast.NodeName
    def __init__(self, label: renpy.ast.NodeName, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def __call__(self) -> None: ...

class Show(Action, DictEquality):
    args: tuple[Any, ...]
    screen: str | tuple[str, ...]
    transition: Incomplete | None
    kwargs: dict[str, Any]
    def __init__(
        self,
        screen: str | tuple[str, ...],
        transition: Incomplete | None = None,
        *args: Incomplete,
        **kwargs: Incomplete,
    ) -> None: ...
    def predict(self) -> None: ...
    def __call__(self) -> None: ...
    def get_selected(self) -> bool: ...

class ToggleScreen(Action, DictEquality):
    args: tuple[Any, ...]
    screen: str | tuple[str, ...]
    transition: Incomplete | None
    kwargs: dict[str, Any]
    def __init__(
        self,
        screen: str | tuple[str, ...],
        transition: Incomplete | None = None,
        *args: Incomplete,
        **kwargs: Incomplete,
    ) -> None: ...
    def predict(self) -> None: ...
    def __call__(self) -> None: ...
    def get_selected(self) -> bool: ...

@renpy.exports.pure
def ShowTransient(
    screen: str | tuple[str, ...], transition: Incomplete | None = None, *args: Incomplete, **kwargs: Incomplete
) -> Incomplete: ...

class Hide(Action, DictEquality):
    _layer: str | None
    immediately: bool
    screen: str | None
    transition: Incomplete | None
    def __init__(
        self,
        screen: str | None = None,
        transition: Incomplete | None = None,
        _layer: str | None = None,
        immediately: bool = False,
    ) -> None: ...
    def __call__(self) -> None: ...
