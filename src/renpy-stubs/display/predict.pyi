from collections.abc import Generator
from renpy.display.displayable import Displayable as Displayable
from renpy.display.im import ImageBase as ImageBase
from typing import Callable

image: Callable[[ImageBase], None] | None
predicted: set[Displayable]
predicting: bool
screens: list[tuple[str, tuple, dict]]
tlids = list[str | None]

def displayable(d: Displayable | None) -> None: ...
def screen(_screen_name: str, *args, **kwargs) -> None: ...
def reset() -> None: ...
def prediction_coroutine(root_widget: Displayable) -> Generator[bool | None, bool | None, None]: ...
