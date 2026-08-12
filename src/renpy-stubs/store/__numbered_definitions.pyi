from collections.abc import Callable
from typing import Any

import renpy.display.layout
import renpy.display.motion
import renpy.display.transform
import renpy.display.transition
from renpy.character import ADVCharacter

_define: Any
define: Any
_ease_out_time_warp: Callable[[float], float]
_ease_in_time_warp: Callable[[float], float]
_ease_time_warp: Callable[[float], float]

def move_transitions(
    prefix, delay, time_warp=None, in_time_warp=None, out_time_warp=None, old: bool = False, layers=["master"], **kwargs
) -> None: ...
def old_move_transitions(
    prefix, delay, time_warp=None, in_time_warp=None, out_time_warp=None, old: bool = False, layers=["master"], **kwargs
) -> None: ...

fade: renpy.display.transition.MultipleTransition
dissolve: renpy.display.transition.Dissolve
pixellate: renpy.display.transition.Pixellate
wiperight: renpy.display.transition.CropMove
wipeleft: renpy.display.transition.CropMove
wipeup: renpy.display.transition.CropMove
wipedown: renpy.display.transition.CropMove
slideright: renpy.display.transition.CropMove
slideleft: renpy.display.transition.CropMove
slideup: renpy.display.transition.CropMove
slidedown: renpy.display.transition.CropMove
slideawayright: renpy.display.transition.CropMove
slideawayleft: renpy.display.transition.CropMove
slideawayup: renpy.display.transition.CropMove
slideawaydown: renpy.display.transition.CropMove
irisout: renpy.display.transition.CropMove
irisin: renpy.display.transition.CropMove
pushright: renpy.display.transition.PushMove
pushleft: renpy.display.transition.PushMove
pushup: renpy.display.transition.PushMove
pushdown: renpy.display.transition.PushMove
zoomin: renpy.curry.Partial[renpy.display.layout.MultiBox]
zoomout: renpy.curry.Partial[renpy.display.layout.MultiBox]
zoominout: renpy.curry.Partial[renpy.display.layout.MultiBox]
vpunch: renpy.display.motion.Motion
hpunch: renpy.display.motion.Motion
blinds: renpy.display.transition.ImageDissolve
squares: renpy.display.transition.ImageDissolve
swing: renpy.display.transform.ATLTransform
_narrator: ADVCharacter
adv_narrator = _narrator
centered: ADVCharacter
vcentered: ADVCharacter
narrator = _narrator
