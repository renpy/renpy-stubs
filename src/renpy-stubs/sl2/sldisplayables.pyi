import renpy
from renpy.display.displayable import Displayable as Displayable, Placement as Placement
from renpy.display.layout import Container as Container
from renpy.pygame.event import EventType as EventType
from renpy.sl2.slast import SLContext as SLContext
from renpy.sl2.slparser import (
    DisplayableParser as DisplayableParser,
    Keyword as Keyword,
    Positional as Positional,
    PrefixStyle as PrefixStyle,
    Style as Style,
    add as add,
    many as many,
)
from renpy.sl2.slproperties import (
    bar_properties as bar_properties,
    box_properties as box_properties,
    button_properties as button_properties,
    grid_properties as grid_properties,
    position_properties as position_properties,
    scrollbar_bar_properties as scrollbar_bar_properties,
    scrollbar_position_properties as scrollbar_position_properties,
    side_position_properties as side_position_properties,
    text_position_properties as text_position_properties,
    text_properties as text_properties,
    text_text_properties as text_text_properties,
    viewport_position_properties as viewport_position_properties,
    vscrollbar_bar_properties as vscrollbar_bar_properties,
    vscrollbar_position_properties as vscrollbar_position_properties,
    window_properties as window_properties,
)
from typing import Any

class ShowIf(renpy.display.layout.Container):
    condition: bool | None
    pending_event: str | None
    show_child: bool
    def __init__(self, condition: bool | None, replaces: ShowIf | None = None) -> None: ...
    @property
    def _box_skip(self): ...
    def per_interact(self) -> None: ...
    offsets: list[tuple[int, int]]
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def get_placement(self) -> Placement: ...
    def _tts(self, raw: bool) -> str: ...

def sl2bar(context: SLContext | None = None, **properties) -> renpy.display.behavior.Bar: ...
def sl2vbar(context: SLContext | None = None, **properties) -> renpy.display.behavior.Bar: ...
def sl2viewport(context: SLContext | None = None, **kwargs) -> Displayable: ...
def sl2vpgrid(context: SLContext | None = None, **kwargs) -> Displayable: ...
def sl2add(
    d: renpy.types.DisplayableLike | None,
    replaces: renpy.display.motion.Transform | None = None,
    scope: dict[str, Any] | None = None,
    **kwargs,
) -> renpy.display.motion.Transform | Displayable: ...
