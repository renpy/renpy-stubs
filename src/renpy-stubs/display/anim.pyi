import renpy
from _typeshed import Incomplete as Incomplete
from renpy.curry import Partial as Partial
from renpy.display.displayable import Displayable as Displayable
from renpy.display.transition import Transition as Transition
from renpy.types import DisplayableLike as DisplayableLike
from typing import Callable

class State:
    name: str
    image: Displayable | None
    atlist: Callable[[Displayable | Incomplete], Displayable | Incomplete]
    properties: Incomplete
    def __init__(
        self,
        name: str,
        image: DisplayableLike | None,
        *atlist: Callable[[Displayable | Incomplete], Displayable | Incomplete],
        **properties,
    ) -> None: ...
    def add(self, sma: SMAnimation) -> None: ...
    def get_image(self) -> Displayable: ...
    def motion_copy(self, child: DisplayableLike | None) -> State: ...

class Edge:
    old: str
    delay: float
    new: str
    trans: Callable[..., Transition] | None
    prob: int
    def __init__(
        self, old: str, delay: float, new: str, trans: Callable[..., Transition] | None = None, prob: int = 1
    ) -> None: ...
    def add(self, sma: SMAnimation) -> None: ...

class SMAnimation(renpy.display.displayable.Displayable):
    delay: float | None
    showold: bool
    anim_timebase: bool
    properties: Incomplete
    initial: str
    states: dict[str, State]
    edges: dict[str, list[Edge]]
    edge_start: float | None
    edge_cache: Displayable | None
    edge: Edge | None
    state: str | None
    def __init__(self, initial: str, *args: Edge, **properties) -> None: ...
    def visit(self) -> list[Displayable | None]: ...
    def pick_edge(self, state: str) -> None: ...
    def update_cache(self) -> None: ...
    def get_placement(self) -> Incomplete: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def __call__(
        self,
        child: DisplayableLike | None = None,
        new_widget: Displayable | None = None,
        old_widget: Displayable | None = None,
    ) -> SMAnimation: ...

def Animation(*args, **kwargs) -> TransitionAnimation: ...

class TransitionAnimation(renpy.display.displayable.Displayable):
    anim_timebase: bool
    images: list[Displayable]
    prev_images: list[Displayable]
    delays: list[float]
    transitions: list[Callable[..., Transition] | None]
    def __init__(self, *args: DisplayableLike | float | Callable[..., Transition] | None, **properties) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render | None: ...
    def visit(self) -> list[Displayable]: ...

class Blink(renpy.display.displayable.Displayable):
    image: Displayable
    on: float
    off: float
    rise: float
    set: float
    high: float
    low: float
    offset: float
    anim_timebase: bool
    cycle: float
    def __init__(
        self,
        image: DisplayableLike,
        on: float = 0.5,
        off: float = 0.5,
        rise: float = 0.5,
        set: float = 0.5,
        high: float = 1.0,
        low: float = 0.0,
        offset: float = 0.0,
        anim_timebase: bool = False,
        **properties,
    ) -> None: ...
    def visit(self) -> list[Displayable]: ...
    def render(self, height, width, st, at) -> Incomplete: ...

def Filmstrip(
    image: DisplayableLike,
    framesize: tuple[float, float],
    gridsize: tuple[int, int],
    delay: float,
    frames: int | None = None,
    loop: bool = True,
    **properties,
) -> Incomplete: ...
