from typing import Any

import renpy
from renpy.display.displayable import Displayable as Displayable
from renpy.display.displayable import Placement as Placement
from renpy.display.layout import Container as Container
from renpy.pygame.event import EventType as EventType
from renpy.sl2.slast import SLContext as SLContext
from renpy.sl2.slparser import DisplayableParser as DisplayableParser
from renpy.sl2.slparser import Keyword as Keyword
from renpy.sl2.slparser import Positional as Positional
from renpy.sl2.slparser import PrefixStyle as PrefixStyle
from renpy.sl2.slparser import Style as Style
from renpy.sl2.slparser import add as add
from renpy.sl2.slparser import many as many
from renpy.sl2.slproperties import bar_properties as bar_properties
from renpy.sl2.slproperties import box_properties as box_properties
from renpy.sl2.slproperties import button_properties as button_properties
from renpy.sl2.slproperties import grid_properties as grid_properties
from renpy.sl2.slproperties import position_properties as position_properties
from renpy.sl2.slproperties import scrollbar_bar_properties as scrollbar_bar_properties
from renpy.sl2.slproperties import scrollbar_position_properties as scrollbar_position_properties
from renpy.sl2.slproperties import side_position_properties as side_position_properties
from renpy.sl2.slproperties import text_position_properties as text_position_properties
from renpy.sl2.slproperties import text_properties as text_properties
from renpy.sl2.slproperties import text_text_properties as text_text_properties
from renpy.sl2.slproperties import viewport_position_properties as viewport_position_properties
from renpy.sl2.slproperties import vscrollbar_bar_properties as vscrollbar_bar_properties
from renpy.sl2.slproperties import vscrollbar_position_properties as vscrollbar_position_properties
from renpy.sl2.slproperties import window_properties as window_properties

class ShowIf(renpy.display.layout.Container):
    condition: bool | None
    pending_event: str | None
    show_child: bool
    def __init__(self, condition: bool | None, replaces: ShowIf | None = None) -> None: ...
    @property
    def _box_skip(self) -> bool: ...
    def per_interact(self) -> None: ...
    offsets: list[tuple[int, int]]
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...
    def get_placement(self) -> Placement: ...
    def _tts(self, raw: bool) -> str: ...

def sl2bar(context: SLContext | None = None, **properties: Any) -> renpy.display.behavior.Bar: ...
def sl2vbar(context: SLContext | None = None, **properties: Any) -> renpy.display.behavior.Bar: ...
def sl2viewport(context: SLContext | None = None, **kwargs: Any) -> Displayable: ...
def sl2vpgrid(context: SLContext | None = None, **kwargs: Any) -> Displayable: ...
def sl2add(
    d: renpy.types.DisplayableLike | None,
    replaces: renpy.display.motion.Transform | None = None,
    scope: dict[str, Any] | None = None,
    **kwargs: Any,
) -> renpy.display.motion.Transform | Displayable: ...
