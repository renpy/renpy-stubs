import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.displayable import Displayable as Displayable
from renpy.display.layout import Container as Container, Null as Null, Window as Window
from renpy.display.render import Render as Render, render as render
from renpy.object import Object as Object
from renpy.pygame.event import EventType as EventType
from renpy.python import AlwaysRollback as AlwaysRollback
from renpy.style import StyleLike
from renpy.text.text import Text as Text
from renpy.types import DisplayableLike as DisplayableLike
from typing import Any, Callable, Sequence, Literal, Self

type KeysymType = str | list[str] | tuple[str, ...]
type ActionType = renpy.ui.Action | Callable[..., Any] | Sequence[Callable[..., Any], ...] | None

def compile_event(key: KeysymType | None, keydown: bool) -> str: ...

event_cache: dict[str | tuple[str, ...], Callable[..., bool]]
keyup_cache: dict[str | tuple[str, ...], Callable[..., bool]]

def init_keymap() -> None: ...
def clear_keymap_cache() -> None: ...
def queue_event(name: KeysymType, up: bool = False, **kwargs) -> None: ...
def map_event(ev: EventType, keysym: KeysymType) -> bool: ...
def map_keyup(ev: EventType, keysym: KeysymType) -> bool: ...
def skipping(ev: EventType) -> None: ...
def inspector(ev: EventType) -> bool: ...
def predict_action(var: ActionType) -> None: ...
def run(action: ActionType | None, *args, **kwargs) -> Any: ...
def run_unhovered(var: ActionType) -> None: ...
def run_periodic(var: ActionType, st: float) -> Any: ...
def get_tooltip(action: ActionType) -> Any | None: ...
def is_selected(action: ActionType) -> bool: ...
def is_sensitive(action: ActionType) -> bool: ...
def alt(clicked: ActionType) -> str | None: ...

class Keymap(renpy.display.layout.Null):
    capture: bool
    _box_skip: bool
    keymap: dict[str, Callable[..., Any | None] | None]
    def __init__(
        self,
        replaces: Self | None = None,
        activate_sound: str | None = None,
        capture: bool = True,
        **keymap: Callable[..., Any | None] | None,
    ) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def predict_one_action(self) -> None: ...

class RollForward(renpy.display.layout.Null):
    value: Incomplete
    def __init__(self, value: Any, **properties) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class PauseBehavior(renpy.display.layout.Null):
    voice: bool
    modal: bool
    self_voice: bool
    delay: float
    result: Incomplete
    self_voicing: Incomplete
    def __init__(
        self,
        delay: float,
        result: bool = False,
        voice: bool = False,
        self_voicing: bool = False,
        modal: bool | None = None,
        **properties,
    ) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class PredictPauseBehavior(renpy.display.layout.Null):
    def __init__(self, **properties) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class SoundStopBehavior(renpy.display.layout.Null):
    channel: Incomplete
    result: Incomplete
    def __init__(self, channel: str, result: bool = False, **properties) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class SayBehavior(renpy.display.layout.Null):
    focusable: bool
    text_tuple: tuple[renpy.text.text.Text, ...] | None
    dismiss_unfocused: Sequence[str]
    dialogue_pause: float | None
    afm_length: Incomplete
    dismiss: Incomplete
    allow_dismiss: Incomplete
    def __init__(
        self,
        default: bool = True,
        afm: list | None = None,
        dismiss: str | list[str] | tuple[str] = ["dismiss"],
        allow_dismiss: Callable[[], bool] | None = None,
        dismiss_unfocused: str | list[str] | tuple[str] = ["dismiss_unfocused"],
        dialogue_pause: float | None = None,
        **properties,
    ) -> None: ...
    def _tts_all(self, raw: bool) -> str: ...
    def set_text(self, *args: renpy.text.text.Text) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class DismissBehavior(renpy.display.displayable.Displayable):
    focusable: bool
    keysym: KeysymType
    action: Incomplete
    modal: Incomplete
    def __init__(
        self, action: ActionType = None, modal: bool = True, keysym: KeysymType = "dismiss", **properties
    ) -> None: ...
    def _tts(self, raw: bool) -> str: ...
    def _tts_all(self, raw: bool) -> str: ...
    def find_focusable(self, callback: Callable[[Displayable | None, str], None], focus_name: str) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

KEY_EVENTS: tuple[int, ...]

class Button(renpy.display.layout.Window):
    _store_transform_event: bool
    keymap: dict[str, ActionType]
    action: ActionType
    alternate: ActionType
    longpress_start: float | None
    longpress_x: float | None
    longpress_y: float | None
    role_parameter: str | None
    keysym: KeysymType | None
    alternate_keysym: KeysymType | None
    locked: bool
    selected: Incomplete
    sensitive: Incomplete
    clicked: Incomplete
    hovered: Incomplete
    unhovered: Incomplete
    focusable: bool
    time_policy_data: Incomplete
    _duplicatable: bool
    def __init__(
        self,
        child: DisplayableLike | None = None,
        style: StyleLike = "button",
        clicked: ActionType = None,
        hovered: ActionType = None,
        unhovered: ActionType = None,
        action: ActionType = None,
        role: str | None = None,
        time_policy: Incomplete = None,
        keymap: dict[str, ActionType] = {},
        alternate: ActionType = None,
        selected: bool | None = None,
        sensitive: bool | None = None,
        keysym: KeysymType | None = None,
        alternate_keysym: KeysymType | None = None,
        **properties,
    ) -> None: ...
    def _get_tooltip(self) -> Incomplete: ...
    def _in_current_store(self) -> Self: ...
    def predict_one_action(self) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def focus(self, default: bool = False) -> Any | None: ...
    def unfocus(self, default: bool = False) -> None: ...
    def is_selected(self) -> bool: ...
    def is_sensitive(self) -> bool: ...
    role: Incomplete
    def per_interact(self) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def set_style_prefix(self, prefix: str, root: bool) -> None: ...
    def _tts(self, raw: bool) -> str: ...
    def _tts_all(self, raw: bool) -> str: ...

def TextButton(
    text: Incomplete,
    style: StyleLike = "button",
    text_style: StyleLike = "button_text",
    clicked: ActionType = None,
    **properties,
) -> Button: ...

class ImageButton(Button):
    imagebutton_child: Displayable | None
    imagebutton_raw_child: Displayable | None
    state_children: Incomplete
    def __init__(
        self,
        idle_image: DisplayableLike,
        hover_image: DisplayableLike | None = None,
        insensitive_image: DisplayableLike | None = None,
        activate_image: DisplayableLike | None = None,
        selected_idle_image: DisplayableLike | None = None,
        selected_hover_image: DisplayableLike | None = None,
        selected_insensitive_image: DisplayableLike | None = None,
        selected_activate_image: DisplayableLike | None = None,
        style: StyleLike = "image_button",
        clicked: ActionType = None,
        hovered: ActionType = None,
        **properties,
    ) -> None: ...
    def visit(self) -> list[Displayable]: ...
    def get_child(self) -> Displayable | None: ...

class HoveredProxy:
    a: Incomplete
    b: Incomplete
    def __init__(self, a: Callable[[], None], b: Callable[[], Any] | None) -> None: ...
    def __call__(self) -> Any: ...

current_input_value: Incomplete | None
input_value_active: bool
default_input_value: Incomplete | None
input_values: list[Incomplete]
inputs: list[Input]

def input_pre_per_interact() -> None: ...
def input_post_per_interact() -> None: ...

class CaretBlink(renpy.display.displayable.Displayable):
    caret: Incomplete
    caret_blink: Incomplete
    st: float
    st_base: float
    def __init__(self, caret: DisplayableLike, caret_blink: float, **properties) -> None: ...
    def get_placement(self) -> Incomplete: ...
    def visit(self) -> list[Displayable]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class Input(renpy.text.text.Text):
    changed: Callable[[str], None] | None
    prefix: str
    suffix: str
    caret_pos: int
    old_caret_pos: int
    pixel_width: float | None
    default: str
    edit_text: str
    value: Incomplete
    shown: bool
    multiline: bool
    action: ActionType
    arrowkeys: bool
    st: float
    content: str
    length: Incomplete
    allow: Incomplete
    exclude: Incomplete
    copypaste: Incomplete
    editable: Incomplete
    caret: Incomplete
    def __init__(
        self,
        default: str | None = "",
        length: int | None = None,
        style: StyleLike = "input",
        allow: str | None = None,
        exclude: str | None = None,
        prefix: str = "",
        suffix: str = "",
        changed: Callable[[str], None] | None = None,
        button: Button | None = None,
        replaces: Self | None = None,
        editable: bool = True,
        pixel_width: float | None = None,
        value: Incomplete | None = None,
        copypaste: bool = False,
        caret_blink: float | None = None,
        multiline: bool = False,
        action: ActionType = None,
        arrowkeys: bool = True,
        **properties,
    ) -> None: ...
    def update_text(self, new_content: str, editable: bool, check_size: bool = False) -> None: ...
    def set_style_prefix(self, prefix: str, root: bool) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def per_interact(self) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def get_caret_above_below_pos(self) -> tuple[int | None, int | None]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

adj_registered: dict["Adjustment", list["Displayable"]]

class Adjustment(renpy.object.Object):
    force_step: Literal["release"] | bool
    animation_amplitude: float | None
    animation_target: float | None
    animation_start: float | None
    animation_delay: float | None
    animation_warper: Callable[[float], float | None] | None
    restart_interaction_at_limit: bool
    restart_interaction_at_range: bool
    raw_changed: Callable[[Adjustment, float], None] | None
    _range: Incomplete
    _value: Incomplete
    _page: Incomplete
    _step: Incomplete
    changed: Incomplete
    adjustable: Incomplete
    ranged: Incomplete
    def __init__(
        self,
        range: int | float = 1,
        value: int | float = 0,
        step: int | float | None = None,
        page: int | float | None = None,
        changed: Callable[[int | float], Any] | None = None,
        adjustable: bool | None = None,
        ranged: Callable[[Adjustment], None] | None = None,
        force_step: bool = False,
        raw_changed: Callable[[Adjustment, int | float], None] | None = None,
    ) -> None: ...
    range: Incomplete
    value: Incomplete
    def viewport_replaces(self, replaces: Adjustment) -> None: ...
    def round_value(self, value: int | float, release: bool) -> int | float: ...
    def get_value(self) -> int | float: ...
    def set_value(self, v: int | float) -> None: ...
    def get_range(self) -> int | float: ...
    def set_range(self, v: int | float) -> None: ...
    def get_page(self) -> int | float: ...
    def set_page(self, v: int | float) -> None: ...
    page: Incomplete
    def get_step(self) -> int | float: ...
    def set_step(self, v: int | float) -> None: ...
    step: Incomplete
    def register(self, d: Displayable) -> None: ...
    def change(self, value: int | float, end_animation: bool = True) -> Incomplete: ...
    def update(self) -> None: ...
    def inertia_warper(self, done: float) -> float: ...
    def animate(self, amplitude: float, delay: float, warper: Callable[[float], float]) -> None: ...
    def inertia(self, amplitude: float, time_constant: float, st: float) -> None: ...
    def end_animation(self, instantly: bool = False) -> None: ...
    def periodic(self, st: float) -> float | None: ...

class Bar(renpy.display.displayable.Displayable):
    _store_transform_event: bool
    @property
    def _draggable(self) -> Incomplete: ...
    __version__: int
    adjustment: Incomplete
    value: Incomplete
    def after_upgrade(self, version: int) -> None: ...
    focusable: bool
    thumb_dim: int
    height: int
    width: int
    hidden: bool
    hovered: Incomplete
    unhovered: Incomplete
    released: Incomplete
    def __init__(
        self,
        range: int | float | None = None,
        value: int | float | renpy.ui.BarValue | None = None,
        width: int | None = None,
        height: int | None = None,
        changed: Callable[[int | float], None] | None = None,
        adjustment: Adjustment | None = None,
        step: int | float | None = None,
        page: int | float | None = None,
        bar: Incomplete = None,
        style: StyleLike = None,
        vertical: bool = False,
        replaces: Self | None = None,
        hovered: ActionType = None,
        unhovered: ActionType = None,
        released: ActionType = None,
        **properties,
    ) -> None: ...
    def per_interact(self) -> None: ...
    def visit(self) -> list[Displayable]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def focus(self, default: bool = False) -> None: ...
    def unfocus(self, default: bool = False) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def set_style_prefix(self, prefix: str, root: bool) -> None: ...
    def _tts(self, raw: bool) -> str: ...
    def _tts_all(self, raw: bool) -> str: ...

class Conditional(renpy.display.layout.Container):
    condition: Incomplete
    null: Incomplete
    state: Incomplete
    def __init__(self, condition: str, *args, **properties) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class TimerState(renpy.python.AlwaysRollback):
    started: bool
    next_event: float | None

class Timer(renpy.display.layout.Null):
    __version__: int
    started: bool
    _box_skip: bool
    modal: bool
    state: Incomplete
    def after_upgrade(self, version: int) -> None: ...
    delay: Incomplete
    repeat: Incomplete
    next_event: float | None
    function: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(
        self,
        delay: float,
        action: ActionType = None,
        repeat: bool = False,
        args: Incomplete = (),
        kwargs: Incomplete = {},
        replaces: Self | None = None,
        modal: bool | None = None,
        **properties,
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class MouseArea(renpy.display.displayable.Displayable):
    at_st_offset: float
    hovered: Incomplete
    unhovered: Incomplete
    is_hovered: bool
    width: float
    height: float
    def __init__(
        self,
        hovered: ActionType | None = None,
        unhovered: ActionType | None = None,
        replaces: Self | None = None,
        **properties,
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class OnEvent(renpy.display.displayable.Displayable):
    event_name: Incomplete
    action: Incomplete
    def __init__(self, event: str | Sequence[str], action: ActionType = []) -> None: ...
    def is_event(self, event: str) -> bool: ...
    def _handles_event(self, event: str) -> bool: ...
    def set_transform_event(self, event: str) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class AreaPicker(renpy.display.layout.Container):
    rows: Incomplete
    cols: Incomplete
    rect0: tuple[float, float, float, float] | None
    rect1: tuple[float, float, float, float] | None
    width: int
    height: int
    position: Incomplete
    changed: Incomplete
    finished: Incomplete
    persist: Incomplete
    def __init__(
        self,
        rows: int | None = None,
        cols: int | None = None,
        position: Callable[[tuple[float, float]], None] | None = None,
        changed: Callable[[tuple[int, int, int, int]], None] | None = None,
        finished: Callable[[tuple[int, int, int, int]], None] | None = None,
        persist: bool = False,
        **properties,
    ) -> None: ...
    def round_to_grid(
        self, x: float, y: float, current: tuple[float, float, float, float] | None
    ) -> tuple[float, float, float, float] | None: ...
    def get_rect(self) -> tuple[int, int, int, int] | None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class WebInput(renpy.display.displayable.Displayable):
    active: Self | None
    prompt: Incomplete
    default: Incomplete
    allow: Incomplete
    exclude: Incomplete
    mask: Incomplete
    value: Incomplete
    def __init__(
        self,
        prompt: str,
        default: str = "",
        allow: str | None = None,
        exclude: str = "{}",
        mask: bool = False,
        **properties,
    ) -> None: ...
    @staticmethod
    def pre_find_focusable() -> None: ...
    def find_focusable(self, callback: Incomplete, focus_name: Incomplete) -> None: ...
    @staticmethod
    def post_find_focusable() -> None: ...
    def activate(self) -> None: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
