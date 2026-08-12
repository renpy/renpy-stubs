from collections.abc import Generator
from typing import Callable, Any

import renpy
from renpy.display.displayable import Displayable as Displayable
from renpy.display.im import ImageBase as ImageBase

image: Callable[[ImageBase], None] | None
predicted: set[Displayable]
predicting: bool
screens: list[tuple[str, tuple, dict]]
tlids = list[str | None]

def displayable(d: Displayable | None) -> None: ...
def screen(_screen_name: str, *args: Any, **kwargs: Any) -> None: ...
def reset() -> None: ...
def prediction_coroutine(root_widget: Displayable) -> Generator[bool | None, bool | None, None]: ...

statement: renpy.ast.Node | None
