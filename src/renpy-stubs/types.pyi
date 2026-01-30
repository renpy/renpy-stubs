import renpy
from typing import Any, Protocol, Self

type Unused = Any
type Position = int | float | renpy.display.position.absolute | renpy.display.position.position

class Duplicatable(Protocol):
    def _duplicate(self, args: renpy.display.displayable.DisplayableArguments) -> Self: ...

type Displayable = renpy.display.displayable.Displayable
type DisplayableLike = Displayable | str | list[str] | renpy.color.Color | Duplicatable
