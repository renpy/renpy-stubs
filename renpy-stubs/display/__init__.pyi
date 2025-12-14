import renpy
from _typeshed import Incomplete

draw: renpy.display.core.Renderer | None
interface: renpy.display.core.Interface | None
less_imagedissolve: bool
touch: bool
info: Incomplete
can_fullscreen: bool

def get_info(): ...

log: Incomplete
ic_log: Incomplete
to_log: Incomplete
