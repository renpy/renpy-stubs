from _typeshed import Incomplete as Incomplete
from typing import Protocol

class BaseMotion(Protocol):
    duration: Incomplete
    def get(self, st: float, fade_st: float | None, do_fade_in: bool, do_fade_out: bool) -> Incomplete: ...
    def wait(self, st: float, fade_st: float | None, do_fade_in: bool, do_fade_out: bool) -> float | None: ...

def cosine_easing(done: Incomplete) -> Incomplete: ...

class Linear:
    duration: Incomplete
    y0: Incomplete
    y1: Incomplete
    def __init__(self, x0: Incomplete, y0: Incomplete, x1: Incomplete, y1: Incomplete) -> None: ...
    def get(self, t: Incomplete) -> Incomplete: ...
    def wait(self, t: Incomplete) -> Incomplete: ...

class Step:
    duration: Incomplete
    y0: Incomplete
    y1: Incomplete
    def __init__(self, x0: Incomplete, y0: Incomplete, x1: Incomplete, y1: Incomplete) -> None: ...
    def get(self, t: Incomplete) -> Incomplete: ...
    def wait(self, t: Incomplete) -> Incomplete: ...

class InvStep:
    duration: Incomplete
    y0: Incomplete
    y1: Incomplete
    def __init__(self, x0: Incomplete, y0: Incomplete, x1: Incomplete, y1: Incomplete) -> None: ...
    def get(self, t: Incomplete) -> Incomplete: ...
    def wait(self, t: Incomplete) -> Incomplete: ...

class Bezier:
    duration: Incomplete
    x0: int
    x1: Incomplete
    x2: Incomplete
    x3: Incomplete
    y0: Incomplete
    y1: Incomplete
    y2: Incomplete
    y3: Incomplete
    def __init__(
        self,
        x0: Incomplete,
        y0: Incomplete,
        x1: Incomplete,
        y1: Incomplete,
        x2: Incomplete,
        y2: Incomplete,
        x3: Incomplete,
        y3: Incomplete,
    ) -> None: ...
    def get(self, t: Incomplete) -> Incomplete: ...
    def wait(self, t: Incomplete) -> Incomplete: ...

class Motion:
    filename: Incomplete
    duration: Incomplete
    curves: Incomplete
    fades: Incomplete
    def __init__(self, filename: Incomplete, fadein: Incomplete, fadeout: Incomplete) -> None: ...
    def get(self, st: float, fade_st: float | None, do_fade_in: bool, do_fade_out: bool) -> Incomplete: ...
    def wait(self, st: float, fade_st: float | None, do_fade_in: bool, do_fade_out: bool) -> float | None: ...

class NullMotion:
    duration: float
    def get(self, st: float, fade_st: float | None, do_fade_in: bool, do_fade_out: bool) -> Incomplete: ...
    def wait(self, st: float, fade_st: float | None, do_fade_in: bool, do_fade_out: bool) -> float | None: ...
