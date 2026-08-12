from _typeshed import Incomplete
from _frozen_importlib import BuiltinImporter as BuiltinImporter
from typing import Any, Iterable, Sequence
import renpy

Event = EventType

class EventType:
    _type = int

    ## type: pygame.ACTIVEEVENT
    state: int
    gain: int

    ## type: pygame.CONTROLLERAXISMOTION
    which: int
    axis: int
    value: int

    ## type: pygame.CONTROLLERBUTTONDOWN, pygame.CONTROLLERBUTTONUP
    which: int
    button: int
    state: int

    ## type: pygame.CONTROLLERDEVICEADDED, pygame.CONTROLLERDEVICEREMOVED, pygame.CONTROLLERDEVICEREMAPPED
    which: int

    ## type: pygame.DROPFILE, pygame.DROPTEXT, pygame.DROPBEGIN, pygame.DROPCOMPLETE
    file: str | None
    window_id: int

    ## type: pygame.FINGERMOTION, pygame.FINGERDOWN, pygame.FINGERUP
    touchId: int
    fingerId: int
    touch_id: int
    finger_id: int
    x: float
    y: float
    dx: float
    dy: float
    pressure: float

    ## type: pygame.KEYDOWN, pygame.KEYUP
    key: int
    scancode: int
    unicode: str
    mod: int
    repeat: bool

    ## type: pygame.JOYAXISMOTION
    joy: int
    instance_id: int
    axis: int
    value: float

    ## type: pygame.JOYBALLMOTION
    joy: int
    instance_id: int
    ball: int
    rel: tuple[int, int]

    ## type: pygame.JOYHATMOTION
    joy: int
    instance_id: int
    hat: int
    value: int

    ## type: pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP
    joy: int
    instance_id: int
    button: int

    ## type: pygame.JOYDEVICEADDED, pygame.JOYDEVICEREMOVED
    which: int

    ## type: renpy.display.core.EVENTNAME
    eventnames: Sequence[str]
    controller: str
    up: bool

    ## type: pygame.TIMEEVENT
    modal: bool

    ## type: pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP
    button: int
    pos: tuple[int, int]
    which: int
    touch: bool

    ## type: pygame.MOUSEMOTION
    pos: tuple[int, int]
    rel: tuple[int, int]
    buttons: tuple[int, int, int]
    which: int
    touch: bool

    ## type: pygame.MOUSEWHEEL
    which: int
    button: int
    pos: tuple[int, int]
    touch: bool

    ## type: pygame.MULTIGESTURE
    touchId: int
    dTheta: float
    dDist: float
    x: float
    y: float
    numFingers: int
    touch_id: int
    rotated: float
    pinched: float
    num_fingers: int

    ## type: pygame.TEXTEDITING
    text: str
    start: int
    length: int

    ## type: pygame.TEXTINPUT
    text: str

    ## type: pygame.VIDEORESIZE
    size: tuple[int, int]
    w: int
    h: int

    ## type: pygame.WINDOWEVENT
    event: int
    data1: int
    data2: int

    ## type: pygame.WINDOWMOVED
    pos: tuple[int, int]
    x: int
    y: int

    def __init__(self, type: int, dict: dict[str, Any] | None = None, **kwargs: Incomplete) -> None: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def type(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __repr__(self) -> str: ...

def clear(t: int | Iterable[int] | None = None) -> None: ...
def copy_event_queue() -> list[EventType]: ...
def event_name(t: int) -> str: ...
def get(t: int | Iterable[int] | None = None) -> list[EventType]: ...
def get_blocked(t: int) -> bool: ...
def get_grab() -> bool: ...
def get_mousewheel_buttons() -> bool: ...
def get_standard_events() -> list[int]: ...
def init() -> None: ...
def peek(t: int | Iterable[int] | None = None) -> bool: ...
def poll() -> EventType: ...
def post(e: EventType) -> None: ...
def pump() -> None: ...
def register(name: str) -> int: ...
def set_allowed(t: int | Iterable[int] | None = None) -> None: ...
def set_blocked(t: int | Iterable[int] | None = None) -> None: ...
def set_grab(on: bool) -> None: ...
def set_mousewheel_buttons(flag: bool) -> None: ...
def unichr(i: int) -> str: ...
def wait() -> EventType: ...

ACTIVEEVENT: int
USEREVENT_MAX: int
VIDEOEXPOSE: int
VIDEORESIZE: int
WINDOWMOVED: int
