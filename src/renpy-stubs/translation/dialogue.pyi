from _typeshed import Incomplete as Incomplete
from renpy.translation import quote_unicode as quote_unicode

def create_dialogue_map(language: Incomplete) -> Incomplete: ...
def notags_filter(s: Incomplete) -> Incomplete: ...
def combine_filter(s: Incomplete) -> Incomplete: ...
def what_filter(s: Incomplete) -> Incomplete: ...

class DialogueFile:
    filename: Incomplete
    tdf: Incomplete
    notags: Incomplete
    escape: Incomplete
    strings: Incomplete
    language: Incomplete
    f: Incomplete
    def __init__(
        self,
        filename: Incomplete,
        output: Incomplete,
        tdf: bool = True,
        strings: bool = False,
        notags: bool = True,
        escape: bool = True,
        language: Incomplete = None,
    ) -> None: ...
    def write_dialogue(self) -> Incomplete: ...
    def get_strings(self) -> Incomplete: ...

def dialogue_command() -> Incomplete: ...
