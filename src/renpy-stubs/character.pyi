import re
from collections.abc import Callable, Sequence
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    NotRequired,
    Protocol,
    TypeAlias,
    TypedDict,
    Unpack,
    overload,
    type_check_only,
)

import renpy
from renpy.display.displayable import Displayable as Displayable
from renpy.object import Object as Object
from renpy.object import Sentinel as Sentinel
from renpy.text.text import Text as Text

# The value returned by a `show_function` (e.g. `show_display_say`). A
# screen-based say statement returns `(tag, widget_id, layer)`, while a
# non-screen statement returns the `ui.text` widget directly.
type ShowResult = Text | tuple[str, str, str] | None

# The (attributes, images) state returned by `ADVCharacter.handle_say_attributes`
# and consumed by `restore_say_attributes`.
type _SayAttributeState = tuple[tuple[str, ...], renpy.display.image.ShownImageInfo]

if TYPE_CHECKING:
    class CharacterCallbackParameters(TypedDict):
        interact: bool
        type: Literal["nvl", "adv", "bubble"]
        what: str
        multiple: NotRequired[tuple[int, int]]

        start: NotRequired[int]
        end: NotRequired[int]
        delay: NotRequired[float | None]
        last_segment: NotRequired[bool]

        exception: bool
        please_ignore_unknown_keyword_arguments: NotRequired[None]

    class CharacterCallback(Protocol):
        def __call__(
            self,
            event: Literal["begin", "show", "show_done", "slow_done", "interact_done", "end"],
            **kwargs: Unpack[CharacterCallbackParameters],
        ) -> None: ...

TAG_RE: re.Pattern[str]
less_pauses: bool

class Callbacks:
    callbacks: Sequence[CharacterCallback] | None
    interact: bool
    type: str | None
    cb_args: dict[str, Any]
    multiple: tuple[int, int] | None
    what: str | None
    start: int | None
    end: int | None
    delay: float | None
    last_segment: bool | None
    def __init__(
        self,
        callbacks: Sequence[CharacterCallback] | None,
        interact: bool,
        type: str | None,
        cb_args: dict[str, Any],
        multiple: tuple[int, int] | None,
    ) -> None: ...
    def __call__(self, *args: str, **kwargs: Any) -> None: ...
    def copy(self) -> Callbacks: ...

class DialogueTextTags:
    text: str
    pause_start: list[int]
    afm_start: list[int]
    pause_end: list[int]
    pause_delay: list[float | None]
    no_wait: bool
    has_done: bool
    fast: bool
    def __init__(self, s: str) -> None: ...

class CTCPauseHolder(renpy.display.displayable.Displayable):
    ctc: Displayable
    rtl: bool
    def __init__(self, ctc: Displayable) -> None: ...
    def set_rtl(self, rtl: bool) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def visit(self) -> list[Displayable | None]: ...
    def get_position(self) -> tuple[int, int]: ...

def predict_show_display_say(
    who: str | Displayable | None,
    what: str | Displayable | list[Displayable | str],
    who_args: dict[str, Any],
    what_args: dict[str, Any],
    window_args: dict[str, Any],
    image: bool | str = False,
    two_window: bool = False,
    side_image: Displayable | None = None,
    screen: str | None = None,
    properties: dict[str, Any] | None = None,
    **kwargs: Any,
) -> None: ...
def compute_widget_properties(
    who_args: dict[str, Any],
    what_args: dict[str, Any],
    window_args: dict[str, Any],
    properties: dict[str, Any],
    variant: str | None = None,
    multiple: tuple[int, int] | None = None,
) -> dict[str, Any]: ...
def show_display_say(
    who: str | Displayable | None,
    what: str | Displayable | list[Displayable | str],
    who_args: dict[str, Any] = {},
    what_args: dict[str, Any] = {},
    window_args: dict[str, Any] = {},
    image: bool | str = False,
    side_image: Displayable | None = None,
    two_window: bool = False,
    two_window_vbox_properties: dict[str, Any] = {},
    who_window_properties: dict[str, Any] = {},
    say_vbox_properties: dict[str, Any] = {},
    transform: Displayable | None = None,
    variant: str | None = None,
    screen: str | None = None,
    layer: str | None = None,
    properties: dict[str, Any] = {},
    multiple: tuple[int, int] | None = None,
    retain: str | bool | None = None,
    **kwargs: Any,
) -> ShowResult: ...

class SlowDone:
    delay: float | None
    ctc_kwargs: dict[str, Any]
    last_pause: bool
    no_wait: bool
    screen_tag: str | None
    screen_layer: str | None
    ctc: Displayable | None
    ctc_position: str
    callback: Callbacks
    interact: bool
    type: str | None
    cb_args: dict[str, Any]
    def __init__(
        self,
        ctc: Displayable | None,
        ctc_position: str,
        callback: Callbacks,
        interact: bool,
        type: str | None,
        cb_args: dict[str, Any],
        delay: float | None,
        ctc_kwargs: dict[str, Any],
        last_pause: bool,
        no_wait: bool,
    ) -> None: ...
    def __call__(self) -> None: ...

afm_text_queue: list[Text]

def display_say(
    who: str | Displayable | None,
    what: str | Displayable | list[Displayable | str],
    show_function: Callable[..., ShowResult],
    interact: bool,
    slow: bool,
    afm: bool,
    ctc: Displayable | None,
    ctc_pause: Displayable | None,
    ctc_position: Literal["nestled", "nestled-close", "fixed", "screen-variable"],
    all_at_once: bool,
    cb_args: dict[str, Any],
    with_none: bool | None,
    callback: CharacterCallback | Sequence[CharacterCallback] | None,
    type: str | None,
    checkpoint: bool = True,
    ctc_timedpause: Displayable | None = None,
    ctc_force: bool = False,
    advance: bool = True,
    multiple: tuple[int, int] | None = None,
    dtt: DialogueTextTags | None = None,
    retain: bool = False,
) -> None: ...

class HistoryEntry(renpy.object.Object):
    multiple: tuple[int, int] | None
    who: str | Displayable | None
    what: str | Displayable | list[Displayable | str]
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

NotSet: Sentinel
multiple_count: int

class ADVCharacter:
    special_properties: list[str]
    voice_tag: str | None
    properties: dict[str, dict[str, Any]]
    name: str | None
    who_prefix: str
    who_suffix: str
    what_prefix: str
    what_suffix: str
    show_function: Callable[..., ShowResult]
    predict_function: Callable[..., None]
    condition: str | None
    dynamic: bool
    screen: str | None
    mode: str | None
    image_tag: str | None
    display_args: dict[str, Any]
    who_args: dict[str, Any]
    what_args: dict[str, Any]
    window_args: dict[str, Any]
    show_args: dict[str, Any]
    cb_args: dict[str, Any]
    def __init__(
        self, name: str | None | Sentinel = ..., kind: Literal[False] | None | ADVCharacter = None, **properties: Any
    ) -> None: ...
    def copy(self, name: str | None | Sentinel = ..., **properties: Any) -> ADVCharacter: ...
    def do_add(
        self,
        who: str | Displayable | None,
        what: str | Displayable | list[Displayable | str],
        multiple: tuple[int, int] | None = None,
    ) -> None: ...
    def get_show_properties(
        self, extra_properties: dict[str, Any] | None
    ) -> tuple[
        str | None,
        dict[str, Any],
        dict[str, Any],
        dict[str, Any],
        dict[str, Any],
        dict[str, Any],
    ]: ...
    def do_show(
        self,
        who: str | Displayable | None,
        what: str | Displayable | list[Displayable | str],
        multiple: tuple[int, int] | None = None,
        extra_properties: dict[str, Any] | None = None,
        retain: str | bool | None = None,
    ) -> ShowResult: ...
    def do_done(
        self,
        who: str | Displayable | None,
        what: str | Displayable | list[Displayable | str],
        multiple: tuple[int, int] | None = None,
    ) -> None: ...
    def do_extend(self) -> None: ...
    def do_display(
        self, who: str | Displayable | None, what: str | Displayable | list[Displayable | str], **display_args: Any
    ) -> None: ...
    def do_predict(
        self,
        who: str | Displayable | None,
        what: str | Displayable | list[Displayable | str],
        extra_properties: dict[str, Any] | None = None,
    ) -> None: ...
    def resolve_say_attributes(self, predict: bool, attrs: Sequence[str] | None) -> bool | None: ...
    def handle_say_attributes(self, predicting: bool, interact: bool) -> _SayAttributeState | None: ...
    def handle_say_transition(
        self, mode: Literal["permanent", "temporary", "both", "restore"], before: Sequence[str], after: Sequence[str]
    ) -> None: ...
    def restore_say_attributes(
        self, predicting: bool, state: _SayAttributeState | None, interact: bool
    ) -> bool | None: ...
    def __format__(self, spec: str) -> str: ...
    def empty_window(self, multiple: int | None = None) -> None: ...
    def has_character_arguments(self, **kwargs: Any) -> bool: ...
    def prefix_suffix(self, thing: Literal["who", "what"], prefix: str, body: str, suffix: str) -> str: ...
    def __call__(
        self,
        what: str,
        interact: bool = True,
        _call_done: bool = True,
        multiple: int | None = None,
        **kwargs: Any,
    ) -> bool | None: ...
    def statement_name(self) -> str: ...
    def predict(self, what: str) -> None: ...
    def will_interact(self) -> bool: ...
    def add_history(
        self,
        kind: str,
        who: str | Displayable | None,
        what: str | Displayable | list[Displayable | str],
        multiple: tuple[int, int] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def pop_history(self) -> None: ...

@overload
def Character(
    name: str | None | Sentinel = ...,
    kind: None = None,
    **properties: Any,
) -> ADVCharacter: ...
@overload
def Character[T](
    name: str | None | Sentinel = ...,
    kind: T = ...,
    **properties: Any,
) -> T: ...
def DynamicCharacter(name_expr: str, **properties: Any) -> ADVCharacter: ...
