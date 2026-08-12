import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.displayable import Displayable as Displayable
from renpy.types import DisplayableLike as DisplayableLike
from typing import Any, Literal, Self

UniformValue = (
    float
    | tuple[float, float]
    | tuple[float, float, float]
    | tuple[float, float, float, float]
    | renpy.display.matrix.Matrix
)

class Texture:
    texture_wrap: Incomplete | None
    displayable: Displayable
    focus: bool
    main: bool
    fit: bool
    def __init__(
        self, displayable: DisplayableLike, focus: bool, main: bool, fit: bool, texture_wrap: Incomplete | None = None
    ) -> None: ...
    def _in_current_store(self) -> Texture: ...

class Model(renpy.display.displayable.Displayable):
    size: tuple[float, float] | None
    textures: list[Texture]
    _mesh: tuple[Literal["grid"], int, int] | None
    shaders: list[str]
    uniforms: dict[str, UniformValue]
    properties: dict[str, Any]
    def __init__(self, size: tuple[float, float] | None = None, **properties) -> None: ...
    def grid_mesh(self, width: int, height: int) -> Self: ...
    def texture(
        self,
        displayable: DisplayableLike,
        focus: bool = False,
        main: bool = False,
        fit: bool = False,
        texture_wrap: Incomplete | None = None,
    ) -> Self: ...
    def child(self, displayable: DisplayableLike, fit: bool = False) -> Self: ...
    def shader(self, shader: str) -> Self: ...
    def uniform(self, name: str, value: UniformValue) -> Self: ...
    def property(self, name: str, value: Any) -> Self: ...
    def _handles_event(self, event: str) -> bool: ...
    def set_style_prefix(self, prefix: str, root: bool) -> None: ...
    def _in_current_store(self) -> Model: ...
    def visit(self) -> list[Displayable]: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
