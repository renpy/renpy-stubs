import renpy
from _typeshed import Incomplete
from renpy.display.render import Render as Render, render as render
from typing import Callable

def compile_event(key, keydown): ...

event_cache: Incomplete
keyup_cache: Incomplete

def init_keymap() -> None: ...
def clear_keymap_cache() -> None: ...
def queue_event(name, up: bool = False, **kwargs) -> None: ...
def map_event(ev, keysym): ...
def map_keyup(ev, keysym): ...
def skipping(ev) -> None: ...
def inspector(ev): ...
def predict_action(var) -> None: ...
def run(action, *args, **kwargs): ...
def run_unhovered(var) -> None: ...
def run_periodic(var, st): ...
def get_tooltip(action): ...
def is_selected(action): ...
def is_sensitive(action): ...
def alt(clicked): ...

class Keymap(renpy.display.layout.Null):
    capture: bool
    keymap: Incomplete
    def __init__(self, replaces=None, activate_sound=None, capture: bool = True, **keymap) -> None: ...
    def event(self, ev, x, y, st): ...
    def predict_one_action(self) -> None: ...

class RollForward(renpy.display.layout.Null):
    value: Incomplete
    def __init__(self, value, **properties) -> None: ...
    def event(self, ev, x, y, st): ...

class PauseBehavior(renpy.display.layout.Null):
    voice: bool
    modal: bool
    self_voice: bool
    delay: Incomplete
    result: Incomplete
    self_voicing: Incomplete
    def __init__(
        self, delay, result: bool = False, voice: bool = False, self_voicing: bool = False, modal=None, **properties
    ) -> None: ...
    def event(self, ev, x, y, st): ...

class PredictPauseBehavior(renpy.display.layout.Null):
    def __init__(self, **properties) -> None: ...
    def event(self, ev, x, y, st): ...

class SoundStopBehavior(renpy.display.layout.Null):
    channel: Incomplete
    result: Incomplete
    def __init__(self, channel, result: bool = False, **properties) -> None: ...
    def event(self, ev, x, y, st): ...

class SayBehavior(renpy.display.layout.Null):
    focusable: bool
    text_tuple: Incomplete
    dismiss_unfocused: Incomplete
    dialogue_pause: Incomplete
    afm_length: Incomplete
    dismiss: Incomplete
    allow_dismiss: Incomplete
    def __init__(
        self,
        default: bool = True,
        afm=None,
        dismiss=["dismiss"],
        allow_dismiss=None,
        dismiss_unfocused=["dismiss_unfocused"],
        dialogue_pause=None,
        **properties,
    ) -> None: ...
    def set_text(self, *args) -> None: ...
    def event(self, ev, x, y, st): ...

class DismissBehavior(renpy.display.displayable.Displayable):
    focusable: bool
    keysym: str
    action: Incomplete
    modal: Incomplete
    def __init__(self, action=None, modal: bool = True, keysym: str = "dismiss", **properties) -> None: ...
    def find_focusable(self, callback, focus_name) -> None: ...
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...

KEY_EVENTS: Incomplete

class Button(renpy.display.layout.Window):
    keymap: Incomplete
    action: Incomplete
    alternate: Incomplete
    longpress_start: Incomplete
    longpress_x: Incomplete
    longpress_y: Incomplete
    role_parameter: Incomplete
    keysym: Incomplete
    alternate_keysym: Incomplete
    locked: bool
    selected: Incomplete
    sensitive: Incomplete
    clicked: Incomplete
    hovered: Incomplete
    unhovered: Incomplete
    focusable: bool
    time_policy_data: Incomplete
    def __init__(
        self,
        child=None,
        style: str = "button",
        clicked=None,
        hovered=None,
        unhovered=None,
        action=None,
        role=None,
        time_policy=None,
        keymap={},
        alternate=None,
        selected=None,
        sensitive=None,
        keysym=None,
        alternate_keysym=None,
        **properties,
    ) -> None: ...
    def predict_one_action(self) -> None: ...
    def render(self, width, height, st, at): ...
    def focus(self, default: bool = False): ...
    def unfocus(self, default: bool = False) -> None: ...
    def is_selected(self): ...
    def is_sensitive(self): ...
    role: Incomplete
    def per_interact(self) -> None: ...
    def event(self, ev, x, y, st): ...
    def set_style_prefix(self, prefix, root) -> None: ...

def TextButton(text, style: str = "button", text_style: str = "button_text", clicked=None, **properties): ...

class ImageButton(Button):
    imagebutton_child: Incomplete
    imagebutton_raw_child: Incomplete
    state_children: Incomplete
    def __init__(
        self,
        idle_image,
        hover_image=None,
        insensitive_image=None,
        activate_image=None,
        selected_idle_image=None,
        selected_hover_image=None,
        selected_insensitive_image=None,
        selected_activate_image=None,
        style: str = "image_button",
        clicked=None,
        hovered=None,
        **properties,
    ) -> None: ...
    def visit(self): ...
    def get_child(self): ...

class HoveredProxy:
    a: Incomplete
    b: Incomplete
    def __init__(self, a, b) -> None: ...
    def __call__(self): ...

current_input_value: Incomplete
input_value_active: bool
default_input_value: Incomplete
input_values: Incomplete
inputs: Incomplete

def input_pre_per_interact() -> None: ...
def input_post_per_interact() -> None: ...

class CaretBlink(renpy.display.displayable.Displayable):
    caret: Incomplete
    caret_blink: Incomplete
    st: int
    st_base: int
    def __init__(self, caret, caret_blink, **properties) -> None: ...
    def get_placement(self): ...
    def visit(self): ...
    def render(self, width, height, st, at): ...

class Input(renpy.text.text.Text):
    changed: Incomplete
    prefix: str
    suffix: str
    caret_pos: int
    old_caret_pos: int
    pixel_width: Incomplete
    default: str
    edit_text: str
    value: Incomplete
    shown: bool
    multiline: bool
    action: Incomplete
    arrowkeys: bool
    st: int
    content: Incomplete
    length: Incomplete
    allow: Incomplete
    exclude: Incomplete
    copypaste: Incomplete
    editable: Incomplete
    caret: Incomplete
    def __init__(
        self,
        default: str = "",
        length=None,
        style: str = "input",
        allow=None,
        exclude=None,
        prefix: str = "",
        suffix: str = "",
        changed=None,
        button=None,
        replaces=None,
        editable: bool = True,
        pixel_width=None,
        value=None,
        copypaste: bool = False,
        caret_blink=None,
        multiline: bool = False,
        action=None,
        arrowkeys: bool = True,
        **properties,
    ) -> None: ...
    def update_text(self, new_content, editable, check_size: bool = False) -> None: ...
    def set_style_prefix(self, prefix, root) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def per_interact(self) -> None: ...
    def event(self, ev, x, y, st): ...
    def get_caret_above_below_pos(self): ...
    def render(self, width, height, st, at): ...

adj_registered: Incomplete

class Adjustment(renpy.object.Object):
    force_step: bool
    animation_amplitude: float | None
    animation_target: float | None
    animation_start: float | None
    animation_delay: float | None
    animation_warper: Incomplete
    restart_interaction_at_limit: bool
    restart_interaction_at_range: bool
    raw_changed: Incomplete
    changed: Incomplete
    adjustable: Incomplete
    ranged: Incomplete
    def __init__(
        self,
        range: int | float | None = 1,
        value: int | float | None = 0,
        step: int | float | None = None,
        page: int | float | None = None,
        changed: Callable | None = None,
        adjustable: bool | None = None,
        ranged: Callable | None = None,
        force_step: bool = False,
        raw_changed: Callable | None = None,
    ) -> None: ...
    range: Incomplete
    value: Incomplete
    def viewport_replaces(self, replaces: Adjustment) -> None: ...
    def round_value(self, value, release): ...
    def get_value(self): ...
    def set_value(self, v) -> None: ...
    def get_range(self): ...
    def set_range(self, v) -> None: ...
    def get_page(self): ...
    def set_page(self, v) -> None: ...
    page: Incomplete
    def get_step(self): ...
    def set_step(self, v) -> None: ...
    step: Incomplete
    def register(self, d) -> None: ...
    def change(self, value, end_animation: bool = True): ...
    def update(self) -> None: ...
    def inertia_warper(self, done): ...
    def animate(self, amplitude, delay, warper) -> None: ...
    def inertia(self, amplitude, time_constant, st) -> None: ...
    def end_animation(self, instantly: bool = False) -> None: ...
    def periodic(self, st): ...

class Bar(renpy.display.displayable.Displayable):
    __version__: int
    adjustment: Incomplete
    value: Incomplete
    def after_upgrade(self, version) -> None: ...
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
        range=None,
        value=None,
        width=None,
        height=None,
        changed=None,
        adjustment=None,
        step=None,
        page=None,
        bar=None,
        style=None,
        vertical: bool = False,
        replaces=None,
        hovered=None,
        unhovered=None,
        released=None,
        **properties,
    ) -> None: ...
    def per_interact(self) -> None: ...
    def visit(self): ...
    def render(self, width, height, st, at): ...
    def focus(self, default: bool = False) -> None: ...
    def unfocus(self, default: bool = False) -> None: ...
    def event(self, ev, x, y, st): ...
    def set_style_prefix(self, prefix, root) -> None: ...

class Conditional(renpy.display.layout.Container):
    condition: Incomplete
    null: Incomplete
    state: Incomplete
    def __init__(self, condition, *args, **properties) -> None: ...
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...

class TimerState(renpy.python.AlwaysRollback):
    started: bool
    next_event: Incomplete

class Timer(renpy.display.layout.Null):
    __version__: int
    started: bool
    modal: bool
    state: Incomplete
    def after_upgrade(self, version) -> None: ...
    delay: Incomplete
    repeat: Incomplete
    next_event: Incomplete
    function: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(
        self, delay, action=None, repeat: bool = False, args=(), kwargs={}, replaces=None, modal=None, **properties
    ) -> None: ...
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...

class MouseArea(renpy.display.displayable.Displayable):
    at_st_offset: int
    hovered: Incomplete
    unhovered: Incomplete
    is_hovered: bool
    width: int
    height: int
    def __init__(self, hovered=None, unhovered=None, replaces=None, **properties) -> None: ...
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...

class OnEvent(renpy.display.displayable.Displayable):
    event_name: Incomplete
    action: Incomplete
    def __init__(self, event, action=[]) -> None: ...
    def is_event(self, event): ...
    def set_transform_event(self, event) -> None: ...
    def render(self, width, height, st, at): ...

class AreaPicker(renpy.display.layout.Container):
    rows: Incomplete
    cols: Incomplete
    rect0: Incomplete
    rect1: Incomplete
    width: int
    height: int
    position: Incomplete
    changed: Incomplete
    finished: Incomplete
    persist: Incomplete
    def __init__(
        self, rows=None, cols=None, position=None, changed=None, finished=None, persist: bool = False, **properties
    ) -> None: ...
    def round_to_grid(self, x, y, current): ...
    def get_rect(self): ...
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st) -> None: ...

class WebInput(renpy.display.displayable.Displayable):
    active: Incomplete
    prompt: Incomplete
    default: Incomplete
    allow: Incomplete
    exclude: Incomplete
    mask: Incomplete
    value: Incomplete
    def __init__(
        self, prompt, default: str = "", allow=None, exclude: str = "{}", mask: bool = False, **properties
    ) -> None: ...
    @staticmethod
    def pre_find_focusable() -> None: ...
    def find_focusable(self, callback, focus_name) -> None: ...
    @staticmethod
    def post_find_focusable() -> None: ...
    def activate(self) -> None: ...
    def event(self, ev, x, y, st): ...
    def render(self, width, height, st, at): ...
