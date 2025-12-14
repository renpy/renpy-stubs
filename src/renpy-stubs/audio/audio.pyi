from _typeshed import Incomplete
import renpy

pcm_ok: Incomplete
unique: Incomplete
serial: int
old_channel_count: int

def get_serial(): ...

AudioNotReady: Incomplete

def load(fn): ...

class AudioData(str):
    data: bytes
    def __new__(cls, data: bytes, filename: str): ...
    def __init__(self, data, filename) -> None: ...
    def __reduce__(self): ...

class QueueEntry:
    audio_filter: Incomplete
    filename: Incomplete
    fadein: Incomplete
    tight: Incomplete
    loop: Incomplete
    relative_volume: Incomplete
    def __init__(self, filename, fadein, tight, loop, relative_volume, audio_filter) -> None: ...

class MusicContext(renpy.revertable.RevertableObject):
    __version__: int
    pause: bool
    last_relative_volume: float
    audio_filter: Incomplete
    raw_audio_filter: Incomplete
    pan_time: Incomplete
    pan: int
    secondary_volume_time: Incomplete
    secondary_volume: float
    last_changed: int
    last_tight: bool
    last_filenames: Incomplete
    force_stop: bool
    def __init__(self) -> None: ...
    def copy(self): ...

next_channel_number: int
lock: Incomplete
NotSet: Incomplete

class Channel:
    audio_filter: Incomplete
    raw_audio_filter: Incomplete
    name: Incomplete
    mixer: Incomplete
    chan_volume: float
    actual_volume: float
    queue: Incomplete
    loop: Incomplete
    playing: bool
    synchro_start: bool
    default_synchro_start: Incomplete
    last_changed: int
    callback: Incomplete
    pan_time: Incomplete
    secondary_volume_time: Incomplete
    stop_on_mute: Incomplete
    tight: Incomplete
    keep_queue: int
    file_prefix: Incomplete
    file_suffix: Incomplete
    buffer_queue: Incomplete
    paused: Incomplete
    default_loop: bool
    default_loop_set: bool
    movie: Incomplete
    def __init__(
        self,
        name,
        default_loop,
        stop_on_mute,
        tight,
        file_prefix,
        file_suffix,
        buffer_queue,
        movie,
        framedrop,
        synchro_start,
    ) -> None: ...
    def get_number(self): ...
    number: Incomplete
    def get_context(self): ...
    context: Incomplete
    def copy_context(self): ...
    def split_filename(
        self, filename: str | AudioData, looped: bool
    ) -> tuple[str | AudioData, float, float, float]: ...
    def periodic(self) -> None: ...
    def dequeue(self, even_tight: bool = False) -> None: ...
    def interact(self) -> None: ...
    def fadeout(self, secs) -> None: ...
    def reload(self) -> None: ...
    def set_audio_filter(self, audio_filter, replace: bool = False, duration: float = 0.016) -> None: ...
    def enqueue(
        self,
        filenames,
        loop: bool = True,
        synchro_start=None,
        fadein: int = 0,
        tight=None,
        loop_only: bool = False,
        relative_volume: float = 1.0,
    ) -> None: ...
    def get_playing(self): ...
    def set_volume(self, volume) -> None: ...
    def get_pos(self): ...
    def get_duration(self): ...
    def set_pan(self, pan, delay) -> None: ...
    def set_secondary_volume(self, volume, delay) -> None: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def read_video(self): ...
    def video_ready(self): ...

all_channels: Incomplete
channels: Incomplete

def register_channel(
    name,
    mixer=None,
    loop=...,
    stop_on_mute: bool = True,
    tight: bool = False,
    file_prefix: str = "",
    file_suffix: str = "",
    buffer_queue: bool = True,
    movie: bool = False,
    framedrop: bool = True,
    force: bool = False,
    synchro_start=None,
) -> None: ...
def alias_channel(name, newname) -> None: ...
def get_channel(name): ...
def set_force_stop(name, value) -> None: ...

periodic_thread: Incomplete
periodic_thread_quit: bool

def init() -> None: ...
def fadeout_all() -> None: ...
def quit() -> None: ...

pcm_volume: Incomplete
old_emphasized: bool

def periodic_pass(): ...

periodic_exc: Exception | None
run_periodic: bool
periodic_condition: Incomplete

def periodic_thread_main() -> None: ...
def periodic() -> None: ...
def interact() -> None: ...
def pump() -> None: ...
def rollback() -> None: ...
def autoreload(_fn) -> None: ...
def pause_all() -> None: ...
def unpause_all() -> None: ...
def sample_surfaces(rgb, rgba) -> None: ...
def advance_time() -> None: ...
