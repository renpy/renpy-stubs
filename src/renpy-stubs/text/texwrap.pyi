from _frozen_importlib import BuiltinImporter as BuiltinImporter
from dataclasses import dataclass
from renpy.text.textsupport import Glyph

@dataclass
class Word:
    glyph: list[Glyph]
    start_x: float
    end_x: float

class WordWrapper:
    words: list[Word]
    len_words: int
    glyphs: list[Glyph]
    scores: list[float]
    splits: list[int]

    def __init__(self, glyphs: list[Glyph], first_width: int, rest_width: int, subtitle: bool) -> None: ...
    def __dealloc__(self) -> None: ...
    def unmark_splits(self) -> None: ...
    def knuth_plass(self, first_width: int, rest_width: int, subtitle: bool) -> None: ...
    def make_word_list(self, glyphs: list[Glyph]) -> None: ...

def linebreak_tex(glyphs: list[Glyph], first_width: int, rest_width: int, subtitle: bool) -> None: ...
