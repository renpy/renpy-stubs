import renpy as renpy
import threading as threading
from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete as Incomplete
from renpy.display.displayable import Displayable as Displayable
from renpy.display.matrix import Matrix as Matrix, Matrix2D as Matrix2D
from renpy.display.screen import ScreenDisplayable as ScreenDisplayable
from renpy.pygame.event import EventType as EventType
from renpy.pygame.surface import Surface as Surface
from renpy.color import Color as Color, ColorLike
from typing import Any, Sequence, Callable

type Rect = renpy.pygame.rect.Rect
type RectLike = renpy.pygame.rect.RectLike

type FocusTuple = tuple[
    Displayable,
    Any,
    int | None,
    int | None,
    int | None,
    int | None,
    int | None,
    Incomplete | Render | None,  # mask
]
Modal: renpy.object.Sentinel

class Canvas:
    def __init__(self, surf: Surface) -> None: ...
    def aaline(self, color: Color, startpos: tuple[int, int], endpos: tuple[int, int], blend: int = 1) -> None: ...
    def aalines(self, color: Color, closed: bool, pointlist: Sequence[tuple[int, int]], blend: int = 1) -> None: ...
    def arc(
        self, color: Color, rect: tuple[int, int, int, int], start_angle: float, stop_angle: float, width: int = 1
    ) -> None: ...
    def circle(self, color: Color, pos: tuple[int, int], radius: int, width: int = 0) -> None: ...
    def ellipse(self, color: Color, rect: tuple[int, int, int, int], width: int = 0) -> None: ...
    def get_surface(self) -> Surface: ...
    def line(self, color: Color, start_pos: tuple[int, int], end_pos: tuple[int, int], width: int = 1) -> None: ...
    def lines(self, color: Color, closed: bool, pointlist: Sequence[tuple[int, int]], width: int = 1) -> None: ...
    def polygon(self, color: Color, pointlist: Sequence[tuple[int, int]], width: int = 0) -> None: ...
    def rect(self, color: Color, rect: tuple[int, int, int, int], width: int = 0) -> None: ...

class Render:
    def __init__(self, width: float, height: float, layer_name: str | None = None) -> None: ...
    def __getstate__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: Incomplete) -> None: ...
    def absolute_blit(
        self,
        source: "Render | Surface",
        pos: tuple[float, float],
        focus: bool = True,
        main: bool = True,
        index: int | None = None,
    ) -> int: ...
    def add_focus(
        self,
        d: Displayable,
        arg: Any = None,
        x: int | None = 0,
        y: int | None = 0,
        w: int | None = None,
        h: int | None = None,
        mx: int | None = None,
        my: int | None = None,
        mask: Incomplete | Render | None = None,
    ) -> None: ...
    def add_property(self, name: str, value: Any) -> None: ...
    def add_shader(self, shader: str) -> None: ...
    def add_uniform(self, name: str, value: Any) -> None: ...
    def blit(
        self,
        source: "Render | Surface",
        pos: RectLike,
        focus: bool = True,
        main: bool = True,
        index: int | None = None,
    ) -> int: ...
    def canvas(self) -> "Canvas": ...
    def compute_subline(self, sx: int, sw: int, cx: int, cw: int, bx: int, bw: int) -> tuple[int, int, int]: ...
    def depends_on(self, source: "Render", focus: bool = False) -> None: ...
    def fill(self, color: ColorLike) -> None: ...
    def focus_at_point(
        self, x: int, y: int, screen: ScreenDisplayable | None
    ) -> tuple[Displayable, Any, ScreenDisplayable | None] | Modal | None: ...
    def get_property(self, name: str, default: Any) -> Any: ...
    def get_size(self) -> tuple[float, float]: ...
    def is_fully_transparent(self) -> bool: ...
    def is_pixel_opaque(self, x: int, y: int) -> bool: ...
    def kill(self) -> None: ...
    def kill_cache(self) -> None: ...
    def main_displayables_at_point(
        self, x: int, y: int, layers: Sequence[str], depth: int | None = None
    ) -> list[tuple[int, int, int, Displayable]]: ...
    def place(
        self,
        d: Displayable,
        x: int = 0,
        y: int = 0,
        width: int | None = None,
        height: int | None = None,
        st: float | None = None,
        at: float | None = None,
        render: "Render | None" = None,
        main: bool = True,
    ) -> tuple[float, float]: ...
    def pygame_surface(self, alpha: bool = True) -> Surface: ...
    def render_to_texture(self, alpha: bool = True) -> Surface: ...
    def screen_rect(self, sx: float, sy: float, transform: Matrix) -> tuple[int, int, int, int]: ...
    def subpixel_blit(
        self,
        source: "Render | Surface",
        pos: tuple[float, float],
        focus: bool = True,
        main: bool = True,
        index: int | None = None,
    ) -> int: ...
    def subsurface(
        self,
        rect: tuple[float, float, float, float],
        focus: bool = False,
        subpixel: bool = False,
        bounds: tuple[int, int, int, int] | None = None,
    ) -> "Render": ...
    def take_focuses(
        self,
        cminx: int,
        cminy: int,
        cmaxx: int,
        cmaxy: int,
        transform: renpy.display.matrix.Matrix,
        screen: ScreenDisplayable | None,
        focuses: list[renpy.display.focus.Focus],
    ) -> None: ...
    def zoom(self, xzoom: float, yzoom: float) -> None: ...
    mark: bool
    cache_killed: bool
    killed: bool
    width: float
    height: float
    layer_name: str | None
    children: list[tuple["Render | Surface", float, float, bool, bool]]
    forward: renpy.display.matrix.Matrix | None
    reverse: renpy.display.matrix.Matrix | None
    alpha: float
    over: float
    nearest: bool | None
    focuses: list[renpy.display.focus.Focus] | None
    pass_focuses: list[Render] | None
    focus_screen: ScreenDisplayable | None
    render_of: list[renpy.display.core.Displayable]
    xclipping: bool
    yclipping: bool
    modal: bool | str | Callable[[EventType | None, float, float, float | None, float | None], bool] | None
    text_input: bool
    parents: set[Render]
    depends_on_list: list[Render]
    operation: int
    operation_complete: float
    operation_alpha: bool
    operation_parameter: int
    surface: Surface
    alpha_surface: Surface
    half_cache: Incomplete | None
    mesh: Incomplete | None
    shaders: tuple[str, ...] | None
    uniforms: dict[str, Any] | None
    properties: dict[str, Any] | None
    cached_texture: Incomplete | None
    cached_model: Incomplete | None
    loaded: bool
    uniforms_has_render: bool

def adjust_render_cache_times(old_time: float, new_time: float) -> None: ...
def check_at_shutdown() -> None: ...
def check_redraws() -> bool: ...
def focus_at_point(x: float, y: float) -> renpy.display.focus.Focus | None: ...
def free_memory() -> None: ...
def invalidate(d: Displayable) -> None: ...
def mark_sweep() -> None: ...
def mutated_surface(surf: Surface) -> None: ...
def process_redraws() -> bool: ...
def redraw_time() -> float | None: ...
def redraw(d: Displayable, when: float) -> None: ...
def render_for_size(d: Displayable, width: int, height: int, st: float, at: float) -> "Render": ...
def render_ready() -> None: ...
def render_screen(root: Displayable, width: int, height: int) -> "Render": ...
def render(d: Displayable, widtho: float, heighto: float, st: float, at: float) -> "Render": ...
def take_focuses(focuses: list[renpy.display.focus.Focus]) -> None: ...

screen_render: Render | None
IDENTITY: renpy.display.matrix.Matrix
blit_lock: threading.Condition
BLIT: int
DISSOLVE: int
FLATTEN: int
IMAGEDISSOLVE: int
PIXELLATE: int
models: int
per_frame: int
render_height: int
render_width: int
sizing: int
