from _typeshed import Incomplete
import renpy.audio

def play(
    filename: Incomplete,
    channel: str = "sound",
    fadeout: int = 0,
    fadein: int = 0,
    tight: bool = False,
    loop: bool = False,
    relative_volume: float = 1.0,
) -> None: ...
def queue(
    filename: Incomplete,
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

def set_volume(volume: Incomplete, delay: int = 0, channel: str = "sound") -> None: ...
def set_pan(pan: Incomplete, delay: Incomplete, channel: str = "sound") -> None: ...
def is_playing(channel: str = "sound") -> Incomplete: ...
def get_playing(channel: str = "sound") -> Incomplete: ...
