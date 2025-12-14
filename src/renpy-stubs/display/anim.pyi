from _typeshed import Incomplete

class State:
    name: Incomplete
    image: Incomplete
    atlist: Incomplete
    properties: Incomplete
    def __init__(self, name, image, *atlist, **properties) -> None: ...
    def add(self, sma) -> None: ...
    def get_image(self): ...
    def motion_copy(self, child): ...

class Edge:
    old: Incomplete
    delay: Incomplete
    new: Incomplete
    trans: Incomplete
    prob: Incomplete
    def __init__(self, old, delay, new, trans=None, prob: int = 1) -> None: ...
    def add(self, sma) -> None: ...

class SMAnimation(renpy.display.displayable.Displayable):
    delay: Incomplete
    showold: Incomplete
    anim_timebase: Incomplete
    properties: Incomplete
    initial: Incomplete
    states: Incomplete
    edges: Incomplete
    edge_start: Incomplete
    edge_cache: Incomplete
    edge: Incomplete
    state: Incomplete
    def __init__(self, initial, *args, **properties) -> None: ...
    def visit(self): ...
    def pick_edge(self, state) -> None: ...
    def update_cache(self) -> None: ...
    def get_placement(self): ...
    def render(self, width, height, st, at): ...
    def __call__(self, child=None, new_widget=None, old_widget=None): ...

def Animation(*args, **kwargs): ...

class TransitionAnimation(renpy.display.displayable.Displayable):
    anim_timebase: Incomplete
    images: Incomplete
    prev_images: Incomplete
    delays: Incomplete
    transitions: Incomplete
    def __init__(self, *args, **properties) -> None: ...
    def render(self, width, height, st, at): ...
    def visit(self): ...

class Blink(renpy.display.displayable.Displayable):
    image: Incomplete
    on: Incomplete
    off: Incomplete
    rise: Incomplete
    set: Incomplete
    high: Incomplete
    low: Incomplete
    offset: Incomplete
    anim_timebase: Incomplete
    cycle: Incomplete
    def __init__(
        self,
        image,
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
    def visit(self): ...
    def render(self, height, width, st, at): ...

def Filmstrip(image, framesize, gridsize, delay, frames=None, loop: bool = True, **properties): ...
