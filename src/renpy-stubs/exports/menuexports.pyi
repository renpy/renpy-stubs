from renpy.exports.commonexports import renpy_pure as renpy_pure
from _typeshed import Incomplete as Incomplete

def get_menu_args() -> Incomplete: ...
def menu(
    items: Incomplete,
    set_expr: Incomplete,
    args: Incomplete = None,
    kwargs: Incomplete = None,
    item_arguments: Incomplete = None,
) -> Incomplete: ...
def choice_for_skipping() -> None: ...
def predict_menu() -> None: ...

class MenuEntry(tuple): ...

def display_menu(
    items: Incomplete,
    window_style: str = "menu_window",
    interact: bool = True,
    with_none: Incomplete = None,
    caption_style: str = "menu_caption",
    choice_style: str = "menu_choice",
    choice_chosen_style: str = "menu_choice_chosen",
    choice_button_style: str = "menu_choice_button",
    choice_chosen_button_style: str = "menu_choice_chosen_button",
    scope: Incomplete = (),
    widget_properties: Incomplete = None,
    screen: str = "choice",
    type: str = "menu",
    predict_only: bool = False,
    _layer: Incomplete = None,
    _args: Incomplete = None,
    _kwargs: Incomplete = None,
    **kwargs,
) -> Incomplete: ...
