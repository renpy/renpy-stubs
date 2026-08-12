from typing import Any

import renpy

_side_image_tag: str | None
_side_image_old: tuple | None
_side_image_raw: tuple | None
_side_image: Any
_side_image_prefix_tag: str

def _side_per_interact() -> None: ...
def SideImage(prefix_tag: str | None = None) -> renpy.display.displayable.Displayable: ...
def HasSideImage() -> bool: ...
