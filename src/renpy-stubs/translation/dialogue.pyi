from _typeshed import Incomplete
from renpy.translation import quote_unicode as quote_unicode

def create_dialogue_map(language): ...
def notags_filter(s): ...
def combine_filter(s): ...
def what_filter(s): ...

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
        filename,
        output,
        tdf: bool = True,
        strings: bool = False,
        notags: bool = True,
        escape: bool = True,
        language=None,
    ) -> None: ...
    def write_dialogue(self): ...
    def get_strings(self): ...

def dialogue_command(): ...
