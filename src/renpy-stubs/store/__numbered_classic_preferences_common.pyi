from collections.abc import Callable
from typing import Any

def _prefs_screen_run(prefs_map: dict[str, list[Any]]) -> None: ...

class _Preference:
    name: str
    field: str
    values: list[tuple[str, Any, str | None]]
    base: Any
    def __init__(self, name: str, field: str, values: list[tuple[str, Any, str | None]], base: Any = ...) -> None: ...
    def render(self) -> None: ...

class _VolumePreference:
    name: str
    mixer: str
    enable: str
    sound: str
    channel: int
    def __init__(self, name: str, mixer: str, enable: str = "True", sound: str = "None", channel: int = 0) -> None: ...
    def render(self) -> None: ...

class _SliderPreference:
    name: str
    field: str
    range: int
    enable: str
    base: Any
    def __init__(self, name: str, field: str, range: int, enable: str = "True", base: Any = ...) -> None: ...
    def get(self) -> int: ...
    def set(self, value: int) -> None: ...
    def render(self) -> None: ...

class _JumpPreference:
    name: str
    target: str
    condition: str
    show: str
    def __init__(self, name: str, target: str, condition: str = "True", show: str = "True") -> None: ...
    def render(self) -> None: ...

def _remove_preference(name: str) -> None: ...
