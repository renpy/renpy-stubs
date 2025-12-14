import renpy.audio
from renpy.compat import (
    PY2 as PY2,
    basestring as basestring,
    bchr as bchr,
    bord as bord,
    chr as chr,
    open as open,
    pystr as pystr,
    range as range,
    round as round,
    str as str,
    tobytes as tobytes,
    unicode as unicode,
)

def play(
    filename,
    channel: str = "sound",
    fadeout: int = 0,
    fadein: int = 0,
    tight: bool = False,
    loop: bool = False,
    relative_volume: float = 1.0,
) -> None: ...
def queue(
    filename,
    channel: str = "sound",
    clear_queue: bool = True,
    fadein: int = 0,
    tight: bool = False,
    loop: bool = False,
    relative_volume: float = 1.0,
) -> None: ...
def stop(channel: str = "sound", fadeout: int = 0) -> None: ...

set_mixer = renpy.audio.music.set_mixer
set_queue_empty_callback = renpy.audio.music.set_queue_empty_callback

def set_volume(volume, delay: int = 0, channel: str = "sound") -> None: ...
def set_pan(pan, delay, channel: str = "sound") -> None: ...
def is_playing(channel: str = "sound"): ...
def get_playing(channel: str = "sound"): ...
