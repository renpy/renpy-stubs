from _typeshed import Incomplete
from typing import Callable, NoReturn, Sequence

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
        **properties: Incomplete,
    ) -> Button: ...
    @staticmethod
    def label(
        label: str, type: str, suffix: str = "label", index: str | None = None, **properties: Incomplete
    ) -> None: ...
    @staticmethod
    def prompt(label: str, type: str, index: str | None = None, **properties: Incomplete) -> None: ...
    @staticmethod
    def list(
        entries: Sequence[tuple[int, str]],
        clicked: ActionType | None = None,
        hovered: ActionType | None = None,
        unhovered: ActionType | None = None,
        selected: int | None = None,
        **properties: Incomplete,
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
    #         ground: Incomplete,
    #         selected: Incomplete,
    #         hotspots: Incomplete,
    #         idle: Incomplete = None,
    #         variant: Incomplete = None
    #     ) -> None: ...
    # def imagemap_navigation(
    #         ground: Incomplete,
    #         idle: Incomplete,
    #         hover: Incomplete,
    #         selected_idle: Incomplete,
    #         selected_hover: Incomplete,
    #         hotspots: Incomplete
    #     ) -> None: ...
    # def imagemap_preferences(
    #         ground: Incomplete,
    #         idle: Incomplete,
    #         hover: Incomplete,
    #         selected_idle: Incomplete,
    #         selected_hover: Incomplete,
    #         hotspots: Incomplete
    #     ) -> None: ...
    # def imagemap_yesno_prompt(
    #         ground: Incomplete,
    #         idle: Incomplete,
    #         hover: Incomplete,
    #         hotspots: Incomplete,
    #         prompt_images: Incomplete = { }
    #     ) -> None: ...
    # def imagemap_load_save(
    #         ground: Incomplete,
    #         idle: Incomplete,
    #         hover: Incomplete,
    #         selected_idle: Incomplete,
    #         selected_hover: Incomplete,
    #         hotspots: Incomplete,
    #         variant: Incomplete = None
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
        message: str, yes: ActionType = None, no: ActionType = None, **kwargs: Incomplete
    ) -> None: ...
    @staticmethod
    def yesno_screen(message: str, yes: ActionType = None, no: ActionType = None, **kwargs: Incomplete) -> None: ...
    @staticmethod
    def __auto_save_extra_info() -> str: ...
    # store._button_menu = button_menu

layout: Layout
_layout: Layout

def _intra_jumps_core(label: renpy.ast.NodeName, transition: str) -> NoReturn: ...

_intra_jumps: Partial[Partial[NoReturn]]
