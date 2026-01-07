import renpy
from renpy.display.layout import Null as Null
from renpy.pygame.joystick import Joystick as Joystick

enabled: bool

class JoyBehavior(renpy.display.layout.Null): ...

joysticks: dict[int, Joystick]

def count() -> int: ...
def get(n: int) -> Joystick | None: ...
