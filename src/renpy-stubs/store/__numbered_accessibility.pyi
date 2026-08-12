from typing import Any

import renpy

def alt(what: str, interact: bool = True, **kwargs: Any) -> None: ...
def alt_statement_name() -> str: ...

sv = alt
_m1_00accessibility__font_transform_cache: dict[tuple[str, int, int], renpy.text.font.FontGroup] = {}

def _font_transform(font: str, base_font: str, charset: str) -> renpy.text.font.FontGroup: ...
