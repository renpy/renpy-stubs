from typing import Any

def web_input(
    prompt: str,
    default: str = "",
    allow: str | None = None,
    exclude: str = "{}",
    length: int | None = None,
    mask: bool = False,
) -> str | None: ...
def input(
    prompt: str,
    default: str = "",
    allow: str | None = None,
    exclude: str = "{}",
    length: int | None = None,
    with_none: bool | None = None,
    pixel_width: float | None = None,
    screen: str = "input",
    mask: str | None = None,
    copypaste: bool = True,
    multiline: bool = False,
    **kwargs,
) -> str | None: ...
def get_editable_input_value() -> tuple[Any | None, bool]: ...
def set_editable_input_value(input_value: Any | None, editable: bool) -> None: ...
