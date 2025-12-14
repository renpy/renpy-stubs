from _typeshed import Incomplete
import renpy

from renpy.display.behavior import map_event as map_event, run as run, run_unhovered as run_unhovered
from renpy.display.core import absolute as absolute
from renpy.display.render import Render as Render, redraw as redraw, render as render

def default_drag_group(): ...
def default_drag_joined(drag): ...
def default_drop_allowable(drop, drags): ...

class Drag(renpy.display.displayable.Displayable, renpy.revertable.RevertableObject):
    z: int
    focusable: bool
    old_position: Incomplete
    drag_offscreen: bool
    activated: Incomplete
    alternate: Incomplete
    dragging: Incomplete
    drag_group_weakref: Incomplete
    click_time: Incomplete
    drag_name: Incomplete
    draggable: Incomplete
    droppable: Incomplete
    drag_raise: Incomplete
    dragged: Incomplete
    dropped: Incomplete
    drop_allowable: Incomplete
    drag_handle: Incomplete
    drag_joined: Incomplete
    clicked: Incomplete
    hovered: Incomplete
    unhovered: Incomplete
    mouse_drop: Incomplete
    child: Incomplete
    x: Incomplete
    y: Incomplete
    w: Incomplete
    h: Incomplete
    parent_width: Incomplete
    parent_height: Incomplete
    target_x: Incomplete
    target_y: Incomplete
    grab_x: Incomplete
    grab_y: Incomplete
    last_x: Incomplete
    last_y: Incomplete
    start_x: int
    start_y: int
    at: int
    target_at: int
    target_at_delay: int
    snap_warper: Incomplete
    snap_start: int
    snap_start_x: int
    snap_start_y: int
    snapping: bool
    snapped: Incomplete
    last_drop: renpy.display.displayable.Displayable | None
    drag_moved: bool
    def __init__(
        self,
        d=None,
        drag_name=None,
        draggable: bool = True,
        droppable: bool = True,
        drag_raise: bool = True,
        dragged=None,
        dropped=None,
        drop_allowable=...,
        drag_handle=(0.0, 0.0, 1.0, 1.0),
        drag_joined=...,
        clicked=None,
        hovered=None,
        unhovered=None,
        replaces=None,
        drag_offscreen: bool = False,
        mouse_drop: bool = False,
        activated=None,
        alternate=None,
        style: str = "drag",
        dragging=None,
        **properties,
    ) -> None: ...
    @property
    def drag_group(self): ...
    @drag_group.setter
    def drag_group(self, value) -> None: ...
    def snap(self, x, y, delay: int = 0, warper=None) -> None: ...
    def set_style_prefix(self, prefix, root) -> None: ...
    def add(self, d) -> None: ...
    def set_child(self, d) -> None: ...
    def top(self) -> None: ...
    def bottom(self) -> None: ...
    def update_style_prefix(self) -> None: ...
    def visit(self): ...
    def focus(self, default: bool = False): ...
    def unfocus(self, default: bool = False) -> None: ...
    def render(self, width, height, st, at): ...
    def get_drag_from_name(self, name): ...
    def event(self, ev, x, y, st): ...
    def get_placement(self): ...
    def per_interact(self) -> None: ...

class DragGroup(renpy.display.layout.MultiBox):
    z_serial: int
    sorted: bool
    min_overlap: Incomplete
    positions: Incomplete
    sensitive: Incomplete
    def __init__(self, *children, **properties) -> None: ...
    def add(self, child) -> None: ...
    def remove(self, child) -> None: ...
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...
    def raise_children(self, l) -> None: ...
    def lower_children(self, l) -> None: ...
    def get_best_drop(self, joined): ...
    def get_drop_at(self, joined, x, y): ...
    def get_children(self): ...
    def get_child_by_name(self, name): ...

def rect_overlap_area(r1, r2): ...
