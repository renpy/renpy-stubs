import renpy
from _typeshed import Incomplete as Incomplete
from renpy.object import Object as Object

pad_bindings: dict[str, list[str]]
all_preferences: list[Preference]

class Preference:
    name: str
    default: Any
    types: type | tuple[type, ...]
    def __init__(self, name: str, default: Any, types: type | tuple[type, ...] = ...) -> None: ...

class Preferences(renpy.object.Object):
    __version__: int
    fullscreen: bool
    skip_unseen: bool
    text_cps: int
    afm_time: int
    afm_enable: bool
    using_afm_enable: bool
    voice_sustain: bool
    mouse_move: bool
    show_empty_window: bool
    wait_voice: bool
    afm_after_click: bool
    transitions: int
    video_image_fallback: bool
    skip_after_choices: bool
    volumes: dict[str, float]
    mute: dict[str, bool]
    joymap: dict[str, str]
    physical_size: tuple[int, int] | None
    virtual_size: tuple[int, int] | None
    renderer: str
    performance_test: bool
    language: str | None
    self_voicing: bool
    self_voicing_volume_drop: float
    emphasize_audio: bool
    pad_enabled: bool
    mobile_rollback_side: str
    desktop_rollback_side: str
    gl_npot: bool
    gl_powersave: bool
    gl_framerate: int | None
    gl_tearing: bool
    font_transform: str | None
    font_size: float
    font_line_spacing: float
    system_cursor: bool
    high_contrast: bool
    audio_when_minimized: bool
    audio_when_unfocused: bool
    web_cache_preload: bool
    voice_after_game_menu: bool
    maximized: bool
    window_position: tuple[int, int]
    window_position_layout: tuple[tuple[int, int, int, int], ...]
    restore_window_position: bool
    mono_audio: bool
    font_kerning: float
    tts_speed: float
    tts_voice: str | None
    def init(self) -> None: ...
    def reset(self) -> None: ...
    def check(self) -> str | None: ...
    def after_upgrade(self, version: int) -> None: ...
    def __init__(self) -> None: ...
    def set_volume(self, mixer: str, volume: float) -> None: ...
    def get_volume(self, mixer: str) -> float: ...
    def set_mixer(self, mixer: str, volume: float) -> None: ...
    def get_mixer(self, mixer: str) -> float: ...
    def set_mute(self, mixer: str, mute: bool) -> None: ...
    def get_mute(self, mixer: str) -> bool: ...
    def init_mixers(self) -> None: ...
    def get_all_mixers(self) -> list[str]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
