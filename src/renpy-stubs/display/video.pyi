import renpy
from renpy.display.displayable import Displayable as Displayable, DisplayableArguments as DisplayableArguments
from renpy.display.render import Render as Render
from renpy.pygame.surface import Surface as Surface
from renpy.types import DisplayableLike as DisplayableLike, Unused as Unused
from typing import Callable, Literal, overload
from _typeshed import Incomplete

current_movie: Unused
fullscreen: bool
default_size: tuple[int, int]
surface_file: Unused
surface: Unused

def movie_stop(clear: bool = True, only_fullscreen: bool = False) -> None: ...
def movie_start(filename: str, size: tuple[int, int] | None = None, loops: int = 0) -> None: ...
def movie_start_fullscreen(filename: str, size: tuple[int, int] | None = None, loops: int = 0) -> None: ...

movie_start_displayable = movie_start
texture: dict[str, Render | Surface]
displayable_channels: dict[tuple[str, str], list["Movie"]]
channel_movie: dict[str, "Movie"]
reset_channels: set[str]
group_texture: dict[str, Render | Surface]

def early_interact() -> None: ...
def interact() -> bool: ...
def get_movie_texture(
    channel: str, mask_channel: str | None = None, side_mask: bool = False, mipmap: bool | None = None
) -> tuple[Render | Surface | None, bool]: ...
def get_movie_texture_web(
    channel: str, mask_channel: str | None = None, side_mask: bool = False, mipmap: bool | None = None
) -> tuple[Render | Surface | None, bool]: ...
@overload
def resize_movie(r: None, width: float, height: float) -> None: ...
@overload
def resize_movie(r: Render | Surface, width: float, height: float) -> Render: ...
def render_movie(channel: str, width: float, height: float) -> Render | None: ...
def find_oversampled_filename(filename: str) -> str: ...
@overload
def find_oversampled(new: Movie, filename: str) -> str: ...
@overload
def find_oversampled(new: Movie, filename: list[str]) -> list[str]: ...
@overload
def find_oversampled(new: Movie, filename: None) -> None: ...
def default_play_callback(old: Incomplete, new: Movie) -> None: ...

allocated_channels: set[str]

class Movie(renpy.display.displayable.Displayable):
    fullscreen: bool
    channel: str
    _play: str | list[str] | None
    _original_play: str | list[str] | None
    mask: bool | None
    mask_channel: str | None
    side_mask: bool
    image: Displayable | None
    start_image: Displayable | None
    play_callback: Callable[[Movie | None, Movie], None] | None
    loop: bool
    group: str | None
    oversample: float | None
    playing_oversample: float
    dynamic_channel: bool
    @staticmethod
    def any_loadable(name: str | list[str]) -> bool: ...
    def after_setstate(self) -> None: ...
    def ensure_channel(self, name: str | None) -> None: ...
    def ensure_channels(self) -> None: ...
    def release_channel(self) -> None: ...
    keep_last_frame_serial: int
    size: tuple[int, int] | None
    _duplicatable: bool
    def __init__(
        self,
        fps: int = 24,
        size: tuple[int, int] | None = None,
        channel: str = "movie",
        play: str | list[str] | None = None,
        mask: bool | None = None,
        mask_channel: str | None = None,
        image: DisplayableLike | None = None,
        play_callback: Callable[[Movie | None, Movie], None] | None = None,
        side_mask: bool = False,
        loop: bool = True,
        start_image: DisplayableLike | None = None,
        group: str | None = None,
        keep_last_frame: bool = False,
        oversample: Unused = None,
        **properties,
    ) -> None: ...
    def _duplicate(self, args: DisplayableArguments | None) -> Movie: ...
    def _handles_event(self, event: str) -> bool: ...
    def set_transform_event(self, event: str) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def play(self, old: Movie | None) -> None: ...
    def stop(self) -> None: ...
    def per_interact(self) -> None: ...
    def visit(self) -> list[Displayable | None]: ...

def playing() -> Literal[True] | None: ...

last_channel_movie: dict[str, Movie]

def update_playing() -> None: ...
def frequent() -> bool: ...
