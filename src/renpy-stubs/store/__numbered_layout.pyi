from collections.abc import Callable, Sequence
from typing import Any, NoReturn

import renpy
from renpy.curry import Partial
from renpy.display.behavior import ActionType, Button

class Layout:
    def __call__(self, func: Callable) -> Callable: ...
    @staticmethod
    def provides(kind: str) -> None: ...
    @staticmethod
    def defaults() -> None: ...
    @staticmethod
    def button(
        label: str,
        type: str | None = None,
        selected: bool = False,
        enabled: bool = True,
        clicked: ActionType | None = None,
        hovered: ActionType | None = None,
        unhovered: ActionType | None = None,
        index: str | None = None,
        **properties: Any,
    ) -> Button: ...
    @staticmethod
    def label(label: str, type: str, suffix: str = "label", index: str | None = None, **properties: Any) -> None: ...
    @staticmethod
    def prompt(label: str, type: str, index: str | None = None, **properties: Any) -> None: ...
    @staticmethod
    def list(
        entries: Sequence[tuple[int, str]],
        clicked: ActionType | None = None,
        hovered: ActionType | None = None,
        unhovered: ActionType | None = None,
        selected: int | None = None,
        **properties: Any,
    ) -> None: ...
    @staticmethod
    def button_menu() -> None: ...
    # def compat() -> None: ...
    # def classic_main_menu() -> None: ...
    # def classic_navigation() -> None: ...
    # def classic_load_save() -> None: ...
    # def classic_yesno_prompt() -> None: ...
    # def classic_preferences(center: bool = False) -> None: ...
    # def classic_joystick_preferences() -> None: ...
    # def two_column_preferences() -> None: ...
    # def one_column_preferences() -> None: ...
    # def grouped_main_menu(per_group: int = 2, equal_size: bool = True) -> None: ...
    # def grouped_navigation(per_group: int = 2, equal_size: bool = True) -> None: ...
    # def scrolling_load_save() -> None: ...
    # def imagemap_main_menu(
    #         ground: str,
    #         selected: str,
    #         hotspots: list[tuple[int, int, int, int, str | None]],
    #         idle: str | None = None,
    #         variant: str | None = None
    #     ) -> None: ...
    # def imagemap_navigation(
    #         ground: str,
    #         idle: str | None = None,
    #         hover: str,
    #         selected_idle: str,
    #         selected_hover: str,
    #         hotspots: list[tuple[int, int, int, int, str | None]]
    #     ) -> None: ...
    # def imagemap_preferences(
    #         ground: str,
    #         idle: str | None = None,
    #         hover: str,
    #         selected_idle: str,
    #         selected_hover: str,
    #         hotspots: list[tuple[int, int, int, int, str | None]]
    #     ) -> None: ...
    # def imagemap_yesno_prompt(
    #         ground: str,
    #         idle: str | None = None,
    #         hover: str,
    #         hotspots: list[tuple[int, int, int, int, str | None]],
    #         prompt_images: dict[str, str] = {}
    #     ) -> None: ...
    # def imagemap_load_save(
    #         ground: str,
    #         idle: str | None = None,
    #         hover: str,
    #         selected_idle: str,
    #         selected_hover: str,
    #         hotspots: list[tuple[int, int, int, int, str | None]],
    #         variant: str | None = None
    #     ) -> None: ...
    # def screen_main_menu() -> None: ...
    # def screen_load_save() -> None: ...
    # def screen_preferences() -> None: ...
    # def screen_joystick_preferences() -> None: ...
    # def screen_yesno_prompt() -> None: ...
    ARE_YOU_SURE: str
    DELETE_SAVE: str
    OVERWRITE_SAVE: str
    LOADING: str
    QUIT: str
    MAIN_MENU: str
    CONTINUE: str
    END_REPLAY: str
    SLOW_SKIP: str
    FAST_SKIP_SEEN: str
    FAST_SKIP_UNSEEN: str
    @staticmethod
    def invoke_yesno_prompt(
        message: str, yes: ActionType | None = None, no: ActionType | None = None, **kwargs: Any
    ) -> None: ...
    @staticmethod
    def yesno_screen(
        message: str, yes: ActionType | None = None, no: ActionType | None = None, **kwargs: Any
    ) -> None: ...
    @staticmethod
    def __auto_save_extra_info() -> str: ...
    # store._button_menu = button_menu

layout: Layout
_layout: Layout

def _intra_jumps_core(label: renpy.ast.NodeName, transition: str) -> NoReturn: ...

_intra_jumps: Partial[Partial[NoReturn]]
