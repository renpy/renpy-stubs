import renpy.pygame as pygame
from _typeshed import Incomplete as Incomplete
from collections.abc import Generator
from renpy.pygame.surface import Surface as Surface

WHITE: Incomplete
BLACK: Incomplete

def is_zerowidth(char: Incomplete) -> Incomplete: ...

class ImageFont:
    height: int
    kerns: dict[str, float]
    default_kern: float
    baseline: int
    width: dict[str, float]
    advance: dict[str, float]
    offsets: dict[str, tuple[int, int]]
    chars: dict[str, Surface]
    def glyphs(self, s: Incomplete, level: Incomplete) -> Incomplete: ...
    def bounds(self, glyphs: Incomplete, bounds: Incomplete) -> Incomplete: ...
    def draw(
        self,
        target: Incomplete,
        xo: Incomplete,
        yo: Incomplete,
        color: Incomplete,
        glyphs: Incomplete,
        underline: Incomplete,
        strikethrough: Incomplete,
        black_color: Incomplete,
    ) -> None: ...
    @staticmethod
    def load_image(filename: str) -> pygame.Surface: ...

class SFont(ImageFont):
    filename: Incomplete
    spacewidth: Incomplete
    default_kern: Incomplete
    kerns: Incomplete
    charset: Incomplete
    baseline: Incomplete
    def __init__(
        self,
        filename: Incomplete,
        spacewidth: Incomplete,
        default_kern: Incomplete,
        kerns: Incomplete,
        charset: Incomplete,
        baseline: Incomplete = None,
    ) -> None: ...
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
    def __init__(
        self, filename: Incomplete, xml: Incomplete, spacewidth: Incomplete, default_kern: Incomplete, kerns: Incomplete
    ) -> None: ...
    chars: Incomplete
    width: Incomplete
    advance: Incomplete
    offsets: Incomplete
    height: Incomplete
    baseline: Incomplete
    def load(self) -> None: ...

def parse_bmfont_line(l: Incomplete) -> Incomplete: ...

class BMFont(ImageFont):
    filename: Incomplete
    def __init__(self, filename: Incomplete) -> None: ...
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
    def __init__(self, parent: Incomplete, factor: Incomplete) -> None: ...

def register_sfont(
    name: Incomplete = None,
    size: Incomplete = None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename: Incomplete = None,
    spacewidth: int = 10,
    baseline: Incomplete = None,
    default_kern: int = 0,
    kerns: Incomplete = {},
    charset: str = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
) -> None: ...
def register_mudgefont(
    name: Incomplete = None,
    size: Incomplete = None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename: Incomplete = None,
    xml: Incomplete = None,
    spacewidth: int = 10,
    default_kern: int = 0,
    kerns: Incomplete = {},
) -> None: ...
def register_bmfont(
    name: Incomplete = None,
    size: Incomplete = None,
    bold: bool = False,
    italics: bool = False,
    underline: bool = False,
    filename: Incomplete = None,
) -> None: ...

face_cache: Incomplete

def load_face(fn: Incomplete, shaper: Incomplete) -> Incomplete: ...

image_fonts: Incomplete
scaled_image_fonts: Incomplete
font_cache: Incomplete
last_scale: float

def get_font(
    fn: Incomplete,
    size: Incomplete,
    bold: bool,
    italics: bool,
    outline: bool,
    antialias: bool,
    vertical: bool,
    hinting: Incomplete,
    scale: float,
    shaper: Incomplete,
    instance: Incomplete,
    axis: Incomplete,
    features: Incomplete,
) -> Incomplete: ...
def free_memory() -> None: ...
def load_fonts() -> None: ...
def variable_font_info(font: Incomplete) -> Incomplete: ...

class FontGroup:
    char_map: Incomplete
    map: Incomplete
    def __init__(self) -> None: ...
    def add(
        self,
        font: Incomplete,
        start: Incomplete,
        end: Incomplete,
        target: Incomplete = None,
        target_increment: bool = False,
    ) -> None: ...
    def remap(self, cha: Incomplete, target: Incomplete) -> None: ...
    def segment(self, s: Incomplete) -> Generator[Incomplete]: ...
