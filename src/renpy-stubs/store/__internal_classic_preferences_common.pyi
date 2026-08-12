from _typeshed import Incomplete

def _prefs_screen_run(prefs_map: Incomplete) -> None: ...

class _Preference:
    name: Incomplete
    field: Incomplete
    values: Incomplete
    base: Incomplete
    def __init__(self, name: Incomplete, field: Incomplete, values: Incomplete, base: Incomplete = ...) -> None: ...
    def render(self) -> Incomplete: ...

class _VolumePreference:
    name: Incomplete
    mixer: Incomplete
    enable: Incomplete
    sound: Incomplete
    channel: Incomplete
    def __init__(
        self, name: Incomplete, mixer: Incomplete, enable: str = "True", sound: str = "None", channel: str = "sound"
    ) -> None: ...
    def render(self) -> None: ...

class _SliderPreference:
    name: Incomplete
    field: Incomplete
    range: Incomplete
    enable: Incomplete
    base: Incomplete
    def __init__(
        self, name: Incomplete, field: Incomplete, range: Incomplete, enable: str = "True", base: Incomplete = ...
    ) -> None: ...
    def get(self) -> Incomplete: ...
    def set(self, value: Incomplete) -> None: ...
    def render(self) -> None: ...

class _JumpPreference:
    name: Incomplete
    target: Incomplete
    condition: Incomplete
    show: Incomplete
    def __init__(self, name: Incomplete, target: Incomplete, condition: str = "True", show: str = "True") -> None: ...
    def render(self) -> None: ...

def _remove_preference(name: Incomplete) -> None: ...
