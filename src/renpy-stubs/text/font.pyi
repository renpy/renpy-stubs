import renpy.pygame as pygame
from _typeshed import Incomplete as Incomplete
from collections.abc import Generator
from renpy.pygame.surface import Surface as Surface

WHITE: Incomplete
BLACK: Incomplete

def is_zerowidth(char): ...

class ImageFont:
    height: int
    kerns: dict[str, float]
    default_kern: float
    baseline: int
    width: dict[str, float]
    advance: dict[str, float]
    offsets: dict[str, tuple[int, int]]
    chars: dict[str, Surface]
    def glyphs(self, s, level): ...
    def bounds(self, glyphs, bounds): ...
    def draw(self, target, xo, yo, color, glyphs, underline, strikethrough, black_color) -> None: ...
    @staticmethod
    def load_image(filename: str) -> pygame.Surface: ...

class SFont(ImageFont):
    filename: Incomplete
    spacewidth: Incomplete
    default_kern: Incomplete
    kerns: Incomplete
    charset: Incomplete
    baseline: Incomplete
    def __init__(self, filename, spacewidth, default_kern, kerns, charset, baseline=None) -> None: ...
    chars: Incomplete
    width: Incomplete
    advance: Incomplete
    offsets: Incomplete
    height: Incomplete
    def load(self) -> None: ...

class MudgeFont(ImageFont):
    filename: Incomplete
    xml: Incomplete
    spacewidth: Incomplete
    default_kern: Incomplete
    kerns: Incomplete
    def __init__(self, filename, xml, spacewidth, default_kern, kerns) -> None: ...
    chars: Incomplete
    width: Incomplete
    advance: Incomplete
    offsets: Incomplete
    height: Incomplete
    baseline: Incomplete
    def load(self) -> None: ...

def parse_bmfont_line(l): ...

class BMFont(ImageFont):
    filename: Incomplete
    def __init__(self, filename) -> None: ...
    chars: Incomplete
    width: Incomplete
    advance: Incomplete
    offsets: Incomplete
    kerns: Incomplete
    default_kern: int
    height: Incomplete
    baseline: Incomplete
    def load(self) -> None: ...

class ScaledImageFont(ImageFont):
    height: Incomplete
    baseline: Incomplete
    default_kern: Incomplete
    width: Incomplete
    advance: Incomplete
    offsets: Incomplete
    kerns: Incomplete
    chars: Incomplete
    def __init__(self, parent, factor) -> None: ...

def register_sfont(
    name=None,
    size=None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename=None,
    spacewidth: int = 10,
    baseline=None,
    default_kern: int = 0,
    kerns={},
    charset: str = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
) -> None: ...
def register_mudgefont(
    name=None,
    size=None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename=None,
    xml=None,
    spacewidth: int = 10,
    default_kern: int = 0,
    kerns={},
) -> None: ...
def register_bmfont(
    name=None, size=None, bold: bool = False, italics: bool = False, underline: bool = False, filename=None
) -> None: ...

face_cache: Incomplete

def load_face(fn, shaper): ...

image_fonts: Incomplete
scaled_image_fonts: Incomplete
font_cache: Incomplete
last_scale: float

def get_font(
    fn, size, bold, italics, outline, antialias, vertical, hinting, scale, shaper, instance, axis, features
): ...
def free_memory() -> None: ...
def load_fonts() -> None: ...
def variable_font_info(font): ...

class FontGroup:
    char_map: Incomplete
    map: Incomplete
    def __init__(self) -> None: ...
    def add(self, font, start, end, target=None, target_increment: bool = False): ...
    def remap(self, cha, target): ...
    def segment(self, s) -> Generator[Incomplete]: ...
