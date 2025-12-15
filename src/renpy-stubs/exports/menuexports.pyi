from renpy.exports.commonexports import renpy_pure as renpy_pure

def get_menu_args(): ...
def menu(items, set_expr, args=None, kwargs=None, item_arguments=None): ...
def choice_for_skipping() -> None: ...
def predict_menu() -> None: ...

class MenuEntry(tuple): ...

def display_menu(
    items,
    window_style: str = "menu_window",
    interact: bool = True,
    with_none=None,
    caption_style: str = "menu_caption",
    choice_style: str = "menu_choice",
    choice_chosen_style: str = "menu_choice_chosen",
    choice_button_style: str = "menu_choice_button",
    choice_chosen_button_style: str = "menu_choice_chosen_button",
    scope=(),
    widget_properties=None,
    screen: str = "choice",
    type: str = "menu",
    predict_only: bool = False,
    _layer=None,
    _args=None,
    _kwargs=None,
    **kwargs,
): ...
