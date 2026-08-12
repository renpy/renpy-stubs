from _typeshed import Incomplete

from renpy.ui import Action
from renpy.store import DictEquality

class _m1_00preferences__DisplayAction(Action, DictEquality):
    factor: float
    def __init__(self, factor: Incomplete) -> None: ...
    def get_size(self) -> Incomplete: ...
    def __call__(self) -> None: ...
    def get_sensitive(self) -> bool: ...
    def get_selected(self) -> bool: ...

_m1_00screen__DisplayAction = _m1_00preferences__DisplayAction

class _m1_00preferences__ResetPreferences(Action, DictEquality):
    def __call__(self) -> None: ...

class _DisplayReset(Action, DictEquality):
    def __call__(self) -> None: ...

@renpy.pure
def Preference(name: Incomplete, value: Incomplete = None, range: Incomplete = None) -> Incomplete: ...
def _m1_00preferences__show_self_voicing() -> None: ...
def _prefs_screen_run(prefs_map: Incomplete, positions: Incomplete) -> None: ...

class _Preference:
    name: Incomplete
    field: Incomplete
    values: Incomplete
    base: Incomplete
    def __init__(self, name: Incomplete, field: Incomplete, values: Incomplete, base: Incomplete = ...) -> None: ...
    def render_preference(self) -> Incomplete: ...

class _VolumePreference:
    name: Incomplete
    mixer: Incomplete
    enable: Incomplete
    sound: Incomplete
    channel: Incomplete
    def __init__(
        self, name: Incomplete, mixer: Incomplete, enable: str = "True", sound: str = "None", channel: int = 0
    ) -> None: ...
    def render_preference(self) -> None: ...

class _SliderPreference:
    name: Incomplete
    range: Incomplete
    get: Incomplete
    set: Incomplete
    enable: Incomplete
    def __init__(
        self, name: Incomplete, range: Incomplete, get: Incomplete, set: Incomplete, enable: str = "True"
    ) -> None: ...
    def render_preference(self) -> None: ...

class _PreferenceSpinner:
    name: Incomplete
    field: Incomplete
    minimum: Incomplete
    maximum: Incomplete
    delta: Incomplete
    cond: Incomplete
    render: Incomplete
    base: Incomplete
    def __init__(
        self,
        name: Incomplete,
        field: Incomplete,
        minimum: Incomplete,
        maximum: Incomplete,
        delta: Incomplete,
        cond: str = "True",
        render: Incomplete = ...,
        base: Incomplete = ...,
    ) -> None: ...
    def render_preference(self) -> Incomplete: ...

def _joystick_select_binding() -> Incomplete: ...
def _joystick_get_binding() -> None: ...
def _joystick_take_binding(binding: Incomplete, key: Incomplete) -> None: ...

class _JoystickPreference:
    name: Incomplete
    def __init__(self, name: Incomplete) -> None: ...
    def render_preference(self) -> Incomplete: ...

class _JumpPreference:
    name: Incomplete
    target: Incomplete
    condition: Incomplete
    def __init__(self, name: Incomplete, target: Incomplete, condition: str = "True") -> None: ...
    def render_preference(self) -> None: ...

def _remove_preference(name: Incomplete) -> None: ...
