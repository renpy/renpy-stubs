from collections.abc import Callable
from typing import Any

from renpy.character import ADVCharacter
from renpy.rollback import NoRollback
from renpy.store import JSONDB
from renpy.ui import Action

active: bool
shown: NoRollback
db_filename: str
cols: int
rows: int
default_area: tuple[int, int, int, int]
area_property: str
properties: dict[str, list[Any]]
properties_order: list[str]
properties_callback: Callable[[str], list[str]] | None
expand_area: dict[str | None, tuple[int, int, int, int]]
db: JSONDB | None
frame: Any | None
thoughtframe: Any | None
layer: str
retain_layer: str
clear_retain_statements: list[str]

class ToggleShown(Action):
    def __call__(self) -> None: ...
    def get_selected(self) -> bool: ...

def scene_callback(layer: str) -> None: ...
def character_callback(event: str, interact: bool = True, **kwargs: Any) -> None: ...

class BubbleCharacter(ADVCharacter):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def bubble_default_properties(self, image_tag: str) -> dict[str, Any]: ...
    def expand_area(
        self, area: tuple[int, int, int, int] | list[int], properties_key: str
    ) -> tuple[int, int, int, int] | list[int]: ...
    def do_add(self, who: str | None, what: str, multiple: bool = False) -> None: ...
    def do_show(
        self,
        who: str | None,
        what: str,
        multiple: tuple[int, int] | None = None,
        retain: str | bool | None = None,
        extra_properties: dict[str, Any] | None = None,
    ) -> tuple[str, str, str] | None: ...

class CycleBubbleProperty(Action):
    image_tag: str
    tlid: str
    def __init__(self, image_tag: str, tlid: str) -> None: ...
    def get_selected(self) -> bool: ...
    def __call__(self) -> None: ...
    def alternate(self) -> None: ...

class ToggleClearRetain(Action):
    tlid: str
    def __init__(self, tlid: str) -> None: ...
    def get_selected(self) -> bool: ...
    def __call__(self) -> None: ...
    def alternate(self) -> None: ...

class SetWindowArea(Action):
    image_tag: str
    tlid: str
    def __init__(self, image_tag: str, tlid: str) -> None: ...
    def __call__(self) -> None: ...
    def get_selected(self) -> bool: ...
    def finished(self, rect: tuple[int, int, int, int] | list[int]) -> None: ...
    def alternate(self) -> None: ...

def GetCurrentDialogue() -> list[tuple[str, list[tuple[str, Action]]]]: ...

character: BubbleCharacter

def statement_callback(statement: str) -> None: ...

tag_properties: dict[str, dict[str, Any]]
current_dialogue: list[tuple[str, str]]
