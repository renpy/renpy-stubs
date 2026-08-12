from renpy.pygame import (
    CONTROLLERAXISMOTION as CONTROLLERAXISMOTION,
    CONTROLLERBUTTONDOWN as CONTROLLERBUTTONDOWN,
    CONTROLLERBUTTONUP as CONTROLLERBUTTONUP,
    CONTROLLERDEVICEADDED as CONTROLLERDEVICEADDED,
    CONTROLLERDEVICEREMOVED as CONTROLLERDEVICEREMOVED,
)
from renpy.pygame.controller import (
    Controller as Controller,
    get_string_for_axis as get_string_for_axis,
    get_string_for_button as get_string_for_button,
)
from renpy.pygame.event import EventType as EventType
from typing import Literal

def load_mappings() -> None: ...
def init() -> None: ...

controllers: dict[int, Controller]
axis_positions: dict[tuple[Controller, int], Literal["pos", "neg", "zero", None]]
THRESHOLD: int
ZERO_THRESHOLD: int
ignore: bool

def post_event(control: str, state: str, repeat: bool) -> None: ...
def exists() -> bool: ...
def quit(index: int) -> None: ...
def start(index: int) -> None: ...

class PadEvent:
    control: str
    state: Literal["pos", "neg", "zero", "press", "release", None]
    repeat_time: int
    def __init__(self, control: str) -> None: ...
    def event(self, state: Literal["pos", "neg", "zero", "press", "release", None]) -> None: ...
    def repeat(self) -> None: ...

pad_events: dict[str | None, PadEvent]

def controller_event(control: str | None, state: Literal["pos", "neg", "zero", "press", "release", None]) -> None: ...
def periodic() -> None: ...
def event(ev: EventType) -> EventType | None: ...
