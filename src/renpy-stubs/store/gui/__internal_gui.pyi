from _typeshed import Incomplete
from typing import Literal, Any, Callable, Iterable

from renpy.display.layout import Null
from renpy.ui import Action
from store import DictEquality

_null: Null

def init(width: int, height: int, fov: int = 75) -> None: ...

variant_functions: list[tuple[str | Iterable[str], Callable[[], None]]]

def variant(f: Callable[[], None], variant: str | Iterable[str] | None = None) -> Callable[[], None]: ...
def _apply_rebuild() -> None: ...
def rebuild() -> None: ...

not_set: Incomplete
preferences_with_default: set[str]

def preference(name: str, default: Any | Incomplete = ...) -> Any: ...

class SetPreference(Action, DictEquality):
    name: str
    value: Any
    rebuild: bool
    def __init__(self, name: str, value: Any, rebuild: bool = True) -> None: ...
    def __call__(self) -> None: ...
    def get_selected(self) -> bool: ...

class TogglePreference(Action, DictEquality):
    name: str
    a: Any
    b: Any
    rebuild: bool
    def __init__(self, name: Incomplete, a: Incomplete, b: Incomplete, rebuild: bool = True) -> None: ...
    def __call__(self) -> None: ...
    def get_selected(self) -> bool: ...

button_image_extension: str

def button_properties(kind: str) -> dict[str, Any]: ...
def text_properties(kind: str | None = None, accent: bool = False) -> dict[str, Any]: ...

button_text_properties = text_properties
ARE_YOU_SURE: str
DELETE_SAVE: str
OVERWRITE_SAVE: str
LOADING: str
QUIT: str
MAIN_MENU: str
CONTINUE: str
END_REPLAY: str
SLOW_SKIP: str
FAST_SKIP_SEEN: str
FAST_SKIP_UNSEEN: str
UNKNOWN_TOKEN: str
TRUST_TOKEN: str
_skip_backup: bool

def _gui_images() -> Literal[False] | None: ...
