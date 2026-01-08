import renpy
from renpy.display.behavior import Adjustment as Adjustment, is_selected as is_selected, is_sensitive as is_sensitive
from renpy.display.displayable import Displayable as Displayable
from renpy.display.layout import Container as Container
from renpy.display.screen import ScreenDisplayable as ScreenDisplayable
from renpy.object import Object as Object
from renpy.style import StyleLike as StyleLike
from renpy.types import DisplayableLike as DisplayableLike, Unused as Unused
from typing import Any, Callable, Never, TypeVar

T = TypeVar("T", bound=Displayable)

class Action(renpy.object.Object):
    alt: str | None
    def get_sensitive(self) -> bool: ...
    def get_selected(self) -> bool: ...
    def get_tooltip(self) -> Any | None: ...
    def periodic(self, st: float) -> float | None: ...
    def predict(self) -> None: ...
    def __call__(self) -> Any | None: ...

class BarValue(renpy.object.Object):
    alt: str
    force_step: bool
    def replaces(self, other: object) -> None: ...
    def periodic(self, st: float) -> float | None: ...
    def get_adjustment(self) -> Adjustment: ...
    def get_style(self) -> tuple[str, str]: ...
    def get_tooltip(self) -> Any | None: ...

class Addable:
    style_prefix: str | None
    def add(self, d: Displayable, key: str | None) -> None: ...
    def close(self, d: Displayable | None) -> None: ...
    def get_layer(self) -> str: ...

class Layer(Addable):
    name: str
    def __init__(self, name: str) -> None: ...
    def add(self, d: Displayable, key: str | None) -> None: ...
    def close(self, d: Displayable | None) -> None: ...
    def get_layer(self) -> str: ...
    def __repr__(self) -> str: ...

class Many(Addable):
    displayable: Container
    imagemap: bool | None
    style_prefix: str | None
    def __init__(self, displayable: Container, imagemap: bool | None, style_prefix: str | None) -> None: ...
    def add(self, d: Displayable, key: str | None) -> None: ...
    def close(self, d: Displayable | None) -> None: ...
    def __repr__(self) -> str: ...

class One(Addable):
    displayable: Container
    style_prefix: str | None
    def __init__(self, displayable: Container, style_prefix: str | None) -> None: ...
    def add(self, d: Displayable, key: str | None) -> None: ...
    def close(self, d: Displayable | None) -> None: ...
    def __repr__(self) -> str: ...

class Detached(Addable):
    style_prefix: str | None
    def __init__(self, style_prefix: str | None) -> None: ...
    child: Displayable
    def add(self, d: Displayable, key: str | None) -> None: ...
    def close(self, d: Displayable | None) -> None: ...

class ChildOrFixed(Addable):
    queue: list[Displayable]
    style_prefix: str | None
    def __init__(self, style_prefix: str | None) -> None: ...
    def add(self, d: Displayable, key: str | None) -> None: ...
    def close(self, d: Displayable | None) -> None: ...

stack: list[Addable]
at_stack: list[renpy.display.transform.Transform]
add_tag: str | None
imagemap_stack: list["Imagemap"]

def reset() -> None: ...
def interact(type: str = "misc", roll_forward: Any | None = None, **kwargs) -> Any | None: ...
def tag(name: str | None) -> None: ...
def child_or_fixed() -> None: ...
def remove(d: str | Displayable | None) -> None: ...
def remove_above(d: str | Displayable) -> None: ...
def at(transform: renpy.display.transform.Transform) -> None: ...
def clear() -> None: ...
def detached() -> Detached: ...
def layer(name: str) -> None: ...
def close(d: Displayable | None = None) -> None: ...
def reopen(w: Container, clear: bool) -> None: ...
def context_enter(w: Container) -> None: ...
def context_exit(w: Displayable | None) -> None: ...

NoStylePrefixGiven: Unused

def combine_style(style_prefix: str | None, style_suffix: str) -> renpy.style.StyleCore: ...
def prefixed_style(style_suffix: str) -> renpy.style.StyleCore: ...

screen: ScreenDisplayable | None

class Wrapper[T: Displayable](renpy.object.Object):
    def __reduce__(self) -> str: ...
    name: str
    function: Callable[..., T]
    one: bool
    many: bool
    imagemap: bool
    replaces: bool
    kwargs: dict[str, Any]
    style: str | None
    def __init__(
        self,
        function: Callable[..., T],
        one: bool = False,
        many: bool = False,
        imagemap: bool = False,
        replaces: bool = False,
        style: str | None = None,
        **kwargs,
    ) -> None: ...
    def __call__(self, *args, **kwargs) -> T: ...

def _add(d: DisplayableLike, **kwargs) -> Displayable | renpy.display.transform.Transform: ...

add: Wrapper[Displayable | renpy.display.transform.Transform]

def _implicit_add(d: Displayable) -> Displayable: ...

implicit_add: Wrapper[Displayable]

def _image(im: renpy.display.im.ImageLike, **properties) -> renpy.display.im.ImageBase: ...

image: Wrapper[renpy.display.im.ImageBase]
null: Wrapper[renpy.display.layout.Null]
text: Wrapper[renpy.text.text.Text]
hbox: Wrapper[renpy.display.layout.MultiBox]
vbox: Wrapper[renpy.display.layout.MultiBox]
fixed: Wrapper[renpy.display.layout.MultiBox]
default_fixed: Wrapper[renpy.display.layout.MultiBox]
grid: Wrapper[renpy.display.layout.Grid]
side: Wrapper[renpy.display.layout.Side]

def _sizer(
    maxwidth: float | None = None, maxheight: float | None = None, **properties
) -> renpy.display.layout.Container: ...

sizer: Wrapper[Displayable]
window: Wrapper[renpy.display.layout.Window]
frame: Wrapper[renpy.display.layout.Window]
keymap: Wrapper[renpy.display.behavior.Keymap]
saybehavior: Wrapper[renpy.display.behavior.SayBehavior]
pausebehavior: Wrapper[renpy.display.behavior.PauseBehavior]
soundstopbehavior: Wrapper[renpy.display.behavior.SoundStopBehavior]

def _key(
    key: renpy.display.behavior.KeysymType,
    action: Callable[..., Any | None] | None = None,
    activate_sound: str | None = None,
    capture: bool = True,
) -> renpy.display.behavior.Keymap: ...

key: Wrapper[renpy.display.behavior.Keymap]

class ChoiceActionBase(Action):
    sensitive: bool
    label: str
    value: Any
    location: renpy.ast.NodeName | None
    block_all: bool
    args: tuple[Any, ...] | None
    kwargs: dict[str, Any] | None
    def __init__(
        self,
        label: str,
        value: Any,
        location: renpy.ast.NodeName | None = None,
        block_all: bool | None = None,
        sensitive: bool = True,
        args: tuple[Any, ...] | None = None,
        kwargs: dict[str, Any] | None = None,
    ) -> None: ...
    def get_sensitive(self) -> bool: ...
    def get_selected(self) -> bool: ...
    @property
    def chosen(self) -> dict[tuple[renpy.ast.NodeName, str], bool] | None: ...
    def get_chosen(self) -> bool: ...

class ChoiceReturn(ChoiceActionBase):
    def __call__(self) -> Any: ...

class ChoiceJump(ChoiceActionBase):
    def get_selected(self) -> bool: ...
    def __call__(self) -> Never: ...

class Choice:
    value: Any
    args: tuple[Any, ...] | None
    kwargs: dict[str, Any] | None
    def __init__(self, _value: Any, *args, **kwargs) -> None: ...

def menu(
    menuitems: list[tuple[str, Any | None]],
    style: str = "menu",
    caption_style: str = "menu_caption",
    choice_style: str = "menu_choice",
    choice_chosen_style: str = "menu_choice_chosen",
    choice_button_style: str = "menu_choice_button",
    choice_chosen_button_style: str = "menu_choice_chosen_button",
    location: renpy.ast.NodeName | None = None,
    focus: str | None = None,
    default: bool = False,
    **properties,
) -> None: ...

input: Wrapper[renpy.display.behavior.Input]

def imagemap_compat(
    ground: DisplayableLike,
    selected: DisplayableLike,
    hotspots: list[tuple[float, float, float, float, str | None]],
    unselected: DisplayableLike | None = None,
    style: renpy.style.StyleLike = "imagemap",
    button_style: renpy.style.StyleLike = "hotspot",
    **properties,
) -> None: ...

button: Wrapper[renpy.display.behavior.Button]

def _imagebutton(
    idle_image: DisplayableLike | None = None,
    hover_image: DisplayableLike | None = None,
    insensitive_image: DisplayableLike | None = None,
    activate_image: DisplayableLike | None = None,
    selected_idle_image: DisplayableLike | None = None,
    selected_hover_image: DisplayableLike | None = None,
    selected_insensitive_image: DisplayableLike | None = None,
    selected_activate_image: DisplayableLike | None = None,
    idle: DisplayableLike | None = None,
    hover: DisplayableLike | None = None,
    insensitive: DisplayableLike | None = None,
    selected_idle: DisplayableLike | None = None,
    selected_hover: DisplayableLike | None = None,
    selected_insensitive: DisplayableLike | None = None,
    image_style: Unused | None = None,
    auto: str | None = None,
    **properties,
) -> renpy.display.behavior.ImageButton: ...

imagebutton: Wrapper[renpy.display.behavior.ImageButton]

def _textbutton(
    label: DisplayableLike,
    clicked: renpy.display.behavior.ActionType = None,
    style: StyleLike = None,
    text_style: StyleLike = None,
    substitute: bool = True,
    scope: dict[str, Any] | None = None,
    **kwargs,
) -> renpy.display.behavior.Button: ...

textbutton: Wrapper[renpy.display.behavior.Button]

def _label(
    label: DisplayableLike,
    style: StyleLike = None,
    text_style: StyleLike = None,
    substitute: bool = True,
    scope: dict[str, Any] | None = None,
    **kwargs,
) -> renpy.display.layout.Window: ...

label: Wrapper[renpy.display.layout.Window]
adjustment = renpy.display.behavior.Adjustment

def _bar(*args, **properties) -> renpy.display.behavior.Bar: ...

bar: Wrapper[renpy.display.behavior.Bar]
vbar: Wrapper[renpy.display.behavior.Bar]
slider: Wrapper[renpy.display.behavior.Bar]
vslider: Wrapper[renpy.display.behavior.Bar]
scrollbar: Wrapper[renpy.display.behavior.Bar]
vscrollbar: Wrapper[renpy.display.behavior.Bar]

def _autobar_interpolate(
    range: int | float | None,
    start: int | float,
    end: int | float,
    time: float,
    st: float,
    at: float,
    **properties,
) -> tuple[renpy.display.behavior.Bar, float | None]: ...

autobar_interpolate: renpy.curry.Partial[renpy.display.layout.DynamicDisplayableFunction]

def _autobar(
    range: int | float | None,
    start: int | float,
    end: int | float,
    time: float,
    **properties,
) -> renpy.display.layout.DynamicDisplayable: ...

autobar: Wrapper[renpy.display.layout.DynamicDisplayable]
transform: Wrapper[renpy.display.motion.Transform]
_viewport: Wrapper[renpy.display.viewport.Viewport]
_vpgrid: Wrapper[renpy.display.viewport.VPGrid]
VIEWPORT_SIZE: int

def viewport_common(vpfunc: Wrapper[T], _spacing_to_side: bool, scrollbars: str | None = None, **properties) -> T: ...
def viewport(**properties) -> renpy.display.viewport.Viewport: ...
def vpgrid(**properties) -> renpy.display.viewport.VPGrid: ...

conditional: Wrapper[renpy.display.behavior.Conditional]
timer: Wrapper[renpy.display.behavior.Timer]
drag: Wrapper[renpy.display.dragdrop.Drag]
draggroup: Wrapper[renpy.display.dragdrop.DragGroup]
mousearea: Wrapper[renpy.display.behavior.MouseArea]

class Imagemap:
    alpha: bool
    cache_param: bool
    insensitive: DisplayableLike
    idle: DisplayableLike
    selected_idle: DisplayableLike
    hover: DisplayableLike
    selected_hover: DisplayableLike
    selected_insensitive: DisplayableLike
    cache: renpy.display.imagemap.ImageMapCache
    def __init__(
        self,
        insensitive: DisplayableLike,
        idle: DisplayableLike,
        selected_idle: DisplayableLike,
        hover: DisplayableLike,
        selected_hover: DisplayableLike,
        selected_insensitive: DisplayableLike,
        alpha: bool,
        cache: bool,
    ) -> None: ...
    def reuse(self) -> None: ...

def _imagemap(
    ground: DisplayableLike | None = None,
    hover: DisplayableLike | None = None,
    insensitive: DisplayableLike | None = None,
    idle: DisplayableLike | None = None,
    selected_hover: DisplayableLike | None = None,
    selected_idle: DisplayableLike | None = None,
    selected_insensitive: DisplayableLike | None = None,
    auto: str | None = None,
    alpha: bool = True,
    cache: bool = True,
    style: StyleLike = "imagemap",
    **properties,
) -> renpy.display.layout.MultiBox: ...

imagemap: Wrapper[renpy.display.layout.MultiBox]

def _hotspot(
    spot: tuple[float, float, float, float], style: StyleLike = "hotspot", **properties
) -> renpy.display.behavior.Button: ...

hotspot_with_child: Wrapper[renpy.display.behavior.Button]

def hotspot(*args, **kwargs) -> None: ...
def _hotbar(
    spot: tuple[float, float, float, float],
    adjustment: renpy.display.behavior.Adjustment | None = None,
    range: int | float | None = None,
    value: int | float | None = None,
    **properties,
) -> renpy.display.behavior.Bar: ...

hotbar: Wrapper[renpy.display.behavior.Bar]

def _returns(v: T) -> T: ...

returns: renpy.curry.Partial[Callable[..., Any]]

def _jumps(
    label: renpy.ast.NodeName, transition: str | renpy.display.transition.TransitionFunction | None = None
) -> Never: ...

jumps: renpy.curry.Partial[
    Callable[[renpy.ast.NodeName, str | renpy.display.transition.TransitionFunction | None], Never]
]

def _jumpsoutofcontext(label: str) -> Never: ...

jumpsoutofcontext: renpy.curry.Partial[Callable[[str], Never]]

def callsinnewcontext(*args, **kwargs) -> Any: ...
def invokesinnewcontext(*args, **kwargs) -> Any: ...
def gamemenus(*args) -> Any: ...

on: Wrapper[renpy.display.behavior.OnEvent]

def screen_id(id_: str, d: Displayable) -> None: ...
