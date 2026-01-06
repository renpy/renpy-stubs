import renpy
import renpy.pygame as pygame
import renpy.text.extras as extras
import renpy.text.textsupport as textsupport
from _typeshed import Incomplete as Incomplete
from collections.abc import Generator
from renpy.display.displayable import Displayable as Displayable
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
from typing import Any

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
        x: Incomplete,
        y: Incomplete,
        w: Incomplete,
        h: Incomplete,
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
    surface: pygame.Surface | None
    override_color: tuple[int, int, int, int] | None
    outline: float
    displayable_blits: list[tuple[Displayable, int, int]] | None

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
    def __init__(self, source: Incomplete = None) -> None: ...
    def take_style(self, style: Incomplete, layout: Incomplete, context: Incomplete = None) -> None: ...
    def glyphs(self, s: Incomplete, layout: Incomplete, level: int = 0) -> Incomplete: ...
    def draw(self, glyphs: Incomplete, di: Incomplete, xo: Incomplete, yo: Incomplete, layout: Incomplete) -> None: ...
    def assign_times(self, gt: Incomplete, glyphs: Incomplete) -> None: ...
    def subsegment(self, s: Incomplete) -> Generator[Incomplete]: ...
    def bounds(self, glyphs: Incomplete, bounds: Incomplete, layout: Incomplete) -> None: ...

class SpaceSegment:
    width: Incomplete
    height: Incomplete
    ts: Incomplete
    def __init__(self, ts: Incomplete, width: float = 0.0, height: float = 0.0) -> None: ...
    def glyphs(self, s: Incomplete, layout: Incomplete) -> Incomplete: ...
    def bounds(self, glyphs: Incomplete, bounds: Incomplete, layout: Incomplete) -> None: ...
    def draw(self, glyphs: Incomplete, di: Incomplete, xo: Incomplete, yo: Incomplete, layout: Incomplete) -> None: ...
    def assign_times(self, gt: Incomplete, glyphs: Incomplete) -> None: ...

class DisplayableSegment:
    d: Incomplete
    hyperlink: Incomplete
    cps: Incomplete
    ruby_top: Incomplete
    ruby_bottom: Incomplete
    shader: Incomplete
    def __init__(self, ts: Incomplete, d: Incomplete, renders: Incomplete) -> None: ...
    def glyphs(self, s: Incomplete, layout: Incomplete) -> Incomplete: ...
    def draw(self, glyphs: Incomplete, di: Incomplete, xo: Incomplete, yo: Incomplete, layout: Incomplete) -> None: ...
    def assign_times(self, gt: Incomplete, glyphs: Incomplete) -> None: ...
    def bounds(self, glyphs: Incomplete, bounds: Incomplete, layout: Incomplete) -> None: ...

class FlagSegment:
    def glyphs(self, s: Incomplete, layout: Incomplete) -> Incomplete: ...
    def draw(self, glyphs: Incomplete, di: Incomplete, xo: Incomplete, yo: Incomplete, layout: Incomplete) -> None: ...
    def assign_times(self, gt: Incomplete, glyphs: Incomplete) -> None: ...
    def bounds(self, glyphs: Incomplete, bounds: Incomplete, layout: Incomplete) -> None: ...

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
        self,
        text: Incomplete,
        width: Incomplete,
        height: Incomplete,
        renders: Incomplete,
        size_only: bool = False,
        splits_from: Incomplete = None,
        drawable_res: bool = True,
    ) -> None: ...
    def make_alignment_grid(self, surf: Incomplete) -> None: ...
    def scale(self, n: Incomplete) -> Incomplete: ...
    def scale_int(self, n: Incomplete) -> Incomplete: ...
    def scale_outline(self, n: Incomplete) -> Incomplete: ...
    def unscale_pair(self, x: Incomplete, y: Incomplete) -> Incomplete: ...
    def create_text_segments(self, text: Incomplete, ts: Incomplete, style: Incomplete) -> Incomplete: ...
    def segment(
        self, tokens: Incomplete, style: Incomplete, renders: Incomplete, text_displayable: Incomplete
    ) -> Incomplete: ...
    def thaic90_paragraph(self, p: Incomplete) -> Incomplete: ...
    def glyphs_paragraph(self, p: Incomplete, direction: Incomplete) -> Incomplete: ...
    def figure_outlines(self, style: Incomplete) -> Incomplete: ...
    def blits_typewriter(self, st: Incomplete) -> Incomplete: ...
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
    def after_upgrade(self, version: int) -> None: ...
    slow: Incomplete
    slow_done: Callable | None
    displayables: Incomplete
    displayable_offsets: Incomplete
    def __init__(
        self,
        text: Incomplete,
        slow: Incomplete = None,
        scope: Incomplete = None,
        substitute: Incomplete = None,
        slow_done: Incomplete = None,
        replaces: Incomplete = None,
        mask: Incomplete = None,
        tokenized: bool = False,
        **properties,
    ) -> None: ...
    def get_all_text(self) -> Incomplete: ...
    text_parameter: Incomplete
    def set_text(self, text: Any, scope: Any = None, substitute: bool | None = False, update: bool = True) -> bool: ...
    def per_interact(self) -> None: ...
    def set_ctc(self, ctc: Incomplete) -> None: ...
    def set_last_ctc(self, last_ctc: Incomplete) -> None: ...
    focusable: bool
    def update(self) -> None: ...
    def visit(self) -> Incomplete: ...
    def kill_layout(self) -> None: ...
    def get_layout(self) -> Incomplete: ...
    def get_virtual_layout(self) -> Incomplete: ...
    def set_style_prefix(self, prefix: Incomplete, root: Incomplete) -> None: ...
    def get_placement(self) -> Incomplete: ...
    def focus(self, default: bool = False) -> Incomplete: ...
    def unfocus(self, default: bool = False) -> Incomplete: ...
    def hyperlink_sensitive(self, target: Incomplete) -> Incomplete: ...
    def event(self, ev: Incomplete, x: Incomplete, y: Incomplete, st: Incomplete) -> Incomplete: ...
    def size(self, width: int = 4096, height: int = 4096, st: int = 0, at: int = 0) -> Incomplete: ...
    def get_time(self) -> Incomplete: ...
    def render(self, width: Incomplete, height: Incomplete, st: Incomplete, at: Incomplete) -> Incomplete: ...
    def render_blits(self, render: Incomplete, layout: Incomplete, st: Incomplete) -> None: ...
    def render_textshader(self, render: Incomplete, layout: Incomplete, st: Incomplete, at: Incomplete) -> None: ...
    def tokenize(self, text: Incomplete) -> Incomplete: ...
    @staticmethod
    def apply_custom_tags(tokens: Incomplete) -> Incomplete: ...
    def get_displayables(self, tokens: Incomplete) -> Incomplete: ...

language_tailor = textsupport.language_tailor
ParameterizedText = extras.ParameterizedText
