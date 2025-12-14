from _typeshed import Incomplete
from renpy.display.render import render as render
from typing import Callable

DISTRIBUTION_FUNC_T = Callable[[float, float], float]

def linear(a: float, b: float) -> float: ...
def gaussian(a: float, b: float) -> float: ...
def arcsine(a: float, b: float) -> float: ...

distribution_func_map: Incomplete

class SpriteCache(renpy.object.Object):
    nosave: Incomplete
    child: renpy.display.displayable.Displayable | None
    child_copy: renpy.display.displayable.Displayable | None
    st: float | None
    render: renpy.display.render.Render | None
    fast: bool

class Sprite(renpy.object.Object):
    x: int | float | renpy.display.core.absolute
    y: int | float | renpy.display.core.absolute
    zorder: int | float
    child: renpy.display.displayable.Displayable | None
    render: renpy.display.render.Render | None
    live: bool
    manager: SpriteManager | None
    cache: Incomplete
    def set_child(self, d) -> None: ...
    events: bool
    def destroy(self) -> None: ...

class SpriteManager(renpy.display.displayable.Displayable):
    animation: bool
    update_function: Incomplete
    event_function: Incomplete
    predict_function: Incomplete
    ignore_time: Incomplete
    displayable_map: Incomplete
    children: Incomplete
    dead_child: bool
    events: bool
    width: Incomplete
    height: Incomplete
    def __init__(
        self, update=None, event=None, predict=None, ignore_time: bool = False, animation: bool = True, **properties
    ) -> None: ...
    def create(self, d): ...
    def predict_one(self) -> None: ...
    def redraw(self, delay: int = 0) -> None: ...
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...
    def visit(self): ...
    def destroy_all(self) -> None: ...

class Particles(renpy.display.displayable.Displayable, renpy.rollback.NoRollback):
    __version__: int
    nosave: Incomplete
    properties: Incomplete
    sm: Incomplete
    def after_upgrade(self, version) -> None: ...
    particles: Incomplete
    def after_setstate(self) -> None: ...
    factory: Incomplete
    def __init__(self, factory, animation: bool = False, **properties) -> None: ...
    def update_callback(self, st): ...
    def predict_callback(self): ...
    def render(self, w, h, st, at): ...
    def visit(self): ...

class SnowBlossomFactory(renpy.rollback.NoRollback):
    rotate: bool
    image: Incomplete
    count: Incomplete
    xspeed: Incomplete
    yspeed: Incomplete
    border: Incomplete
    start: Incomplete
    fast: Incomplete
    distribution: Incomplete
    def __init__(
        self,
        image,
        count,
        xspeed,
        yspeed,
        border,
        start,
        fast,
        rotate: bool = False,
        distribution: DISTRIBUTION_FUNC_T | str = "linear",
    ) -> None: ...
    starts: Incomplete
    def init(self) -> None: ...
    def create(self, particles, st): ...
    def predict(self): ...

class SnowBlossomParticle(renpy.rollback.NoRollback):
    image: Incomplete
    xspeed: Incomplete
    yspeed: Incomplete
    border: Incomplete
    start: Incomplete
    offset: Incomplete
    rotate: Incomplete
    ystart: Incomplete
    xstart: Incomplete
    def __init__(
        self, image, xspeed, yspeed, border, start, offset, fast, rotate, distribution: DISTRIBUTION_FUNC_T = ...
    ) -> None: ...
    def update(self, st): ...

def SnowBlossom(
    d,
    count: int = 10,
    border: int = 50,
    xspeed=(20, 50),
    yspeed=(100, 200),
    start: int = 0,
    fast: bool = False,
    horizontal: bool = False,
    distribution: DISTRIBUTION_FUNC_T | str = "linear",
    animation: bool = False,
): ...
