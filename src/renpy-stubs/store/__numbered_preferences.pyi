from collections.abc import Callable
from typing import Any

import renpy
from renpy.store import DictEquality, MixerValue
from renpy.ui import Action

class _m1_00preferences__DisplayAction(Action, DictEquality):
    factor: float
    def __init__(self, factor: float) -> None: ...
    def get_size(self) -> tuple[int, int]: ...
    def __call__(self) -> None: ...
    def get_sensitive(self) -> bool: ...
    def get_selected(self) -> bool: ...

_m1_00screen__DisplayAction = _m1_00preferences__DisplayAction

class _m1_00preferences__ResetPreferences(Action, DictEquality):
    def __call__(self) -> None: ...

class _DisplayReset(Action, DictEquality):
    def __call__(self) -> None: ...

@renpy.pure
def Preference(
    name: str, value: str | int | float | None = None, range: int | float | None = None
) -> Action | list[Action] | MixerValue | None: ...
def _m1_00preferences__show_self_voicing() -> None: ...
def _prefs_screen_run(prefs_map: dict[str, list[Any]], positions: dict[str, dict[str, Any]] | None) -> None: ...

class _Preference:
    name: str
    field: str
    values: list[tuple[str, Any, str | None]]
    base: Any
    def __init__(self, name: str, field: str, values: list[tuple[str, Any, str | None]], base: Any = ...) -> None: ...
    def render_preference(self) -> None: ...

class _VolumePreference:
    name: str
    mixer: str
    enable: str
    sound: str
    channel: int
    def __init__(self, name: str, mixer: str, enable: str = "True", sound: str = "None", channel: int = 0) -> None: ...
    def render_preference(self) -> None: ...

class _SliderPreference:
    name: str
    range: int
    get: Callable[[], int]
    set: Callable[[int], None]
    enable: str
    def __init__(
        self, name: str, range: int, get: Callable[[], int], set: Callable[[int], None], enable: str = "True"
    ) -> None: ...
    def render_preference(self) -> None: ...

class _PreferenceSpinner:
    name: str
    field: str
    minimum: int | float
    maximum: int | float
    delta: int | float
    cond: str
    render: Callable[[Any], str]
    base: Any
    def __init__(
        self,
        name: str,
        field: str,
        minimum: int | float,
        maximum: int | float,
        delta: int | float,
        cond: str = "True",
        render: Callable[[Any], str] = ...,
        base: Any = ...,
    ) -> None: ...
    def render_preference(self) -> None: ...

def _joystick_select_binding() -> None: ...
def _joystick_get_binding() -> None: ...
def _joystick_take_binding(binding: str | None, key: str) -> None: ...

class _JoystickPreference:
    name: str
    def __init__(self, name: str) -> None: ...
    def render_preference(self) -> None: ...

class _JumpPreference:
    name: str
    target: str
    condition: str
    def __init__(self, name: str, target: str, condition: str = "True") -> None: ...
    def render_preference(self) -> None: ...

def _remove_preference(name: str) -> None: ...
