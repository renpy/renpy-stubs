def web_input(prompt, default: str = "", allow=None, exclude: str = "{}", length=None, mask: bool = False): ...
def input(
    prompt,
    default: str = "",
    allow=None,
    exclude: str = "{}",
    length=None,
    with_none=None,
    pixel_width=None,
    screen: str = "input",
    mask=None,
    copypaste: bool = True,
    multiline: bool = False,
    **kwargs,
): ...
def get_editable_input_value(): ...
def set_editable_input_value(input_value, editable) -> None: ...
