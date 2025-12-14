from _typeshed import Incomplete
from renpy.compat import (
    PY2 as PY2,
    basestring as basestring,
    bchr as bchr,
    bord as bord,
    chr as chr,
    open as open,
    pystr as pystr,
    range as range,
    round as round,
    str as str,
    tobytes as tobytes,
    unicode as unicode,
)
from renpy.text.textsupport import DISPLAYABLE as DISPLAYABLE, PARAGRAPH as PARAGRAPH, TAG as TAG

text_tags: Incomplete

def check_text_tags(s, check_unclosed: bool = False): ...
def filter_text_tags(s, allow=None, deny=None): ...
def filter_alt_text(s) -> str: ...

class ParameterizedText:
    style: Incomplete
    properties: Incomplete
    def __init__(self, style: str = "default", **properties) -> None: ...

def textwrap(s, width: int = 78, asian: bool = False): ...
def thaic90(s): ...
