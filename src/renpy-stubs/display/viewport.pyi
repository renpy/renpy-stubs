from _typeshed import Incomplete
import renpy

def edgescroll_proportional(n): ...

class Viewport(renpy.display.layout.Container):
    __version__: int
    arrowkeys: bool
    pagekeys: bool
    drag_position_time: Incomplete
    xadjustment: Incomplete
    yadjustment: Incomplete
    set_adjustments: bool
    mousewheel: bool
    draggable: bool
    width: int
    height: int
    drag_position: Incomplete
    edge_size: bool
    edge_speed: bool
    edge_function: Incomplete
    edge_xspeed: int
    edge_yspeed: int
    edge_last_st: Incomplete
    focusable: Incomplete
    def after_upgrade(self, version) -> None: ...
    xoffset: Incomplete
    yoffset: Incomplete
    drag_speed: Incomplete
    def __init__(
        self,
        child=None,
        child_size=(None, None),
        offsets=(None, None),
        xadjustment=None,
        yadjustment=None,
        set_adjustments: bool = True,
        mousewheel: bool = False,
        draggable: bool = False,
        edgescroll=None,
        style: str = "viewport",
        xinitial=None,
        yinitial=None,
        replaces=None,
        arrowkeys: bool = False,
        pagekeys: bool = False,
        **properties,
    ) -> None: ...
    def per_interact(self) -> None: ...
    def set_style_prefix(self, prefix, root) -> None: ...
    def update_offsets(self, cw, ch, st): ...
    offsets: Incomplete
    def render(self, width, height, st, at): ...
    def check_edge_redraw(self, st, reset_st: bool = True) -> None: ...
    def event(self, ev, x, y, st): ...
    def set_xoffset(self, offset) -> None: ...
    def set_yoffset(self, offset) -> None: ...

class VPGrid(Viewport):
    __version__: Incomplete
    allow_underfull: Incomplete
    grid_cols: Incomplete
    grid_rows: Incomplete
    grid_transpose: Incomplete
    def __init__(
        self, cols=None, rows=None, transpose=None, style: str = "vpgrid", allow_underfull=None, **properties
    ) -> None: ...
    width: Incomplete
    height: Incomplete
    offsets: Incomplete
    def render(self, width, height, st, at): ...
    def add(self, d) -> None: ...
    def per_interact(self) -> None: ...
