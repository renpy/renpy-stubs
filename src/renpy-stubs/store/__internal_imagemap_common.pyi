from _typeshed import Incomplete

class _ImageMapper:
    idle: Incomplete
    hover: Incomplete
    selected_idle: Incomplete
    selected_hover: Incomplete
    hotspots: Incomplete
    remaining_hotspots: Incomplete
    def __init__(
        self,
        screen: Incomplete,
        ground: Incomplete,
        idle: Incomplete,
        hover: Incomplete,
        selected_idle: Incomplete,
        selected_hover: Incomplete,
        hotspots: Incomplete,
        navigation: bool = True,
        variant: Incomplete = None,
    ) -> None: ...
    def button(
        self, name: Incomplete, clicked: Incomplete, selected: Incomplete, keymap: Incomplete = {}
    ) -> Incomplete: ...
    def bar(self, name: Incomplete, range: Incomplete, value: Incomplete, changed: Incomplete) -> None: ...
    def nothing(self, name: Incomplete) -> None: ...
    def close(self) -> None: ...
