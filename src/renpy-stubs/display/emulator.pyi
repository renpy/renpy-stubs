from renpy.display.displayable import Displayable as Displayable
from renpy.pygame.event import EventType as EventType
from typing import Callable

emulator: Callable[[EventType, int, int], tuple[EventType | None, int, int]] | None
overlay: list[Displayable]
ios: bool

def null_emulator(ev: EventType, x: int, y: int) -> tuple[EventType, int, int]: ...

TOUCH_KEYS: list[int]

def touch_emulator(ev: EventType, x: int, y: int) -> tuple[EventType | None, int, int]: ...

TV_KEYS: list[int]

def tv_emulator(ev: EventType, x: int, y: int) -> tuple[EventType | None, int, int]: ...

keyboard: Displayable | None
null: Displayable | None

def dynamic_keyboard(st: float, at: float) -> tuple[Displayable, float]: ...
def init_emulator() -> None: ...
def early_init_emulator() -> None: ...
