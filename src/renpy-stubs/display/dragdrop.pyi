import renpy
import weakref
from renpy.display.behavior import (
    ActionType as ActionType,
    map_event as map_event,
    run as run,
    run_unhovered as run_unhovered,
)
from renpy.display.core import absolute as absolute
from renpy.display.displayable import Displayable as Displayable, Placement as Placement
from renpy.display.layout import MultiBox as MultiBox
from renpy.display.render import Render as Render, redraw as redraw, render as render
from renpy.pygame.event import EventType as EventType
from renpy.revertable import RevertableObject as RevertableObject
from renpy.types import DisplayableLike as DisplayableLike
from typing import Any, Callable, Sequence, Literal, Self

type GroupPosition = tuple[float | None, float | None, float | None, float | None, float | None, float | None]

def default_drag_group() -> DragGroup: ...
def default_drag_joined(drag: Drag) -> list[tuple[Drag | str, int, int]]: ...
def default_drop_allowable(drop: Drag, drags: list[Drag]) -> bool: ...

class Drag(renpy.display.displayable.Displayable, renpy.revertable.RevertableObject):
    z: int
    focusable: bool | None
    old_position: GroupPosition | None
    drag_offscreen: bool
    activated: Callable[[list[Drag]], None] | Sequence[Callable[[list[Drag]], None]] | None
    alternate: ActionType
    dragging: Callable[[list[Drag]], Any] | Sequence[Callable[[list[Drag]], Any]] | None
    drag_group_weakref: weakref.ReferenceType[DragGroup] | None
    click_time: float | None
    drag_name: str | None
    draggable: bool
    droppable: bool
    drag_raise: bool
    dragged: Callable[[list[Drag], Drag | None], Any] | Sequence[Callable[[list[Drag], Drag | None], Any]] | None
    dropped: Callable[[Drag | None, list[Drag]], Any] | Sequence[Callable[[Drag | None, list[Drag]], Any]] | None
    drop_allowable: Callable[[Drag, list[Drag]], bool]
    drag_handle: tuple[float, float, float, float]
    drag_joined: Callable[[Drag], list[tuple[Drag | str, int, int]]]
    clicked: Callable[[Drag], Any] | Sequence[Callable[[Drag], Any]] | None
    hovered: ActionType
    unhovered: ActionType
    mouse_drop: bool
    child: Displayable | None
    x: int
    y: int
    w: float
    h: float
    parent_width: int
    parent_height: int
    target_x: int
    target_y: int
    grab_x: int | None
    grab_y: int | None
    last_x: int | None
    last_y: int | None
    start_x: int
    start_y: int
    at: float
    target_at: float
    target_at_delay: int
    snap_warper: Callable[[float], float] | None
    snap_start: float
    snap_start_x: int
    snap_start_y: int
    snapping: bool
    snapped: Callable[[Drag, int, int, bool], Any] | Sequence[Callable[[Drag, int, int, bool], Any]] | None
    last_drop: Drag | None
    drag_moved: bool
    def __init__(
        self,
        d: DisplayableLike | None = None,
        drag_name: str | None = None,
        draggable: bool = True,
        droppable: bool = True,
        drag_raise: bool = True,
        dragged: Callable[[list[Drag], Drag | None], Any]
        | Sequence[Callable[[list[Drag], Drag | None], Any]]
        | None = None,
        dropped: Callable[[Drag | None, list[Drag]], Any]
        | Sequence[Callable[[Drag | None, list[Drag]], Any]]
        | None = None,
        drop_allowable: Callable[[Drag, list[Drag]], bool] = ...,
        drag_handle: tuple[float, float, float, float] = (0.0, 0.0, 1.0, 1.0),
        drag_joined: Callable[[Drag], list[tuple[Drag | str, int, int]]] = ...,
        clicked: Callable[[Drag], Any] | Sequence[Callable[[Drag], Any]] | None = None,
        hovered: ActionType = None,
        unhovered: ActionType = None,
        replaces: Self | None = None,
        drag_offscreen: bool
        | Literal["horizontal", "vertical"]
        | tuple[int, int]
        | tuple[int, int, int, int]
        | Callable[[tuple[int, int]], tuple[int, int]] = False,
        mouse_drop: bool = False,
        activated: Callable[[list[Drag]], None] | Sequence[Callable[[list[Drag]], None]] | None = None,
        alternate: ActionType = None,
        style: str = "drag",
        dragging: Callable[[list[Drag]], Any] | Sequence[Callable[[list[Drag]], Any]] | None = None,
        **properties,
    ) -> None: ...
    @property
    def _draggable(self) -> bool: ...
    @property
    def drag_group(self) -> DragGroup | None: ...
    @drag_group.setter
    def drag_group(self, value: DragGroup | None) -> None: ...
    def snap(self, x: int, y: int, delay: float = 0, warper: Callable[[float], float] | None = None) -> None: ...
    def set_style_prefix(self, prefix: str, root: bool) -> None: ...
    def add(self, d: DisplayableLike) -> None: ...
    def _clear(self) -> None: ...
    def set_child(self, d: DisplayableLike) -> None: ...
    def top(self) -> None: ...
    def bottom(self) -> None: ...
    def update_style_prefix(self) -> None: ...
    def visit(self) -> list[Displayable | None]: ...
    def focus(self, default: bool = False) -> Any | None: ...
    def unfocus(self, default: bool = False) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def get_drag_from_name(self, name: Drag | str) -> Drag: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> None: ...
    def get_placement(self) -> Placement: ...
    def per_interact(self) -> None: ...

class DragGroup(renpy.display.layout.MultiBox):
    z_serial: int
    sorted: bool
    children: list[Drag]
    _list_type = renpy.revertable.RevertableList
    min_overlap: int
    positions: dict[str | None, tuple[int, int, GroupPosition]]
    sensitive: bool
    def __init__(self, *children: Drag, **properties) -> None: ...
    def add(self, child: Drag) -> None: ...
    def remove(self, child: Drag) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> None: ...
    def raise_children(self, l: list[Drag]) -> None: ...
    def lower_children(self, l: list[Drag]) -> None: ...
    def get_best_drop(self, joined: list[Drag]) -> Drag | None: ...
    def get_drop_at(self, joined: list[Drag], x: float, y: float) -> Drag | None: ...
    def get_children(self) -> list[Drag]: ...
    def get_child_by_name(self, name: str) -> Drag | None: ...

def rect_overlap_area(r1: tuple[int, int, int, int], r2: tuple[int, int, int, int]) -> int: ...
