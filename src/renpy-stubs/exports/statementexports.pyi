from renpy.exports.commonexports import renpy_pure as renpy_pure
from typing import Never
from _typeshed import Incomplete

def imagemap(
    ground: Incomplete,
    selected: Incomplete,
    hotspots: Incomplete,
    unselected: Incomplete = None,
    overlays: bool = False,
    style: str = "imagemap",
    mouse: str = "imagemap",
    with_none: Incomplete = None,
    **properties,
) -> Incomplete: ...
def pause(
    delay: Incomplete = None,
    music: Incomplete = None,
    with_none: Incomplete = None,
    hard: bool = False,
    predict: bool = False,
    checkpoint: Incomplete = None,
    modal: Incomplete = None,
) -> Incomplete: ...
def with_statement(trans: Incomplete, always: bool = False, paired: Incomplete = None, clear: bool = True) -> None: ...
def jump(label: Incomplete) -> Never: ...
def call(label: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> None: ...
def return_statement(value: Incomplete = None) -> None: ...
def call_screen(_screen_name: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> None: ...
def execute_default_statement(start: bool = False) -> None: ...
