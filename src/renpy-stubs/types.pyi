from typing import TYPE_CHECKING, Any, Protocol, Self

import renpy

if TYPE_CHECKING:
    type Unused = Any

    class Duplicatable(Protocol):
        def _duplicate(self, args: renpy.display.displayable.DisplayableArguments) -> Self: ...

type Position = int | float | renpy.display.position.absolute | renpy.display.position.position
type Displayable = renpy.display.displayable.Displayable
type DisplayableLike = Displayable | str | list[str] | renpy.color.Color | Duplicatable
