from _typeshed import Incomplete

emulator: Incomplete
overlay: Incomplete
ios: bool

def null_emulator(ev, x, y): ...

TOUCH_KEYS: Incomplete

def touch_emulator(ev, x, y): ...

TV_KEYS: Incomplete

def tv_emulator(ev, x, y): ...

keyboard: Incomplete
null: Incomplete

def dynamic_keyboard(st, at): ...
def init_emulator() -> None: ...
def early_init_emulator() -> None: ...
