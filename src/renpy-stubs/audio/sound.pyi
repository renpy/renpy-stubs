import renpy.audio

def play(
    filename: str | list[str] | None,
    channel: str = "sound",
    fadeout: float = 0,
    fadein: float = 0,
    tight: bool = False,
    loop: bool = False,
    relative_volume: float = 1.0,
) -> None: ...
def queue(
    filename: str | list[str] | None,
    channel: str = "sound",
    clear_queue: bool = True,
    fadein: int = 0,
    tight: bool = False,
    loop: bool = False,
    relative_volume: float = 1.0,
) -> None: ...
def stop(channel: str = "sound", fadeout: float = 0) -> None: ...

set_mixer = renpy.audio.music.set_mixer
set_queue_empty_callback = renpy.audio.music.set_queue_empty_callback

def set_volume(volume: float, delay: float = 0, channel: str = "sound") -> None: ...
def set_pan(pan: float, delay: float, channel: str = "sound") -> None: ...
def is_playing(channel: str = "sound") -> bool: ...
def get_playing(channel: str = "sound") -> str | None: ...
