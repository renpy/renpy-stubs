from renpy.exports.commonexports import renpy_pure as renpy_pure
from typing import Any, Literal

def get_menu_args() -> tuple[tuple[Any, ...], dict[str, Any] | None]: ...
def menu(
    items: list[tuple[str, str, Any]],
    set_expr: str | None,
    args: tuple[Any, ...] | None = None,
    kwargs: dict[str, Any] | None = None,
    item_arguments: list[tuple[tuple[Any, ...], dict[str, Any]]] | None = None,
) -> Any: ...
def choice_for_skipping() -> None: ...
def predict_menu() -> None: ...

class MenuEntry(tuple): ...

def display_menu(
    items: list[tuple[str, Any]],
    window_style: str = "menu_window",
    interact: bool = True,
    with_none: bool | None = None,
    caption_style: str = "menu_caption",
    choice_style: str = "menu_choice",
    choice_chosen_style: str = "menu_choice_chosen",
    choice_button_style: str = "menu_choice_button",
    choice_chosen_button_style: str = "menu_choice_chosen_button",
    scope: dict[str, Any] = (),
    widget_properties: dict[str, Any] | None = None,
    screen: str = "choice",
    type: Literal["menu", "nvl"] = "menu",
    predict_only: bool = False,
    _layer: str | None = None,
    _args: tuple[Any, ...] | None = None,
    _kwargs: dict[str, Any] | None = None,
    **kwargs,
) -> Any: ...
