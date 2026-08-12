from _typeshed import Incomplete
from renpy.display.displayable import DisplayableArguments, Displayable
from renpy.display.layout import MultiBox
from renpy.display.render import Render

class Placeholder(Displayable):
    text: str | None
    child: MultiBox | None
    def after_setstate(self) -> None: ...
    base: str | None
    flip: bool | None
    full: bool
    name: list[str]
    def __init__(
        self,
        base: str | None = None,
        full: bool = False,
        flip: bool | None = None,
        text: str | None = None,
        **properties: Incomplete,
    ) -> None: ...
    def guess_base(self) -> str: ...
    def get_child(self) -> MultiBox: ...
    _duplicatable: bool
    def _duplicate(self, args: DisplayableArguments | None) -> "Placeholder": ...
    def visit(self) -> list[Displayable]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
