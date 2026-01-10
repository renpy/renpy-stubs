from renpy.minstore import *
import renpy
import renpy.display.anim as anim
from _typeshed import Incomplete as Incomplete
from renpy.curry import Partial as Partial
from renpy.display.displayable import Displayable as Displayable
from renpy.types import DisplayableLike as DisplayableLike
from typing import Any

_restart: Incomplete
_return: Any | None
_args: tuple[Any, ...] | None
_kwargs: dict[str, Any] | None
_window: bool
_window_subtitle: str
_rollback: bool
_begin_rollback: bool
_skipping: bool
_dismiss_pause: bool
_config = renpy.config
_widget_by_id: Incomplete
_widget_properties: dict[str, Any]
_text_rect: Incomplete | None
_menu: bool
main_menu: bool
_autosave: bool
_live2d_fade: bool

class _Config(object):
    def __getstate__(self) -> None: ...
    def __setstate__(self, data) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

style: Incomplete | None
config: _Config
library: _Config
eval = renpy.python.py_eval
Bar = renpy.display.behavior.Bar
Button = renpy.display.behavior.Button
ImageButton = renpy.display.behavior.ImageButton
Input = renpy.display.behavior.Input
TextButton = renpy.display.behavior.TextButton
ImageReference = renpy.display.image.ImageReference
DynamicImage = renpy.display.image.DynamicImage
Image = renpy.display.im.image
Frame = renpy.display.imagelike.Frame
Borders = renpy.display.imagelike.Borders
Solid = renpy.display.imagelike.Solid
FileCurrentScreenshot = renpy.display.imagelike.FileCurrentScreenshot
LiveComposite: Incomplete
LiveCrop: Incomplete
LiveTile: Incomplete
Composite = renpy.display.layout.Composite
Crop = renpy.display.layout.Crop
Tile = renpy.display.layout.Tile
Flatten = renpy.display.layout.Flatten
Null = renpy.display.layout.Null
Window = renpy.display.layout.Window
Viewport = renpy.display.viewport.Viewport
DynamicDisplayable = renpy.display.layout.DynamicDisplayable
ConditionSwitch = renpy.display.layout.ConditionSwitch
ShowingSwitch = renpy.display.layout.ShowingSwitch
AlphaMask = renpy.display.layout.AlphaMask
Layer = renpy.display.layout.Layer
Transform = renpy.display.transform.Transform
Camera = renpy.display.transform.Camera
Animation = anim.Animation
Movie = renpy.display.video.Movie
Particles = renpy.display.particle.Particles
SnowBlossom = renpy.display.particle.SnowBlossom
Text = renpy.text.text.Text
ParameterizedText = renpy.text.extras.ParameterizedText
FontGroup = renpy.text.font.FontGroup
Drag = renpy.display.dragdrop.Drag
DragGroup = renpy.display.dragdrop.DragGroup
Sprite = renpy.display.particle.Sprite
SpriteManager = renpy.display.particle.SpriteManager
Matrix = renpy.display.matrix.Matrix
Live2D = renpy.gl2.live2d.Live2D
Model = renpy.display.model.Model
GLTFModel = renpy.gl2.assimp.GLTFModel
Alpha: Partial[Partial[renpy.display.layout.Alpha]]
Position: Partial[Partial[renpy.display.layout.Position]]
Pan: Partial[Partial[renpy.display.motion.Motion]]
Move: Partial[Partial[renpy.display.motion.Motion]]
Motion: Partial[Partial[renpy.display.motion.Motion]]
Revolve: Partial[Partial[renpy.display.motion.Motion]]
Zoom: Partial[Partial[renpy.display.motion.Zoom]]
RotoZoom: Partial[Partial[renpy.display.motion.RotoZoom]]
FactorZoom: Partial[Partial[renpy.display.motion.FactorZoom]]
SizeZoom: Partial[Partial[renpy.display.motion.SizeZoom]]
Fade: Partial[Partial[renpy.display.transition.MultipleTransition]]
Dissolve: Partial[Partial[renpy.display.transition.Dissolve]]
ImageDissolve: Partial[Partial[renpy.display.transition.ImageDissolve]]
AlphaDissolve: Partial[Partial[renpy.display.transition.AlphaDissolve]]
CropMove: Partial[Partial[renpy.display.transition.CropMove]]
PushMove: Partial[Partial[renpy.display.transition.PushMove]]
Pixellate: Partial[Partial[renpy.display.transition.Pixellate]]
OldMoveTransition: Partial[Partial[renpy.display.movetransition.MultiBox]]
MoveTransition: Partial[Partial[Incomplete]]
MoveFactory: Partial[Partial[renpy.display.movetransition.MultiBox]]
MoveIn: Partial[Partial[Incomplete]]
MoveOut: Partial[Partial[Incomplete]]
ZoomInOut: Partial[Partial[Incomplete]]
RevolveInOut: Partial[Partial[Incomplete]]
MultipleTransition: Partial[Partial[renpy.display.transition.MultipleTransition]]
ComposeTransition: Partial[Partial[Displayable]]
Pause: Partial[Partial[renpy.display.transition.NoTransition]]
SubTransition: Partial[Partial[renpy.display.transition.NoTransition]]
ADVSpeaker = renpy.character.ADVCharacter
ADVCharacter = renpy.character.ADVCharacter
Speaker = renpy.character.Character
Character = renpy.character.Character
DynamicCharacter = renpy.character.DynamicCharacter
MultiPersistent = renpy.persistent.MultiPersistent
Action = renpy.ui.Action
BarValue = renpy.ui.BarValue
AudioData = renpy.audio.audio.AudioData
Style: Incomplete
SlottedNoRollback = renpy.rollback.SlottedNoRollback
NoRollback = renpy.rollback.NoRollback

class _layout_class[T: renpy.display.layout.Container](__builtins__["object"]):
    cls: type[T]
    nargs: int
    extra_kwargs: Incomplete
    __doc__: Incomplete
    def __init__(self, cls: type[T], doc: str | None, nargs: int = 0, **extra_kwargs) -> None: ...
    def __call__(self, *args, **properties) -> T: ...

Fixed: _layout_class[renpy.display.layout.MultiBox]
HBox: _layout_class[renpy.display.layout.MultiBox]
VBox: _layout_class[renpy.display.layout.MultiBox]
Grid: _layout_class[renpy.display.layout.Grid]

def AlphaBlend(
    control: DisplayableLike, old: Displayable | None, new: Displayable | None, alpha: bool = False
) -> renpy.display.transition.AlphaDissolve: ...
def At(d: DisplayableLike, *args: renpy.display.scenelists.AtType) -> Displayable: ...

Color = renpy.color.Color
color = renpy.color.Color
menu = renpy.exports.display_menu
predict_menu = renpy.exports.predict_menu
default_transition: Incomplete
mouse_visible: bool
suppress_overlay: bool
adv: ADVCharacter

def predict_say(who: Incomplete, what: Incomplete) -> None: ...
def say(who: Incomplete, what: Incomplete, interact: bool = True, *args, **kwargs) -> None: ...

_last_say_who: Incomplete
_last_say_what: Incomplete
_last_say_args: Incomplete
_last_say_kwargs: Incomplete
_cache_pin_set: Incomplete
_predict_set: Incomplete
_predict_screen: Incomplete
_overlay_screens: Incomplete
_in_replay: Incomplete
_side_image_attributes: Incomplete
_side_image_attributes_reset: bool
_ignore_action: Incomplete
_quit_slot: Incomplete
_screenshot_pattern: Incomplete
