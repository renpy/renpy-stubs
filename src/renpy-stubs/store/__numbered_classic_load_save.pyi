from typing import Any

import renpy

_load_prompt: bool
_m1_classic_load_save__scratch: renpy.display.displayable.Displayable | None

def _render_savefile(
    index: int,
    name: str,
    extra_info: str,
    screenshot: renpy.display.displayable.Displayable | None,
    mtime: int,
    newest: bool,
    clicked: renpy.ui.Action,
) -> None: ...
def _render_new_slot(index: int, name: str, clicked: renpy.ui.Action) -> None: ...
def _file_picker_pages() -> list[tuple[str, str]]: ...
def _file_picker_page_files(page: str) -> list[str]: ...
def _file_picker_file_page(filename: str) -> str | None: ...
def _file_picker_process_screenshot(
    s: renpy.display.displayable.Displayable,
) -> renpy.display.displayable.Displayable: ...
def _file_picker(screen: str, save: bool) -> None: ...
