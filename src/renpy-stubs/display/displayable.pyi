import renpy
from _typeshed import Incomplete
from typing import Any, Callable, TypedDict, Unpack

type Placement = tuple[float | None, float | None, float | None, float | None, float | None, float | None, bool]

def place(width: float, height: float, sw: float, sh: float, placement: Placement) -> tuple[float, float]: ...

class DisplayableArguments(renpy.object.Object):
    name: tuple[str, ...]
    args: tuple[str, ...]
    prefix: str | None
    lint: bool
    class _DisplayableArguments(TypedDict, total=False):
        name: tuple[str, ...]
        args: tuple[str, ...]
        prefix: str | None
        lint: bool

    def copy(self, **kwargs: Unpack[_DisplayableArguments]) -> DisplayableArguments: ...
    def extraneous(self) -> None: ...

default_style: Incomplete

class Displayable(renpy.object.Object):
    focusable: bool | None
    full_focus_name: tuple[str, int] | None
    role: str
    transform_event: str | None
    transform_event_responder: bool
    delay: float | None
    id: str | None
    def __ne__(self, o): ...
    style: Incomplete
    focus_name: Incomplete
    default: Incomplete
    def __init__(
        self,
        focus: str | None = None,
        default: bool = False,
        style: str = "default",
        _args: DisplayableArguments | None = None,
        tooltip: Any | None = None,
        default_focus: bool = False,
        **properties: Any,
    ) -> None: ...
    def parameterize(self, name, parameters): ...
    def find_focusable(self, callback: Callable[[Displayable | None, str], None], focus_name: str): ...
    def focus(self, default: bool = False): ...
    def unfocus(self, default: bool = False): ...
    def is_focused(self) -> bool: ...
    def set_style_prefix(self, prefix: str, root: bool): ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def event(self, ev: renpy.pygame.event.EventType, x: int, y: int, st: float) -> Any | None: ...
    def get_placement(self) -> Placement: ...
    def visit_all(self, callback: Callable[[Displayable], None], seen: set[int] | None = None): ...
    def visit(self) -> list[Displayable | None]: ...
    def per_interact(self) -> None: ...
    def predict_one(self) -> None: ...
    def predict_one_action(self) -> None: ...
    def place(
        self,
        dest: renpy.display.render.Render | None,
        x: float,
        y: float,
        width: float,
        height: float,
        surf: renpy.display.render.Render,
        main: bool = True,
    ) -> tuple[float, float]: ...
    def set_transform_event(self, event: str): ...
