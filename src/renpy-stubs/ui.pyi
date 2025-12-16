import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.behavior import Adjustment as Adjustment, is_selected as is_selected, is_sensitive as is_sensitive
from renpy.display.screen import ScreenDisplayable as ScreenDisplayable
from renpy.object import Object as Object

k: Incomplete
v: Incomplete

class Action(renpy.object.Object):
    alt: str | None
    def get_sensitive(self): ...
    def get_selected(self): ...
    def get_tooltip(self) -> None: ...
    def periodic(self, st: float) -> None: ...
    def predict(self) -> None: ...
    def __call__(self) -> None: ...

class BarValue(renpy.object.Object):
    alt: str
    force_step: bool
    def replaces(self, other) -> None: ...
    def periodic(self, st) -> None: ...
    def get_adjustment(self) -> Adjustment: ...
    def get_style(self): ...
    def get_tooltip(self) -> None: ...

class Addable:
    style_prefix: Incomplete
    def add(self, d, key) -> None: ...
    def close(self, d) -> None: ...
    def get_layer(self): ...

class Layer(Addable):
    name: Incomplete
    def __init__(self, name) -> None: ...
    def add(self, d, key) -> None: ...
    def close(self, d) -> None: ...
    def get_layer(self): ...

class Many(Addable):
    displayable: Incomplete
    imagemap: Incomplete
    style_prefix: Incomplete
    def __init__(self, displayable, imagemap, style_prefix) -> None: ...
    def add(self, d, key) -> None: ...
    def close(self, d) -> None: ...

class One(Addable):
    displayable: Incomplete
    style_prefix: Incomplete
    def __init__(self, displayable, style_prefix) -> None: ...
    def add(self, d, key) -> None: ...
    def close(self, d) -> None: ...

class Detached(Addable):
    style_prefix: Incomplete
    def __init__(self, style_prefix) -> None: ...
    child: Incomplete
    def add(self, d, key) -> None: ...
    def close(self, d) -> None: ...

class ChildOrFixed(Addable):
    queue: Incomplete
    style_prefix: Incomplete
    def __init__(self, style_prefix) -> None: ...
    def add(self, d, key) -> None: ...
    def close(self, d) -> None: ...

stack: list[Addable]
at_stack: Incomplete
add_tag: Incomplete
imagemap_stack: Incomplete

def reset() -> None: ...
def interact(type: str = "misc", roll_forward=None, **kwargs): ...
def tag(name) -> None: ...
def child_or_fixed() -> None: ...
def remove(d) -> None: ...
def remove_above(d) -> None: ...
def at(transform) -> None: ...
def clear() -> None: ...
def detached(): ...
def layer(name) -> None: ...
def close(d=None) -> None: ...
def reopen(w, clear) -> None: ...
def context_enter(w) -> None: ...
def context_exit(w) -> None: ...

NoStylePrefixGiven: Incomplete

def combine_style(style_prefix, style_suffix): ...
def prefixed_style(style_suffix): ...

screen: ScreenDisplayable | None

class Wrapper(renpy.object.Object):
    def __reduce__(self): ...
    name: str
    function: Incomplete
    one: Incomplete
    many: Incomplete
    imagemap: Incomplete
    replaces: Incomplete
    kwargs: Incomplete
    style: Incomplete
    def __init__(
        self,
        function,
        one: bool = False,
        many: bool = False,
        imagemap: bool = False,
        replaces: bool = False,
        style=None,
        **kwargs,
    ) -> None: ...
    def __call__(self, *args, **kwargs): ...

add: Incomplete
implicit_add: Incomplete
image: Incomplete
null: Incomplete
text: Incomplete
hbox: Incomplete
vbox: Incomplete
fixed: Incomplete
default_fixed: Incomplete
grid: Incomplete
side: Incomplete
sizer: Incomplete
window: Incomplete
frame: Incomplete
keymap: Incomplete
saybehavior: Incomplete
pausebehavior: Incomplete
soundstopbehavior: Incomplete
key: Incomplete

class ChoiceActionBase(Action):
    sensitive: bool
    label: Incomplete
    value: Incomplete
    location: Incomplete
    block_all: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(
        self, label, value, location=None, block_all=None, sensitive: bool = True, args=None, kwargs=None
    ) -> None: ...
    def get_sensitive(self): ...
    def get_selected(self): ...
    @property
    def chosen(self): ...
    def get_chosen(self): ...

class ChoiceReturn(ChoiceActionBase):
    def __call__(self): ...

class ChoiceJump(ChoiceActionBase):
    def get_selected(self): ...
    def __call__(self) -> None: ...

class Choice:
    value: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, _value, *args, **kwargs) -> None: ...

def menu(
    menuitems,
    style: str = "menu",
    caption_style: str = "menu_caption",
    choice_style: str = "menu_choice",
    choice_chosen_style: str = "menu_choice_chosen",
    choice_button_style: str = "menu_choice_button",
    choice_chosen_button_style: str = "menu_choice_chosen_button",
    location=None,
    focus=None,
    default: bool = False,
    **properties,
) -> None: ...

input: Incomplete

def imagemap_compat(
    ground, selected, hotspots, unselected=None, style: str = "imagemap", button_style: str = "hotspot", **properties
) -> None: ...

button: Incomplete
imagebutton: Incomplete
textbutton: Incomplete
label: Incomplete
adjustment = renpy.display.behavior.Adjustment
bar: Incomplete
vbar: Incomplete
slider: Incomplete
vslider: Incomplete
scrollbar: Incomplete
vscrollbar: Incomplete
autobar_interpolate: Incomplete
autobar: Incomplete
transform: Incomplete
VIEWPORT_SIZE: int

def viewport_common(vpfunc, _spacing_to_side, scrollbars=None, **properties): ...
def viewport(**properties): ...
def vpgrid(**properties): ...

conditional: Incomplete
timer: Incomplete
drag: Incomplete
draggroup: Incomplete
mousearea: Incomplete

class Imagemap:
    alpha: bool
    cache_param: bool
    insensitive: Incomplete
    idle: Incomplete
    selected_idle: Incomplete
    hover: Incomplete
    selected_hover: Incomplete
    selected_insensitive: Incomplete
    cache: Incomplete
    def __init__(
        self, insensitive, idle, selected_idle, hover, selected_hover, selected_insensitive, alpha, cache
    ) -> None: ...
    def reuse(self) -> None: ...

imagemap: Incomplete
hotspot_with_child: Incomplete

def hotspot(*args, **kwargs) -> None: ...

hotbar: Incomplete
returns: Incomplete
jumps: Incomplete
jumpsoutofcontext: Incomplete

def callsinnewcontext(*args, **kwargs): ...
def invokesinnewcontext(*args, **kwargs): ...
def gamemenus(*args): ...

on: Incomplete

def screen_id(id_, d) -> None: ...
