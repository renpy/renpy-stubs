import renpy
from renpy.display.displayable import Displayable as Displayable
from renpy.display.layout import Container as Container
from renpy.display.motion import Transform as Transform
from renpy.object import Object as Object
from renpy.pygame.event import EventType
from typing import Any, Callable, Self
from _typeshed import Incomplete as Incomplete

profile_log: renpy.log.LogFile
profile: dict[tuple[str, ...], ScreenProfile]

class ScreenProfile(renpy.object.Object):
    predict: bool
    show: bool
    update: bool
    request: bool
    time: bool
    debug: bool
    const: bool
    def __init__(
        self,
        name: str | None,
        predict: bool = False,
        show: bool = False,
        update: bool = False,
        request: bool = False,
        time: bool = False,
        debug: bool = False,
        const: bool = False,
    ) -> None: ...

def get_profile(name: str | tuple[str, ...]) -> ScreenProfile: ...

predict_cache: dict[Screen, list[ScreenCache]]

class ScreenCache:
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    cache: dict[int, dict[str, Any]]
    def __init__(
        self, screen: Screen, args: tuple[Any, ...], kwargs: dict[str, Any], cache: dict[int, dict[str, Any]]
    ) -> None: ...

cache_put = ScreenCache

def cache_get(screen: Screen, args: tuple[Any, ...], kwargs: dict[str, Any]) -> dict[int, dict[str, Any]]: ...

class ScreenNotFound(LookupError):
    name: str
    def __init__(self, name: str) -> None: ...
    def get_suggestion(self) -> str | None: ...

class Screen(renpy.object.Object):
    sensitive: str
    roll_forward: bool | None
    docstring: str | None
    name: str
    function: renpy.sl2.slast.SLScreen | Callable[..., None]
    ast: renpy.sl2.slast.SLScreen | None
    modal: str
    zorder: str
    tag: str
    predict: bool | None
    parameters: bool
    location: tuple[str, int] | None
    layer: str
    def __init__(
        self,
        name: str | tuple[str, ...],
        function: renpy.sl2.slast.SLScreen | Callable[..., None],
        modal: str = "False",
        zorder: str = "0",
        tag: str | None = None,
        predict: bool | None = None,
        variant: str | None | list[str | None] = None,
        parameters: bool = False,
        location: tuple[str, int] | None = None,
        layer: str = "screens",
        sensitive: str = "True",
        roll_forward: bool | None = None,
        docstring: str | None = None,
    ) -> None: ...

PREDICT: int
SHOW: int
UPDATE: int
HIDE: int
OLD: int
phase_name: list[str]

class ScreenDisplayable(renpy.display.layout.Container):
    nosave: list[str]
    noreach: list[str]
    restarting: bool
    hiding: bool
    transient: bool
    screen: Screen | None
    child: renpy.display.layout.MultiBox | None
    children: list[Displayable]
    transforms: dict[str, Transform]
    widgets: dict[str, Displayable] | None
    base_widgets: dict[str, Displayable] | None
    old_widgets: dict[str, Displayable] | None
    old_transforms: dict[str, Transform] | None
    old_transfers: bool
    hidden_widgets: dict[str, Displayable]
    cache: dict[int, dict[str, Any]]
    phase: int
    use_cache: dict[int, dict[str, Any]]
    miss_cache: dict[int, dict[str, Any]]
    copied_from: "ScreenDisplayable | None"
    profile: ScreenProfile | None
    def after_setstate(self) -> None: ...
    properties: dict[str, Any]
    screen_name: tuple[str, ...]
    _location: tuple[str, int] | None
    tag: str | None
    layer: str | None
    scope: renpy.revertable.RevertableDict
    widget_properties: dict[str, Any]
    current_transform_event: str | None
    modal: bool
    zorder: int
    def __init__(
        self,
        screen: Screen | None,
        tag: str | None,
        layer: str | None,
        widget_properties: dict[str, Any] = {},
        scope: dict[str, Any] = {},
        transient: bool = False,
        **properties,
    ) -> None: ...
    @property
    def name(self) -> Incomplete: ...
    def _repr_info(self) -> Incomplete: ...
    def visit(self) -> list[Displayable | None]: ...
    def visit_all(self, callback: Callable[[Displayable], None], seen: set[int] | None = None) -> None: ...
    def per_interact(self) -> None: ...
    def set_transform_event(self, event: Incomplete) -> None: ...
    def find_focusable(self, callback: Incomplete, focus_name: Incomplete) -> None: ...
    def copy(self) -> Incomplete: ...
    def _handles_event(self, event: str) -> bool: ...
    def _hide(self, st: Incomplete, at: Incomplete, kind: Incomplete) -> Incomplete: ...
    def _in_current_store(self) -> Self: ...
    def update(self) -> Incomplete: ...
    def render(self, w, h, st, at) -> Incomplete: ...
    def get_placement(self) -> Incomplete: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def get_phase_name(self) -> Incomplete: ...
    def _tts(self, raw: bool) -> str: ...

_current_screen: ScreenDisplayable | None
current_screen_stack: list[ScreenDisplayable]

def push_current_screen(screen: ScreenDisplayable) -> None: ...
def pop_current_screen() -> None: ...

screens: dict[tuple[str, str | None], Screen]
screens_by_name: dict[str, dict[str | None, Screen]]
updated_screens: set[ScreenDisplayable]

def get_screen_variant(name: str, candidates: list[str | None] | None = None) -> Screen | None: ...
def get_all_screen_variants(name: Incomplete) -> Incomplete: ...

analyzed: bool
prepared: bool
sorted_screens: list[str]
screens_at_sort: dict[tuple[str, str | None], Screen]
use_cycle: list[str]

def sort_screens() -> list[str]: ...
def sorted_variants() -> list[Screen]: ...
def analyze_screens() -> None: ...
def prepare_screens() -> None: ...
def define_screen(*args, **kwargs) -> None: ...
def get_screen_layer(name: str | tuple[str, ...]) -> str: ...
def get_screen_docstring(name: str, variant: str | None = None) -> str | None: ...
def get_screen(
    name: str | tuple[str, ...], layer: str | None = None, tag_only: bool = False
) -> ScreenDisplayable | None: ...
def get_screen_variable(name: str, screen: str | tuple[str, ...] | None = None, layer: str | None = None) -> Any: ...
def set_screen_variable(
    name: str, value: Any, screen: str | tuple[str, ...] | None = None, layer: str | None = None
) -> None: ...
def has_screen(name: str | tuple[str, ...]) -> bool: ...
def get_screen_roll_forward(screen_name: str | tuple[str, ...]) -> bool | None: ...
def show_screen(_screen_name: str | tuple[str, ...], *_args, **kwargs) -> None: ...
def predict_screen(_screen_name: str | tuple[str, ...], *_args, **kwargs) -> None: ...
def hide_screen(tag: str, layer: str | None = None, immediately: bool = False) -> None: ...
def use_screen(_screen_name: str | tuple[str, ...], *_args, **kwargs) -> None: ...
def current_screen() -> ScreenDisplayable | None: ...
def get_displayable(
    screen: str | tuple[str, ...] | ScreenDisplayable | None, id: str, layer: str | None = None, base: bool = False
) -> Displayable | None: ...

get_widget = get_displayable

def get_displayable_properties(
    id: str, screen: str | tuple[str, ...] | None = None, layer: str | None = None
) -> dict[str, Any]: ...

get_widget_properties = get_displayable_properties

def before_restart() -> None: ...
def show_overlay_screens(suppress_overlay: bool) -> None: ...
def per_frame() -> None: ...
