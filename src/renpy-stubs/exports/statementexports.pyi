from typing import Any, NoReturn

import renpy
from renpy.display.transition import TransitionFunction as TransitionFunction
from renpy.exports.commonexports import renpy_pure as renpy_pure
from renpy.types import DisplayableLike as DisplayableLike

def imagemap(
    ground: DisplayableLike,
    selected: DisplayableLike,
    hotspots: list[tuple[float, float, float, float, str | None]],
    unselected: DisplayableLike | None = None,
    overlays: bool = False,
    style: str = "imagemap",
    mouse: str = "imagemap",
    with_none: bool | None = None,
    **properties,
) -> Any | None: ...
def pause(
    delay: float | None = None,
    music: float | None = None,
    with_none: bool | None = None,
    hard: bool = False,
    predict: bool = False,
    checkpoint: bool | None = None,
    modal: bool | None = None,
) -> Any | None: ...
def with_statement(
    trans: TransitionFunction | dict[str | None, TransitionFunction] | None,
    always: bool = False,
    paired: TransitionFunction | None = None,
    clear: bool = True,
) -> Any | None: ...
def jump(label: renpy.ast.NodeName) -> NoReturn: ...
def call(label: renpy.ast.NodeName, *args: Any, **kwargs: Any) -> NoReturn: ...
def return_statement(value: Any | None = None) -> None: ...
def call_screen(_screen_name: str | tuple[str, ...], *args: Any, **kwargs: Any) -> Any | None: ...
def execute_default_statement(start: bool = False) -> None: ...

_ran_after_init_callbacks: bool

def get_statement_name() -> str: ...

class StatementInfo:
    filename: str
    linenumber: int
    tlid: str | None
    def __init__(self, node, tlid) -> None: ...

def get_statement_info() -> StatementInfo: ...
