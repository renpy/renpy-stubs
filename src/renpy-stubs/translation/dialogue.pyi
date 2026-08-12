from renpy.translation import quote_unicode as quote_unicode
from typing import TextIO

def create_dialogue_map(language: str) -> dict[str, str]: ...
def notags_filter(s: str) -> str: ...
def combine_filter(s: str) -> str: ...
def what_filter(s: str) -> str: ...

class DialogueFile:
    filename: str
    tdf: bool
    notags: bool
    escape: bool
    strings: bool
    language: str | None
    f: TextIO
    def __init__(
        self,
        filename: str,
        output: str,
        tdf: bool = True,
        strings: bool = False,
        notags: bool = True,
        escape: bool = True,
        language: str | None = None,
    ) -> None: ...
    def write_dialogue(self) -> None: ...
    def get_strings(self) -> list[list[str]]: ...

def dialogue_command() -> bool: ...
