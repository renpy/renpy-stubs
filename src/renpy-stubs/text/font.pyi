import renpy.pygame as pygame
from _typeshed import Incomplete as Incomplete
from collections.abc import Generator
from renpy.pygame.surface import Surface as Surface
from renpy.text.textsupport import Glyph as Glyph
from renpy.text import hbfont, ftfont
from typing import Self, Iterable

WHITE: tuple[int, int, int, int]
BLACK: tuple[int, int, int, int]

type FontKey = tuple[str, int, bool, bool]

def is_zerowidth(char: int) -> bool: ...

class ImageFont:
    height: int
    kerns: dict[str, float]
    default_kern: float
    baseline: int
    width: dict[str, float]
    advance: dict[str, float]
    offsets: dict[str, tuple[int, int]]
    chars: dict[str, Surface]
    def glyphs(self, s: str, level: int) -> list[Glyph]: ...
    def bounds(self, glyphs: list[Glyph], bounds: tuple[int, int, int, int]) -> tuple[int, int, int, int]: ...
    def draw(
        self,
        target: Surface,
        xo: int,
        yo: int,
        color: tuple[int, int, int, int],
        glyphs: list[Glyph],
        underline: int,
        strikethrough: bool,
        black_color: tuple[int, int, int, int] | None,
    ) -> None: ...
    @staticmethod
    def load_image(filename: str) -> pygame.surface.Surface: ...

class SFont(ImageFont):
    filename: str
    spacewidth: int
    default_kern: int
    kerns: dict[str, int]
    charset: str
    baseline: int | None
    def __init__(
        self,
        filename: str,
        spacewidth: int,
        default_kern: int,
        kerns: dict[str, int],
        charset: str,
        baseline: int | None = None,
    ) -> None: ...
    chars: dict[str, Surface]
    width: dict[str, float]
    advance: dict[str, float]
    offsets: dict[str, tuple[int, int]]
    height: int
    def load(self) -> None: ...

class MudgeFont(ImageFont):
    filename: str
    xml: str
    spacewidth: int
    default_kern: int
    kerns: dict[str, int]
    def __init__(self, filename: str, xml: str, spacewidth: int, default_kern: int, kerns: dict[str, int]) -> None: ...
    chars: dict[str, Surface]
    width: dict[str, float]
    advance: dict[str, float]
    offsets: dict[str, tuple[int, int]]
    height: int
    baseline: int | None
    def load(self) -> None: ...

def parse_bmfont_line(l: str) -> tuple[str, dict[str, str]]: ...

class BMFont(ImageFont):
    filename: str
    def __init__(self, filename: str) -> None: ...
    chars: dict[str, Surface]
    width: dict[str, float]
    advance: dict[str, float]
    offsets: dict[str, tuple[int, int]]
    kerns: dict[str, int]
    default_kern: int
    height: int
    baseline: int | None
    def load(self) -> None: ...

class ScaledImageFont(ImageFont):
    height: int
    baseline: int
    default_kern: int
    width: dict[str, float]
    advance: dict[str, float]
    offsets: dict[str, tuple[int, int]]
    kerns: dict[str, int]
    chars: dict[str, Surface]
    def __init__(self, parent: ImageFont, factor: float) -> None: ...

def register_sfont(
    name: str = None,
    size: int = None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename: str = None,
    spacewidth: int = 10,
    baseline: int | None = None,
    default_kern: int = 0,
    kerns: dict[str, int] = {},
    charset: str = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
) -> None: ...
def register_mudgefont(
    name: str = None,
    size: int = None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename: str = None,
    xml: str = None,
    spacewidth: int = 10,
    default_kern: int = 0,
    kerns: dict[str, int] = {},
) -> None: ...
def register_bmfont(
    name: str = None,
    size: int = None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename: str = None,
) -> None: ...

face_cache: dict[tuple[str, str], hbfont.HBFace | ftfont.FTFace]

def load_face(fn: str, shaper: str) -> hbfont.HBFace | ftfont.FTFace: ...

image_fonts: dict[FontKey, ImageFont]
scaled_image_fonts: dict[FontKey, ScaledImageFont]
font_cache: dict[Incomplete, hbfont.HBFace | ftfont.FTFace]
last_scale: float

def get_font(
    fn: str,
    size: int,
    bold: bool,
    italics: bool,
    outline: bool,
    antialias: bool,
    vertical: bool,
    hinting: bool | str,
    scale: float,
    shaper: str,
    instance: Incomplete,
    axis: Incomplete,
    features: Incomplete,
) -> ImageFont | hbfont.HBFont | ftfont.FTFont: ...
def free_memory() -> None: ...
def load_fonts() -> None: ...
def variable_font_info(font: str) -> hbfont.Variations: ...

class FontGroup:
    char_map: dict[int, int]
    map: dict[int | None, str]
    def __init__(self) -> None: ...
    def add(
        self,
        font: str,
        start: int | str | bytes | None,
        end: int | str | bytes | None,
        target: int | str | bytes | None = None,
        target_increment: bool = False,
    ) -> Self: ...
    def remap(self, cha: int | str | bytes | Iterable[int | str | bytes], target: int | str | bytes) -> Self: ...
    def segment(self, s: str) -> Generator[tuple[str | None, str], None, None]: ...
