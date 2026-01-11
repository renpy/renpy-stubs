from _typeshed import Incomplete as Incomplete
from typing import Any, Generator, overload

import renpy
import renpy.pygame as pygame
import renpy.text.extras as extras
import renpy.text.textsupport as textsupport
from renpy.display.displayable import Displayable as Displayable
from renpy.display.matrix import Matrix as Matrix, Matrix2D as Matrix2D
from renpy.gl2.gl2polygon import Polygon as Polygon
from renpy.text.bidi import (
    LTR as LTR,
    ON as ON,
    RTL as RTL,
    WLTR as WLTR,
    WRTL as WRTL,
    get_embedding_levels as get_embedding_levels,
    log2vis as log2vis,
)
from renpy.text.emoji_trie import UNQUALIFIED as UNQUALIFIED, emoji as emoji
from renpy.text.textsupport import DISPLAYABLE, PARAGRAPH, TAG, TEXT, Glyph
from renpy.text.shader import TextShader
from typing import Callable

type Token = tuple[int, str | Displayable]
type Outline = tuple[int, renpy.color.ColorLike | None, int, int]
type Paragraph = list[tuple[TextSegment | SpaceSegment | DisplayableSegment | FlagSegment, str]]

BASELINE: int
READING_ORDER: dict[str | None, int]

class Blit:
    x: int
    y: int
    w: int
    h: int
    alpha: float
    left: bool
    right: bool
    top: bool
    bottom: bool
    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        alpha: float = 1.0,
        left: bool = False,
        right: bool = False,
        top: bool = False,
        bottom: bool = False,
    ) -> None: ...

class TextMeshDisplayable(renpy.display.core.Displayable):
    width: Incomplete
    height: Incomplete
    tex: Incomplete
    shader: Incomplete
    mesh: Incomplete
    uniforms: Incomplete
    def __init__(
        self,
        width: Incomplete,
        height: Incomplete,
        tex: Incomplete,
        shader: Incomplete,
        mesh: Incomplete,
        uniforms: Incomplete,
    ) -> None: ...
    def render(self, width: Incomplete, height: Incomplete, st: Incomplete, at: Incomplete) -> Incomplete: ...

def outline_blits(blits: Incomplete, outline: Incomplete) -> Incomplete: ...

class DrawInfo:
    surface: pygame.surface.Surface | None
    override_color: tuple[int, int, int, int] | None
    outline: float
    displayable_blits: list[tuple[Displayable, int, int]] | None

class TextSegment:
    antialias: bool
    vertical: bool | None
    font: str
    size: int
    bold: bool
    italic: bool
    underline: int
    strikethrough: int
    color: renpy.color.Color
    black_color: renpy.color.Color
    hyperlink: int | None
    kerning: float
    cps: float
    ruby_top: bool
    ruby_bottom: bool
    hinting: Incomplete
    outline_color: renpy.color.Color | None
    ignore: bool
    default_font: bool
    shaper: str
    instance: str | None
    axis: dict[str, int] | None
    shader: TextShader | None
    features: dict[str, int] | None
    def __init__(self, source: TextSegment | None = None) -> None: ...
    def take_style(self, style: Incomplete, layout: Layout, context: str | None = None) -> None: ...
    def glyphs(self, s: str, layout: Layout, level: int = 0) -> list[Glyph]: ...
    def draw(self, glyphs: list[Glyph], di: DrawInfo, xo: int, yo: int, layout: Layout) -> None: ...
    def assign_times(self, gt: float, glyphs: list[Glyph]) -> None: ...
    def subsegment(self, s: Incomplete) -> Generator[Incomplete]: ...
    def bounds(
        self, glyphs: list[Glyph], bounds: tuple[int, int, int, int], layout: Layout
    ) -> tuple[int, int, int, int]: ...

class SpaceSegment:
    width: Incomplete
    height: Incomplete
    ts: TextSegment
    def __init__(self, ts: TextSegment, width: float = 0.0, height: float = 0.0) -> None: ...
    def glyphs(self, s: str, layout: Layout) -> list[Glyph]: ...
    def bounds(
        self, glyphs: list[Glyph], bounds: tuple[int, int, int, int], layout: Layout
    ) -> tuple[int, int, int, int]: ...
    def draw(self, glyphs: list[Glyph], di: DrawInfo, xo: int, yo: int, layout: Layout) -> None: ...
    def assign_times(self, gt: float, glyphs: list[Glyph]) -> None: ...

class DisplayableSegment:
    d: Incomplete
    hyperlink: Incomplete
    cps: Incomplete
    ruby_top: Incomplete
    ruby_bottom: Incomplete
    shader: Incomplete
    def __init__(self, ts: TextSegment, d: Incomplete, renders: Incomplete) -> None: ...
    def glyphs(self, s: str, layout: Layout) -> list[Glyph]: ...
    def draw(self, glyphs: list[Glyph], di: DrawInfo, xo: int, yo: int, layout: Layout) -> None: ...
    def assign_times(self, gt: float, glyphs: list[Glyph]) -> None: ...
    def bounds(
        self, glyphs: list[Glyph], bounds: tuple[int, int, int, int], layout: Layout
    ) -> tuple[int, int, int, int]: ...

class FlagSegment:
    def glyphs(self, s: str, layout: Layout) -> list[Glyph]: ...
    def draw(self, glyphs: list[Glyph], di: DrawInfo, xo: int, yo: int, layout: Layout) -> None: ...
    def assign_times(self, gt: float, glyphs: list[Glyph]) -> None: ...
    def bounds(
        self, glyphs: list[Glyph], bounds: tuple[int, int, int, int], layout: Layout
    ) -> tuple[int, int, int, int]: ...

class Layout:
    oversample: float
    reverse: Matrix2D
    forward: Matrix2D
    outline_step: bool
    pixel_perfect: bool
    line_overlap_split: int
    has_hyperlinks: bool
    has_ruby: bool
    start_segment: FlagSegment | None
    end_segment: FlagSegment | None
    paragraph_glyphs: list[Glyph]
    width: float
    height: float
    cps: float
    outlines: list[Outline]
    xborder: int
    yborder: int
    xoffset: int
    yoffset: int
    paragraphs: list[Paragraph]
    hyperlink_targets: dict[int, str]
    size: tuple[int, int]
    baseline: int
    textshaders: list[TextShader] | None
    add_left: int
    add_top: int
    add_right: int
    add_bottom: int
    textures: dict[tuple[int, renpy.color.ColorLike | None], Incomplete | renpy.gl2.gl2texture.GLTexture]
    mesh_displayables: list[tuple[Incomplete, Incomplete, Incomplete, Incomplete]]
    displayable_blits: list[tuple[Displayable, int, int]]
    redraw: float | None
    redraw_when_slow: float
    max_time: float
    lines: list[textsupport.Line]
    hyperlinks: list[Incomplete]
    def __init__(
        self,
        text: Text,
        width: float,
        height: float,
        renders: Incomplete,
        size_only: bool = False,
        splits_from: Layout | None = None,
        drawable_res: bool = True,
    ) -> None: ...
    def make_alignment_grid(self, surf: pygame.surface.Surface) -> None: ...
    @overload
    def scale(self, n: None) -> None: ...
    @overload
    def scale(self, n: float) -> float: ...
    @overload
    def scale_int(self, n: None) -> None: ...
    @overload
    def scale_int(self, n: float) -> int: ...
    @overload
    def scale_outline(self, n: None) -> None: ...
    @overload
    def scale_outline(self, n: float) -> int: ...
    def unscale_pair(self, x: float, y: float) -> tuple[float, float]: ...
    def create_text_segments(self, text: Incomplete, ts: Incomplete, style: Incomplete) -> Incomplete: ...
    def segment(
        self, tokens: list[Token], style: renpy.style.StyleCore, renders: Incomplete, text_displayable: Text
    ) -> list[Paragraph]: ...
    def thaic90_paragraph(self, p: Paragraph) -> Paragraph: ...
    def glyphs_paragraph(self, p: Paragraph, direction: int) -> tuple[Paragraph, bool]: ...
    def figure_outlines(self, style: renpy.style.StyleCore) -> tuple[list[Outline], int, int, int, int]: ...
    def blits_typewriter(self, st: float) -> list[Blit]: ...
    def create_mesh_displayable(
        self,
        outline: Incomplete,
        tex: Incomplete,
        lines: Incomplete,
        xo: Incomplete,
        yo: Incomplete,
        depth: Incomplete,
        max_depth: Incomplete,
        ts: Incomplete,
    ) -> Incomplete: ...

LAYOUT_CACHE_SIZE: int
layout_cache_old: dict[int, Layout]
layout_cache_new: dict[int, Layout]
virtual_layout_cache_old: dict[int, Layout]
virtual_layout_cache_new: dict[int, Layout]

def layout_cache_clear() -> None: ...

slow_text: list[Text]

def text_tick() -> None: ...

VERT_REVERSE: Matrix2D
VERT_FORWARD: Matrix2D

class Text(renpy.display.displayable.Displayable):
    __version__: int
    locked: bool
    language: str | None
    mask: str | None
    last_ctc: Incomplete | list[Incomplete] | None
    tokenized: bool
    slow_done_time: float | None
    ctc: Incomplete | None
    text: list[str | renpy.display.displayable.Displayable]
    scope: Incomplete | None
    substitute: bool
    start: Incomplete
    end: Incomplete
    dirty: bool
    def after_upgrade(self, version: int) -> None: ...
    slow: bool | None
    slow_done: Callable[[], None] | None
    displayables: list[renpy.display.displayable.Displayable] | None
    displayable_offsets: Incomplete
    def __init__(
        self,
        text: str | list[str | renpy.display.displayable.Displayable],
        slow: bool | None = None,
        scope: Incomplete | None = None,
        substitute: Incomplete | None = None,
        slow_done: Incomplete | None = None,
        replaces: Incomplete | None = None,
        mask: str | None = None,
        tokenized: bool = False,
        **properties,
    ) -> None: ...
    def get_all_text(self) -> str: ...
    text_parameter: Incomplete
    def set_text(self, text: Any, scope: Any = None, substitute: bool | None = False, update: bool = True) -> bool: ...
    def per_interact(self) -> None: ...
    def set_ctc(self, ctc: Incomplete) -> None: ...
    def set_last_ctc(self, last_ctc: Incomplete) -> None: ...
    focusable: bool
    def update(self) -> None: ...
    def visit(self) -> list[renpy.display.displayable.Displayable]: ...
    def kill_layout(self) -> None: ...
    def get_layout(self) -> Layout | None: ...
    def get_virtual_layout(self) -> Layout | None: ...
    def set_style_prefix(self, prefix: str, root: bool) -> None: ...
    def get_placement(self) -> renpy.display.displayable.Placement: ...
    def focus(self, default: bool = False) -> Any | None: ...
    def unfocus(self, default: bool = False) -> Any | None: ...
    def hyperlink_sensitive(self, target: str) -> bool: ...
    def event(self, ev: Incomplete, x: Incomplete, y: Incomplete, st: Incomplete) -> Incomplete: ...
    def size(self, width: int = 4096, height: int = 4096, st: float = 0, at: float = 0) -> tuple[float, float]: ...
    def get_time(self) -> float: ...
    def render(self, width: Incomplete, height: Incomplete, st: Incomplete, at: Incomplete) -> Incomplete: ...
    def render_blits(self, render: renpy.display.render.Render, layout: Layout, st: float) -> None: ...
    def render_textshader(self, render: renpy.display.render.Render, layout: Layout, st: float, at: float) -> None: ...
    def tokenize(self, text: list[str | renpy.display.displayable.Displayable]) -> list[Token]: ...
    @staticmethod
    def apply_custom_tags(tokens: list[Token]) -> list[Token]: ...
    def get_displayables(
        self, tokens: list[Token]
    ) -> tuple[list[Token], set[renpy.display.displayable.Displayable]]: ...

language_tailor = textsupport.language_tailor
ParameterizedText = extras.ParameterizedText
