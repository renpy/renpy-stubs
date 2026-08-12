from collections.abc import Callable
from typing import Any

import renpy
from _typeshed import Incomplete

class _SplineInterpolator:
    ANCHORS: dict[str, float]
    points: list[list[Incomplete]]
    initialized: tuple | None
    def __init__(self, points: list, anchors: tuple[float, float] = (0.5, 0.5)) -> None: ...
    def init_values(self, sizes: tuple) -> None: ...
    def __call__(self, t: float, sizes: tuple) -> tuple: ...

def SplineMotion(
    points: list[Incomplete],
    time: float,
    child: renpy.display.displayable.Displayable | None = None,
    anchors: tuple[float, float] = (0.5, 0.5),
    repeat: bool = False,
    bounce: bool = False,
    anim_timebase: bool = False,
    style: str = "default",
    time_warp: Callable[[float], float] | None = None,
    **properties: Any,
) -> renpy.display.motion.Motion: ...
