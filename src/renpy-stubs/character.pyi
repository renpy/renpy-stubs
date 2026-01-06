import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.displayable import Displayable as Displayable
from renpy.object import Object as Object, Sentinel as Sentinel
from typing import Literal

TAG_RE: Incomplete
less_pauses: Incomplete

class Callbacks:
    callbacks: Incomplete
    interact: Incomplete
    type: Incomplete
    cb_args: Incomplete
    multiple: tuple[int, int] | None
    what: str | None
    start: int | None
    end: int | None
    delay: float | None
    last_segment: bool | None
    def __init__(self, callbacks, interact, type, cb_args, multiple) -> None: ...
    def __call__(self, *args, **kwargs) -> None: ...
    def copy(self): ...

class DialogueTextTags:
    text: str
    pause_start: Incomplete
    pause_end: Incomplete
    pause_delay: Incomplete
    no_wait: bool
    has_done: bool
    fast: bool
    def __init__(self, s) -> None: ...

class CTCPauseHolder(renpy.display.displayable.Displayable):
    ctc: Incomplete
    def __init__(self, ctc) -> None: ...
    def render(self, width, height, st, at): ...
    def visit(self): ...
    def get_position(self): ...

def predict_show_display_say(
    who,
    what,
    who_args,
    what_args,
    window_args,
    image: bool = False,
    two_window: bool = False,
    side_image=None,
    screen=None,
    properties=None,
    **kwargs,
) -> None: ...
def compute_widget_properties(who_args, what_args, window_args, properties, variant=None, multiple=None): ...
def show_display_say(
    who,
    what,
    who_args={},
    what_args={},
    window_args={},
    image: bool = False,
    side_image=None,
    two_window: bool = False,
    two_window_vbox_properties={},
    who_window_properties={},
    say_vbox_properties={},
    transform=None,
    variant=None,
    screen=None,
    layer=None,
    properties={},
    multiple=None,
    retain=None,
    **kwargs,
): ...

class SlowDone:
    delay: Incomplete
    ctc_kwargs: Incomplete
    last_pause: bool
    no_wait: bool
    screen_tag: Incomplete
    screen_layer: Incomplete
    ctc: Incomplete
    ctc_position: Incomplete
    callback: Incomplete
    interact: Incomplete
    type: Incomplete
    cb_args: Incomplete
    def __init__(
        self, ctc, ctc_position, callback, interact, type, cb_args, delay, ctc_kwargs, last_pause, no_wait
    ) -> None: ...
    def __call__(self) -> None: ...

afm_text_queue: Incomplete

def display_say(
    who,
    what,
    show_function,
    interact,
    slow,
    afm,
    ctc,
    ctc_pause,
    ctc_position,
    all_at_once,
    cb_args,
    with_none,
    callback,
    type,
    checkpoint: bool = True,
    ctc_timedpause=None,
    ctc_force: bool = False,
    advance: bool = True,
    multiple=None,
    dtt=None,
    retain: bool = False,
) -> None: ...

class HistoryEntry(renpy.object.Object):
    multiple: Incomplete
    who: Incomplete
    what: Incomplete
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

NotSet: Incomplete
multiple_count: int

class ADVCharacter:
    special_properties: Incomplete
    voice_tag: Incomplete
    properties: Incomplete
    name: Incomplete
    who_prefix: Incomplete
    who_suffix: Incomplete
    what_prefix: Incomplete
    what_suffix: Incomplete
    show_function: Incomplete
    predict_function: Incomplete
    condition: Incomplete
    dynamic: Incomplete
    screen: Incomplete
    mode: Incomplete
    image_tag: Incomplete
    display_args: Incomplete
    who_args: Incomplete
    what_args: Incomplete
    window_args: Incomplete
    show_args: Incomplete
    cb_args: Incomplete
    def __init__(
        self, name: str | None | Sentinel = ..., kind: Literal[False] | None | ADVCharacter = None, **properties
    ) -> None: ...
    def copy(self, name=..., **properties): ...
    def do_add(self, who, what, multiple=None) -> None: ...
    def get_show_properties(self, extra_properties): ...
    def do_show(self, who, what, multiple=None, extra_properties=None, retain=None): ...
    def do_done(self, who, what, multiple=None) -> None: ...
    def do_extend(self) -> None: ...
    def do_display(self, who, what, **display_args) -> None: ...
    def do_predict(self, who, what, extra_properties=None): ...
    def resolve_say_attributes(self, predict, attrs): ...
    def handle_say_attributes(self, predicting, interact): ...
    def handle_say_transition(self, mode, before, after) -> None: ...
    def restore_say_attributes(self, predicting, state, interact): ...
    def __format__(self, spec) -> str: ...
    def empty_window(self, multiple=None) -> None: ...
    def has_character_arguments(self, **kwargs): ...
    def prefix_suffix(self, thing, prefix, body, suffix): ...
    def __call__(self, what, interact: bool = True, _call_done: bool = True, multiple=None, **kwargs): ...
    def statement_name(self): ...
    def predict(self, what): ...
    def will_interact(self): ...
    def add_history(self, kind, who, what, multiple=None, **kwargs) -> None: ...
    def pop_history(self) -> None: ...

def Character(name=..., kind=None, **properties): ...
def DynamicCharacter(name_expr, **properties): ...
