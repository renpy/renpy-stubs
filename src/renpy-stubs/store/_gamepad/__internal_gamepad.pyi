from typing import Any

import renpy
from renpy.display.render import Render
from renpy.pygame.event import EventType

_constant: bool

class EventWatcher(renpy.display.displayable.Displayable):
    bound: set[str]
    mappings: dict[str, str]
    def __init__(self, mappings: dict[str, str]) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

def calibrate(index: int | None = None) -> None: ...
