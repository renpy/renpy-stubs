from typing import Any

dark_cyan: str
bright_cyan: str
dark_red: str
bright_red: str
green: str

class _SelectedCompat:
    _is_style_compat: bool
    target: Any
    def __init__(self, target: Any) -> None: ...
    __dict__: dict[str, Any]
    def clear(self) -> None: ...

def _apply_selected_compat() -> None: ...
