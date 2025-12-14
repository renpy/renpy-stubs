from _typeshed import Incomplete

pad_bindings: Incomplete
all_preferences: Incomplete

class Preference:
    name: Incomplete
    default: Incomplete
    types: Incomplete
    def __init__(self, name, default, types=None) -> None: ...

class Preferences(renpy.object.Object):
    __version__: Incomplete
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
    volumes: Incomplete
    mute: Incomplete
    joymap: Incomplete
    physical_size: Incomplete
    virtual_size: Incomplete
    renderer: str
    performance_test: bool
    language: Incomplete
    self_voicing: bool
    self_voicing_volume_drop: float
    emphasize_audio: bool
    pad_enabled: bool
    mobile_rollback_side: str
    desktop_rollback_side: str
    gl_npot: bool
    gl_powersave: bool
    gl_framerate: Incomplete
    gl_tearing: bool
    font_transform: Incomplete
    font_size: float
    font_line_spacing: float
    system_cursor: bool
    high_contrast: bool
    audio_when_minimized: bool
    audio_when_unfocused: bool
    web_cache_preload: bool
    voice_after_game_menu: bool
    maximized: bool
    window_position: Incomplete
    window_position_layout: Incomplete
    restore_window_position: bool
    mono_audio: bool
    font_kerning: float
    def init(self) -> None: ...
    def reset(self) -> None: ...
    def check(self): ...
    def after_upgrade(self, version) -> None: ...
    def __init__(self) -> None: ...
    def set_volume(self, mixer, volume) -> None: ...
    def get_volume(self, mixer): ...
    def set_mixer(self, mixer, volume) -> None: ...
    def get_mixer(self, mixer): ...
    def set_mute(self, mixer, mute) -> None: ...
    def get_mute(self, mixer): ...
    def init_mixers(self) -> None: ...
    def get_all_mixers(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
