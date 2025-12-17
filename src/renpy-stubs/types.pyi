import renpy
from typing import Any

type Unused = Any
type Displayable = renpy.display.displayable.Displayable
type DisplayableLike = Displayable | str | list[str] | renpy.color.Color
type Position = int | float | renpy.display.position.absolute | renpy.display.position.position
