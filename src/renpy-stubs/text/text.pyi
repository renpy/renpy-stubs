import renpy.pygame as pygame
import renpy.text.extras as extras
import renpy.text.textsupport as textsupport
from _typeshed import Incomplete
from collections.abc import Generator

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
from renpy.text.textsupport import DISPLAYABLE as DISPLAYABLE, PARAGRAPH as PARAGRAPH, TAG as TAG, TEXT as TEXT
from typing import Any, Callable

BASELINE: int
READING_ORDER: Incomplete

class Blit:
    x: Incomplete
    y: Incomplete
    w: Incomplete
    h: Incomplete
    alpha: Incomplete
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    def __init__(
        self,
        x,
        y,
        w,
        h,
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
    def __init__(self, width, height, tex, shader, mesh, uniforms) -> None: ...
    def render(self, width, height, st, at): ...

def outline_blits(blits, outline): ...

class DrawInfo:
    surface: pygame.Surface | None
    override_color: tuple[int, int, int, int] | None
    outline: float
    displayable_blits: list[tuple[renpy.display.displayable.Displayable, int, int]] | None

class TextSegment:
    antialias: Incomplete
    vertical: Incomplete
    font: Incomplete
    size: Incomplete
    bold: Incomplete
    italic: Incomplete
    underline: Incomplete
    strikethrough: Incomplete
    color: Incomplete
    black_color: Incomplete
    hyperlink: Incomplete
    kerning: Incomplete
    cps: Incomplete
    ruby_top: Incomplete
    ruby_bottom: Incomplete
    hinting: Incomplete
    outline_color: Incomplete
    ignore: Incomplete
    default_font: Incomplete
    shaper: Incomplete
    instance: Incomplete
    axis: Incomplete
    shader: Incomplete
    features: Incomplete
    def __init__(self, source=None) -> None: ...
    def take_style(self, style, layout, context=None) -> None: ...
    def glyphs(self, s, layout, level: int = 0): ...
    def draw(self, glyphs, di, xo, yo, layout) -> None: ...
    def assign_times(self, gt, glyphs): ...
    def subsegment(self, s) -> Generator[Incomplete]: ...
    def bounds(self, glyphs, bounds, layout): ...

class SpaceSegment:
    width: Incomplete
    height: Incomplete
    ts: Incomplete
    def __init__(self, ts, width: float = 0.0, height: float = 0.0) -> None: ...
    def glyphs(self, s, layout): ...
    def bounds(self, glyphs, bounds, layout): ...
    def draw(self, glyphs, di, xo, yo, layout) -> None: ...
    def assign_times(self, gt, glyphs): ...

class DisplayableSegment:
    d: Incomplete
    hyperlink: Incomplete
    cps: Incomplete
    ruby_top: Incomplete
    ruby_bottom: Incomplete
    shader: Incomplete
    def __init__(self, ts, d, renders) -> None: ...
    def glyphs(self, s, layout): ...
    def draw(self, glyphs, di, xo, yo, layout) -> None: ...
    def assign_times(self, gt, glyphs): ...
    def bounds(self, glyphs, bounds, layout): ...

class FlagSegment:
    def glyphs(self, s, layout): ...
    def draw(self, glyphs, di, xo, yo, layout) -> None: ...
    def assign_times(self, gt, glyphs): ...
    def bounds(self, glyphs, bounds, layout): ...

class Layout:
    oversample: Incomplete
    reverse: Incomplete
    forward: Incomplete
    outline_step: Incomplete
    pixel_perfect: bool
    line_overlap_split: Incomplete
    has_hyperlinks: bool
    has_ruby: bool
    start_segment: Incomplete
    end_segment: Incomplete
    paragraph_glyphs: Incomplete
    width: Incomplete
    height: Incomplete
    cps: Incomplete
    outlines: Incomplete
    xborder: Incomplete
    yborder: Incomplete
    xoffset: Incomplete
    yoffset: Incomplete
    paragraphs: Incomplete
    hyperlink_targets: Incomplete
    size: Incomplete
    baseline: Incomplete
    textshaders: Incomplete
    add_left: Incomplete
    add_top: Incomplete
    add_right: Incomplete
    add_bottom: Incomplete
    textures: Incomplete
    mesh_displayables: Incomplete
    displayable_blits: Incomplete
    redraw: Incomplete
    redraw_when_slow: float
    max_time: Incomplete
    lines: Incomplete
    hyperlinks: Incomplete
    def __init__(
        self, text, width, height, renders, size_only: bool = False, splits_from=None, drawable_res: bool = True
    ) -> None: ...
    def make_alignment_grid(self, surf) -> None: ...
    def scale(self, n): ...
    def scale_int(self, n): ...
    def scale_outline(self, n): ...
    def unscale_pair(self, x, y): ...
    def create_text_segments(self, text, ts, style): ...
    def segment(self, tokens, style, renders, text_displayable): ...
    def thaic90_paragraph(self, p): ...
    def glyphs_paragraph(self, p, direction): ...
    def figure_outlines(self, style): ...
    def blits_typewriter(self, st): ...
    def create_mesh_displayable(self, outline, tex, lines, xo, yo, depth, max_depth, ts): ...

LAYOUT_CACHE_SIZE: int
layout_cache_old: Incomplete
layout_cache_new: Incomplete
virtual_layout_cache_old: Incomplete
virtual_layout_cache_new: Incomplete

def layout_cache_clear() -> None: ...

slow_text: Incomplete

def text_tick() -> None: ...

VERT_REVERSE: Incomplete
VERT_FORWARD: Incomplete

class Text(renpy.display.displayable.Displayable):
    __version__: int
    locked: bool
    language: Incomplete
    mask: Incomplete
    last_ctc: Incomplete
    tokenized: bool
    slow_done_time: Incomplete
    ctc: Incomplete
    text: Incomplete
    scope: Incomplete
    substitute: bool
    start: Incomplete
    end: Incomplete
    dirty: bool
    def after_upgrade(self, version) -> None: ...
    slow: Incomplete
    slow_done: Callable | None
    displayables: Incomplete
    displayable_offsets: Incomplete
    def __init__(
        self,
        text,
        slow=None,
        scope=None,
        substitute=None,
        slow_done=None,
        replaces=None,
        mask=None,
        tokenized: bool = False,
        **properties,
    ) -> None: ...
    def get_all_text(self): ...
    text_parameter: Incomplete
    def set_text(self, text: Any, scope: Any = None, substitute: bool | None = False, update: bool = True) -> bool: ...
    def per_interact(self) -> None: ...
    def set_ctc(self, ctc) -> None: ...
    def set_last_ctc(self, last_ctc) -> None: ...
    focusable: bool
    def update(self) -> None: ...
    def visit(self): ...
    def kill_layout(self) -> None: ...
    def get_layout(self): ...
    def get_virtual_layout(self): ...
    def set_style_prefix(self, prefix, root) -> None: ...
    def get_placement(self): ...
    def focus(self, default: bool = False): ...
    def unfocus(self, default: bool = False): ...
    def hyperlink_sensitive(self, target): ...
    def event(self, ev, x, y, st): ...
    def size(self, width: int = 4096, height: int = 4096, st: int = 0, at: int = 0): ...
    def get_time(self): ...
    def render(self, width, height, st, at): ...
    def render_blits(self, render, layout, st) -> None: ...
    def render_textshader(self, render, layout, st, at) -> None: ...
    def tokenize(self, text): ...
    @staticmethod
    def apply_custom_tags(tokens): ...
    def get_displayables(self, tokens): ...

language_tailor = textsupport.language_tailor
ParameterizedText = extras.ParameterizedText
