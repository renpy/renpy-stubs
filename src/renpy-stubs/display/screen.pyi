from _typeshed import Incomplete
import renpy

profile_log: Incomplete
profile: Incomplete

class ScreenProfile(renpy.object.Object):
    predict: Incomplete
    show: Incomplete
    update: Incomplete
    request: Incomplete
    time: Incomplete
    debug: Incomplete
    const: Incomplete
    def __init__(
        self,
        name,
        predict: bool = False,
        show: bool = False,
        update: bool = False,
        request: bool = False,
        time: bool = False,
        debug: bool = False,
        const: bool = False,
    ) -> None: ...

def get_profile(name): ...

predict_cache: Incomplete

class ScreenCache:
    args: Incomplete
    kwargs: Incomplete
    cache: Incomplete
    def __init__(self, screen, args, kwargs, cache) -> None: ...

cache_put = ScreenCache

def cache_get(screen, args, kwargs): ...

class ScreenNotFound(LookupError):
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def get_suggestion(self): ...

class Screen(renpy.object.Object):
    sensitive: str
    roll_forward: Incomplete
    docstring: Incomplete
    name: Incomplete
    function: Incomplete
    ast: Incomplete
    modal: Incomplete
    zorder: Incomplete
    tag: Incomplete
    predict: Incomplete
    parameters: Incomplete
    location: Incomplete
    layer: Incomplete
    def __init__(
        self,
        name,
        function,
        modal: str = "False",
        zorder: str = "0",
        tag=None,
        predict=None,
        variant=None,
        parameters: bool = False,
        location=None,
        layer: str = "screens",
        sensitive: str = "True",
        roll_forward=None,
        docstring=None,
    ) -> None: ...

PREDICT: int
SHOW: int
UPDATE: int
HIDE: int
OLD: int
phase_name: Incomplete

class ScreenDisplayable(renpy.display.layout.Container):
    nosave: Incomplete
    noreach: Incomplete
    restarting: bool
    hiding: bool
    transient: bool
    screen: Incomplete
    child: Incomplete
    children: Incomplete
    transforms: Incomplete
    widgets: Incomplete
    base_widgets: Incomplete
    old_widgets: Incomplete
    old_transforms: Incomplete
    old_transfers: bool
    hidden_widgets: Incomplete
    cache: Incomplete
    phase: Incomplete
    use_cache: Incomplete
    miss_cache: Incomplete
    copied_from: Incomplete
    profile: Incomplete
    def after_setstate(self) -> None: ...
    properties: Incomplete
    screen_name: Incomplete
    tag: Incomplete
    layer: Incomplete
    scope: Incomplete
    widget_properties: Incomplete
    current_transform_event: Incomplete
    modal: Incomplete
    zorder: Incomplete
    def __init__(
        self, screen, tag, layer, widget_properties={}, scope={}, transient: bool = False, **properties
    ) -> None: ...
    @property
    def name(self): ...
    def visit(self): ...
    def visit_all(self, callback, seen=None) -> None: ...
    def per_interact(self) -> None: ...
    def set_transform_event(self, event) -> None: ...
    def find_focusable(self, callback, focus_name) -> None: ...
    def copy(self): ...
    def update(self): ...
    def render(self, w, h, st, at): ...
    def get_placement(self): ...
    def event(self, ev, x, y, st): ...
    def get_phase_name(self): ...

current_screen_stack: Incomplete

def push_current_screen(screen) -> None: ...
def pop_current_screen() -> None: ...

screens: Incomplete
screens_by_name: Incomplete
updated_screens: Incomplete

def get_screen_variant(name, candidates=None): ...
def get_all_screen_variants(name): ...

analyzed: bool
prepared: bool
sorted_screens: Incomplete
screens_at_sort: Incomplete
use_cycle: Incomplete

def sort_screens(): ...
def sorted_variants(): ...
def analyze_screens() -> None: ...
def prepare_screens() -> None: ...
def define_screen(*args, **kwargs) -> None: ...
def get_screen_layer(name): ...
def get_screen_docstring(name, variant=None): ...
def get_screen(name, layer=None, tag_only: bool = False): ...
def get_screen_variable(name, screen=None, layer=None): ...
def set_screen_variable(name, value, screen=None, layer=None) -> None: ...
def has_screen(name): ...
def get_screen_roll_forward(screen_name): ...
def show_screen(_screen_name, *_args, **kwargs) -> None: ...
def predict_screen(_screen_name, *_args, **kwargs) -> None: ...
def hide_screen(tag, layer=None, immediately: bool = False) -> None: ...
def use_screen(_screen_name, *_args, **kwargs) -> None: ...
def current_screen() -> ScreenDisplayable | None: ...
def get_displayable(screen, id, layer=None, base: bool = False): ...

get_widget = get_displayable

def get_displayable_properties(id, screen=None, layer=None): ...

get_widget_properties = get_displayable_properties

def before_restart() -> None: ...
def show_overlay_screens(suppress_overlay) -> None: ...
def per_frame() -> None: ...
