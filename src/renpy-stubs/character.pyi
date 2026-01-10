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
    def __init__(
        self, callbacks: Incomplete, interact: Incomplete, type: Incomplete, cb_args: Incomplete, multiple: Incomplete
    ) -> None: ...
    def __call__(self, *args, **kwargs) -> None: ...
    def copy(self) -> Incomplete: ...

class DialogueTextTags:
    text: str
    pause_start: Incomplete
    pause_end: Incomplete
    pause_delay: Incomplete
    no_wait: bool
    has_done: bool
    fast: bool
    def __init__(self, s: Incomplete) -> None: ...

class CTCPauseHolder(renpy.display.displayable.Displayable):
    ctc: Incomplete
    def __init__(self, ctc: Incomplete) -> None: ...
    def render(self, width: Incomplete, height: Incomplete, st: Incomplete, at: Incomplete) -> Incomplete: ...
    def visit(self) -> Incomplete: ...
    def get_position(self) -> Incomplete: ...

def predict_show_display_say(
    who: Incomplete,
    what: Incomplete,
    who_args: Incomplete,
    what_args: Incomplete,
    window_args: Incomplete,
    image: bool = False,
    two_window: bool = False,
    side_image: Incomplete = None,
    screen: Incomplete = None,
    properties: Incomplete = None,
    **kwargs,
) -> None: ...
def compute_widget_properties(
    who_args: Incomplete,
    what_args: Incomplete,
    window_args: Incomplete,
    properties: Incomplete,
    variant: Incomplete = None,
    multiple: Incomplete = None,
) -> Incomplete: ...
def show_display_say(
    who: Incomplete,
    what: Incomplete,
    who_args: Incomplete = {},
    what_args: Incomplete = {},
    window_args: Incomplete = {},
    image: bool = False,
    side_image: Incomplete = None,
    two_window: bool = False,
    two_window_vbox_properties: Incomplete = {},
    who_window_properties: Incomplete = {},
    say_vbox_properties: Incomplete = {},
    transform: Incomplete = None,
    variant: Incomplete = None,
    screen: Incomplete = None,
    layer: Incomplete = None,
    properties: Incomplete = {},
    multiple: Incomplete = None,
    retain: Incomplete = None,
    **kwargs,
) -> Incomplete: ...

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
        self,
        ctc: Incomplete,
        ctc_position: Incomplete,
        callback: Incomplete,
        interact: Incomplete,
        type: Incomplete,
        cb_args: Incomplete,
        delay: Incomplete,
        ctc_kwargs: Incomplete,
        last_pause: Incomplete,
        no_wait: Incomplete,
    ) -> None: ...
    def __call__(self) -> None: ...

afm_text_queue: Incomplete

def display_say(
    who: Incomplete,
    what: Incomplete,
    show_function: Incomplete,
    interact: Incomplete,
    slow: Incomplete,
    afm: Incomplete,
    ctc: Incomplete,
    ctc_pause: Incomplete,
    ctc_position: Incomplete,
    all_at_once: Incomplete,
    cb_args: Incomplete,
    with_none: Incomplete,
    callback: Incomplete,
    type: Incomplete,
    checkpoint: bool = True,
    ctc_timedpause: Incomplete = None,
    ctc_force: bool = False,
    advance: bool = True,
    multiple: Incomplete = None,
    dtt: Incomplete = None,
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
    def copy(self, name: Incomplete = ..., **properties) -> Incomplete: ...
    def do_add(self, who: Incomplete, what: Incomplete, multiple: Incomplete = None) -> None: ...
    def get_show_properties(self, extra_properties: Incomplete) -> Incomplete: ...
    def do_show(
        self,
        who: Incomplete,
        what: Incomplete,
        multiple: Incomplete = None,
        extra_properties: Incomplete = None,
        retain: Incomplete = None,
    ) -> Incomplete: ...
    def do_done(self, who: Incomplete, what: Incomplete, multiple: Incomplete = None) -> None: ...
    def do_extend(self) -> None: ...
    def do_display(self, who: Incomplete, what: Incomplete, **display_args: Incomplete) -> None: ...
    def do_predict(self, who: Incomplete, what: Incomplete, extra_properties: Incomplete = None) -> Incomplete: ...
    def resolve_say_attributes(self, predict: Incomplete, attrs: Incomplete) -> Incomplete: ...
    def handle_say_attributes(self, predicting: Incomplete, interact: Incomplete) -> Incomplete: ...
    def handle_say_transition(self, mode: Incomplete, before: Incomplete, after: Incomplete) -> None: ...
    def restore_say_attributes(self, predicting: Incomplete, state: Incomplete, interact: Incomplete) -> Incomplete: ...
    def __format__(self, spec: Incomplete) -> str: ...
    def empty_window(self, multiple: Incomplete = None) -> None: ...
    def has_character_arguments(self, **kwargs: Incomplete) -> Incomplete: ...
    def prefix_suffix(
        self, thing: Incomplete, prefix: Incomplete, body: Incomplete, suffix: Incomplete
    ) -> Incomplete: ...
    def __call__(
        self,
        what: Incomplete,
        interact: bool = True,
        _call_done: bool = True,
        multiple: Incomplete = None,
        **kwargs: Incomplete,
    ) -> Incomplete: ...
    def statement_name(self) -> Incomplete: ...
    def predict(self, what: str) -> Incomplete: ...
    def will_interact(self) -> Incomplete: ...
    def add_history(
        self, kind: Incomplete, who: Incomplete, what: Incomplete, multiple: Incomplete = None, **kwargs: Incomplete
    ) -> None: ...
    def pop_history(self) -> None: ...

def Character(name: Incomplete = ..., kind: Incomplete = None, **properties: Incomplete) -> Incomplete: ...
def DynamicCharacter(name_expr: Incomplete, **properties) -> Incomplete: ...
