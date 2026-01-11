import io
import renpy
import threading
from renpy.audio.filter import AudioFilter as AudioFilter
from renpy.pygame.surface import Surface as Surface
from renpy.revertable import RevertableObject as RevertableObject
from renpy.types import Unused as Unused
from typing import Any, Callable, Literal, overload

pcm_ok: bool | None
unique: float
serial: int
old_channel_count: int

def get_serial() -> tuple[float, int]: ...

AudioNotReady: renpy.object.Sentinel

def load(fn: str) -> io.BytesIO | str | renpy.object.Sentinel: ...

class AudioData(str):
    data: bytes
    def __new__(cls, data: bytes, filename: str) -> AudioData: ...
    def __init__(self, data: bytes, filename: str) -> None: ...
    def __reduce__(self) -> str | tuple[Any, ...]: ...

class QueueEntry:
    audio_filter: AudioFilter | None
    filename: str
    fadein: float
    tight: bool
    loop: bool
    relative_volume: float
    def __init__(
        self,
        filename: str,
        fadein: float,
        tight: bool,
        loop: bool,
        relative_volume: float,
        audio_filter: AudioFilter | None,
    ) -> None: ...

class MusicContext(renpy.revertable.RevertableObject):
    __version__: int
    pause: bool
    last_relative_volume: float
    audio_filter: AudioFilter | None
    raw_audio_filter: AudioFilter | None
    pan_time: tuple[float, int] | None
    pan: float
    secondary_volume_time: tuple[float, int] | None
    secondary_volume: float
    last_changed: int
    last_tight: bool
    last_filenames: list[str]
    force_stop: bool
    def __init__(self) -> None: ...
    def copy(self) -> MusicContext: ...

next_channel_number: int
lock: threading.RLock
NotSet: renpy.object.Sentinel

class Channel:
    audio_filter: AudioFilter | None
    raw_audio_filter: AudioFilter | None
    name: str | int
    _number: int | None
    mixer: str | None
    chan_volume: float
    actual_volume: float
    queue: list[QueueEntry]
    loop: list[str]
    playing: bool
    synchro_start: bool
    default_synchro_start: bool | renpy.object.Sentinel
    last_changed: int
    callback: Callable[[], None] | None
    pan_time: tuple[float, int] | None
    secondary_volume_time: tuple[float, int] | None
    stop_on_mute: bool
    tight: bool
    keep_queue: int
    file_prefix: str
    file_suffix: str
    buffer_queue: bool
    paused: bool | None
    default_loop: bool
    default_loop_set: bool
    movie: int
    def __init__(
        self,
        name: str | int,
        default_loop: bool | renpy.object.Sentinel,
        stop_on_mute: bool,
        tight: bool,
        file_prefix: str,
        file_suffix: str,
        buffer_queue: bool,
        movie: bool,
        framedrop: bool,
        synchro_start: bool | renpy.object.Sentinel,
    ) -> None: ...
    def get_number(self) -> int: ...
    number: int
    def get_context(self) -> MusicContext: ...
    context: MusicContext
    def copy_context(self) -> MusicContext: ...
    @overload
    def split_filename(self, filename: AudioData, looped: bool) -> tuple[AudioData, float, float, float]: ...
    @overload
    def split_filename(self, filename: str, looped: bool) -> tuple[str, float, float, float]: ...
    def split_filename(
        self, filename: str | AudioData, looped: bool
    ) -> tuple[str | AudioData, float, float, float]: ...
    def periodic(self) -> None: ...
    def dequeue(self, even_tight: bool = False) -> None: ...
    def interact(self) -> None: ...
    def fadeout(self, secs: float) -> None: ...
    def reload(self) -> None: ...
    def set_audio_filter(
        self, audio_filter: AudioFilter | None, replace: bool = False, duration: float = 0.016
    ) -> None: ...
    def enqueue(
        self,
        filenames: list[str],
        loop: bool = True,
        synchro_start: bool | renpy.object.Sentinel | None = None,
        fadein: float = 0,
        tight: bool | None = None,
        loop_only: bool = False,
        relative_volume: float = 1.0,
    ) -> None: ...
    def get_playing(self) -> str | list[str] | None: ...
    def set_volume(self, volume: float) -> None: ...
    def get_pos(self) -> float: ...
    def get_duration(self) -> float: ...
    def set_pan(self, pan: float, delay: float) -> None: ...
    def set_secondary_volume(self, volume: float, delay: float) -> None: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def read_video(self) -> Surface | None: ...
    def video_ready(self) -> int: ...

all_channels: list[Channel]
channels: dict[str | int, Channel]

def register_channel(
    name: str,
    mixer: str | None = None,
    loop: bool | renpy.object.Sentinel = ...,
    stop_on_mute: bool = True,
    tight: bool = False,
    file_prefix: str = "",
    file_suffix: str = "",
    buffer_queue: bool = True,
    movie: bool = False,
    framedrop: bool = True,
    force: bool = False,
    synchro_start: bool | renpy.object.Sentinel | None = None,
) -> None: ...
def alias_channel(name: str, newname: str) -> None: ...
def get_channel(name: str) -> Channel: ...
def set_force_stop(name: str, value: bool) -> None: ...

periodic_thread: threading.Thread | None
periodic_thread_quit: bool

def init() -> None: ...
def fadeout_all() -> None: ...
def quit() -> None: ...

pcm_volume: Unused
old_emphasized: bool

def periodic_pass() -> Literal[False] | None: ...

periodic_exc: Exception | None
run_periodic: bool
periodic_condition: threading.Condition

def periodic_thread_main() -> None: ...
def periodic() -> None: ...
def interact() -> None: ...
def pump() -> None: ...
def rollback() -> None: ...
def autoreload(_fn: Unused) -> None: ...
def pause_all() -> None: ...
def unpause_all() -> None: ...
def sample_surfaces(rgb: Surface, rgba: Surface) -> None: ...
def advance_time() -> None: ...
