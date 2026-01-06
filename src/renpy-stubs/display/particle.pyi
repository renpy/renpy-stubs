import renpy
import renpy.display
import renpy.display.render
from renpy.display.displayable import Displayable as Displayable
from renpy.display.position import absolute as absolute
from renpy.display.render import render as render
from renpy.object import Object as Object
from renpy.pygame.event import EventType as EventType
from renpy.rollback import NoRollback as NoRollback
from renpy.types import DisplayableLike as DisplayableLike
from typing import Any, Callable, Protocol, type_check_only
from _typeshed import Incomplete as Incomplete

@type_check_only
class ParticleProtocol(Protocol):
    def update(self, st: float) -> tuple[int, int, float, DisplayableLike] | None: ...

@type_check_only
class ParticleFactoryProtocol(Protocol):
    def create(
        self, particles: list[tuple["Sprite", ParticleProtocol]], st: float
    ) -> list["ParticleProtocol"] | None: ...
    def predict(self) -> list[Displayable]: ...

DISTRIBUTION_FUNC_T = Callable[[float, float], float]

def _interpolate(a: float, b: float, step: float) -> float: ...
def linear(a: float, b: float) -> float: ...
def gaussian(a: float, b: float) -> float: ...
def arcsine(a: float, b: float) -> float: ...

distribution_func_map: dict[str, DISTRIBUTION_FUNC_T]

class SpriteCache(renpy.object.Object):
    nosave: list[str]
    child: Displayable | None
    child_copy: Displayable | None
    st: float | None
    render: renpy.display.render.Render | None
    fast: bool

class Sprite(renpy.object.Object):
    x: int | float | absolute
    y: int | float | absolute
    zorder: int | float
    child: Displayable | None
    render: renpy.display.render.Render | None
    live: bool
    manager: SpriteManager | None
    cache: SpriteCache
    def set_child(self, d: DisplayableLike) -> None: ...
    events: bool
    def destroy(self) -> None: ...

class SpriteManager(renpy.display.displayable.Displayable):
    animation: bool
    update_function: Callable[[float], float] | None
    event_function: Callable[[EventType, float, float, float], Any | None] | None
    predict_function: Callable[[], list[Displayable]] | None
    ignore_time: bool
    displayable_map: dict[int, SpriteCache]
    children: list[Sprite]
    dead_child: bool
    events: bool
    width: float | None
    height: float | None
    def __init__(
        self,
        update: Callable[[float], float] | None = None,
        event: Callable[[EventType, float, float, float], Any | None] | None = None,
        predict: Callable[[], list[Displayable]] | None = None,
        ignore_time: bool = False,
        animation: bool = True,
        **properties,
    ) -> None: ...
    _duplicatable: bool
    def _duplicate(self, args: Incomplete) -> SpriteManager: ...
    def create(self, d: DisplayableLike) -> Sprite: ...
    def predict_one(self) -> None: ...
    def redraw(self, delay: int = 0) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def visit(self) -> list[Displayable]: ...
    def destroy_all(self) -> None: ...

class Particles(renpy.display.displayable.Displayable, renpy.rollback.NoRollback):
    __version__: int
    nosave: list[str]
    properties: dict[str, Any]
    sm: SpriteManager
    def after_upgrade(self, version: int) -> None: ...
    particles: list[tuple[Sprite, ParticleProtocol]] | None
    def after_setstate(self) -> None: ...
    factory: ParticleFactoryProtocol
    def __init__(self, factory: ParticleFactoryProtocol, animation: bool = False, **properties) -> None: ...
    _duplicatable: bool
    def _duplicate(self, args: Incomplete) -> Particles: ...
    def update_callback(self, st: float) -> float: ...
    def predict_callback(self) -> list[Displayable]: ...
    def render(self, w: float, h: float, st: float, at: float) -> renpy.display.render.Render: ...
    def visit(self) -> list[Displayable]: ...

class SnowBlossomFactory(ParticleFactoryProtocol, renpy.rollback.NoRollback):
    rotate: bool
    start: int
    def __setstate__(self, state: Incomplete) -> None: ...
    image: Displayable
    count: int
    xspeed: float | tuple[float, float]
    yspeed: float | tuple[float, float]
    border: float
    fast: bool
    distribution: DISTRIBUTION_FUNC_T
    def __init__(
        self,
        image: DisplayableLike,
        count: int,
        xspeed: float | tuple[float, float],
        yspeed: float | tuple[float, float],
        border: float,
        start: float,
        fast: bool,
        rotate: bool = False,
        distribution: DISTRIBUTION_FUNC_T | str = "linear",
    ) -> None: ...
    starts: list[float]
    def init(self) -> None: ...
    def create(
        self, particles: list[tuple[Displayable, "SnowBlossomParticle"]] | None, st: float
    ) -> list["SnowBlossomParticle"] | None: ...
    def predict(self) -> list[Displayable]: ...

class SnowBlossomParticle(ParticleProtocol, renpy.rollback.NoRollback):
    image: Displayable
    xspeed: float
    yspeed: float
    border: float
    start: float
    offset: float
    rotate: bool
    ystart: float
    xstart: float
    def __init__(
        self,
        image: Displayable,
        xspeed: float,
        yspeed: float,
        border: float,
        start: float,
        offset: float,
        fast: bool,
        rotate: bool,
        distribution: DISTRIBUTION_FUNC_T = ...,
    ) -> None: ...
    def update(self, st: float) -> tuple[int, int, float, Displayable] | None: ...

def SnowBlossom(
    d: DisplayableLike,
    count: int = 10,
    border: float = 50,
    xspeed: float | tuple[float, float] = (20, 50),
    yspeed: float | tuple[float, float] = (100, 200),
    start: float = 0,
    fast: bool = False,
    horizontal: bool = False,
    distribution: DISTRIBUTION_FUNC_T | str = "linear",
    animation: bool = False,
) -> Incomplete: ...
