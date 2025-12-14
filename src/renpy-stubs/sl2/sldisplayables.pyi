from _typeshed import Incomplete

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

class ShowIf(renpy.display.layout.Container):
    condition: Incomplete
    pending_event: str
    show_child: Incomplete
    def __init__(self, condition, replaces=None) -> None: ...
    def per_interact(self) -> None: ...
    offsets: Incomplete
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...
    def get_placement(self): ...

def sl2bar(context=None, **properties): ...
def sl2vbar(context=None, **properties): ...
def sl2viewport(context=None, **kwargs): ...
def sl2vpgrid(context=None, **kwargs): ...
def sl2add(d, replaces=None, scope=None, **kwargs): ...
