from _typeshed import Incomplete

class _SplineInterpolator:
    ANCHORS: Incomplete
    points: Incomplete
    initialized: Incomplete
    def __init__(self, points: Incomplete, anchors: Incomplete = (0.5, 0.5)) -> None: ...
    def init_values(self, sizes: Incomplete) -> Incomplete: ...
    def __call__(self, t: Incomplete, sizes: Incomplete) -> Incomplete: ...

def SplineMotion(
    points: Incomplete,
    time: Incomplete,
    child: Incomplete = None,
    anchors: Incomplete = (0.5, 0.5),
    repeat: bool = False,
    bounce: bool = False,
    anim_timebase: bool = False,
    style: str = "default",
    time_warp: Incomplete = None,
    **properties,
) -> Incomplete: ...
