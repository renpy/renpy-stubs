from typing import Any

import renpy

class _ImageMapper:
    idle: renpy.display.displayable.Displayable
    hover: renpy.display.displayable.Displayable
    selected_idle: renpy.display.displayable.Displayable
    selected_hover: renpy.display.displayable.Displayable
    hotspots: dict[str, tuple[int, int, int, int]]
    remaining_hotspots: set[str]
    def __init__(
        self,
        screen: str,
        ground: renpy.display.displayable.Displayable,
        idle: renpy.display.displayable.Displayable | None,
        hover: renpy.display.displayable.Displayable | None,
        selected_idle: renpy.display.displayable.Displayable | None,
        selected_hover: renpy.display.displayable.Displayable | None,
        hotspots: list[tuple[int, int, int, int, str]],
        navigation: bool = True,
        variant: str | None = None,
    ) -> None: ...
    def button(
        self, name: str, clicked: renpy.ui.Action | None, selected: bool, keymap: dict[str, str] = {}
    ) -> tuple[int, int, int, int] | None: ...
    def bar(self, name: str, range: int | float, value: renpy.ui.BarValue, changed: renpy.ui.Action) -> None: ...
    def nothing(self, name: str) -> None: ...
    def close(self) -> None: ...
