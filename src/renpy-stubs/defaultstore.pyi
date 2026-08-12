from typing import Any

import renpy
from _typeshed import Incomplete as Incomplete
from renpy.curry import Partial as Partial
from renpy.display import anim
from renpy.display.displayable import Displayable as Displayable
from renpy.minstore import *
from renpy.types import DisplayableLike as DisplayableLike

_restart: tuple[Any | None, str, str] | None
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
_widget_by_id: dict[str, renpy.display.displayable.Displayable] | None
_widget_properties: dict[str, Any]
_text_rect: tuple[int, int, int, int] | None
_menu: bool
main_menu: bool
_autosave: bool
_live2d_fade: bool

class _Config:
    def __getstate__(self) -> None: ...
    def __setstate__(self, data: dict[str, Any]) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

style: renpy.style.StyleCore | None
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
LiveComposite: type[renpy.display.layout.LiveComposite]
LiveCrop: type[renpy.display.layout.LiveCrop]
LiveTile: type[renpy.display.layout.LiveTile]
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
MoveTransition: Partial[Partial[renpy.display.movetransition.MultiBox]]
MoveFactory: Partial[Partial[renpy.display.movetransition.MultiBox]]
MoveIn: Partial[Partial[renpy.display.motion.Motion]]
MoveOut: Partial[Partial[renpy.display.motion.Motion]]
ZoomInOut: Partial[Partial[renpy.display.motion.FactorZoom]]
RevolveInOut: Partial[Partial[renpy.display.motion.Revolve]]
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
Style: type[renpy.styledata.styleclass.Style]
SlottedNoRollback = renpy.rollback.SlottedNoRollback
NoRollback = renpy.rollback.NoRollback

class _layout_class[T: renpy.display.layout.Container](__builtins__["object"]):
    cls: type[T]
    nargs: int
    extra_kwargs: dict[str, Any]
    __doc__: str | None
    def __init__(self, cls: type[T], doc: str | None, nargs: int = 0, **extra_kwargs) -> None: ...
    def __call__(self, *args: DisplayableLike, **properties: Any) -> T: ...

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
default_transition: renpy.display.transition.TransitionFunction | None
mouse_visible: bool
suppress_overlay: bool
adv: ADVCharacter

def predict_say(who: Any, what: str) -> None: ...
def say(who: Any, what: str, interact: bool = True, *args: Any, **kwargs: Any) -> None: ...

_last_say_who: Any | None
_last_say_what: str | None
_last_say_args: tuple[Any, ...] | None
_last_say_kwargs: dict[str, Any] | None
_cache_pin_set: set[str] | None
_predict_set: set[str] | None
_predict_screen: str | None
_overlay_screens: list[str] | None
_in_replay: bool | None
_side_image_attributes: tuple[str, ...] | None
_side_image_attributes_reset: bool
_ignore_action: Any | None
_quit_slot: str | None
_screenshot_pattern: str | None

__all__ = [
    "ADVSpeaker",
    "Action",
    "Alpha",
    "AlphaBlend",
    "AlphaDissolve",
    "AlphaMask",
    "Animation",
    "At",
    "AudioData",
    "Bar",
    "BarValue",
    "Borders",
    "Button",
    "Camera",
    "Color",
    "ComposeTransition",
    "Composite",
    "ConditionSwitch",
    "Crop",
    "CropMove",
    "Dissolve",
    "Drag",
    "DragGroup",
    "DynamicCharacter",
    "DynamicDisplayable",
    "DynamicImage",
    "FactorZoom",
    "Fade",
    "FileCurrentScreenshot",
    "Fixed",
    "Flatten",
    "FontGroup",
    "Frame",
    "GLTFModel",
    "Grid",
    "HBox",
    "Image",
    "ImageButton",
    "ImageDissolve",
    "ImageReference",
    "Input",
    "Layer",
    "Live2D",
    "LiveComposite",
    "LiveCrop",
    "LiveTile",
    "Matrix",
    "Model",
    "Motion",
    "Move",
    "MoveFactory",
    "MoveIn",
    "MoveOut",
    "MoveTransition",
    "Movie",
    "MultiPersistent",
    "MultipleTransition",
    "NoRollback",
    "Null",
    "OldMoveTransition",
    "Pan",
    "ParameterizedText",
    "Particles",
    "Pause",
    "Pixellate",
    "Position",
    "PushMove",
    "Revolve",
    "RevolveInOut",
    "RotoZoom",
    "ShowingSwitch",
    "SizeZoom",
    "SlottedNoRollback",
    "SnowBlossom",
    "Solid",
    "Speaker",
    "Sprite",
    "SpriteManager",
    "SubTransition",
    "Text",
    "TextButton",
    "Tile",
    "Transform",
    "VBox",
    "Viewport",
    "Window",
    "Zoom",
    "ZoomInOut",
    "_Config",
    "_args",
    "_autosave",
    "_begin_rollback",
    "_cache_pin_set",
    "_config",
    "_dismiss_pause",
    "_ignore_action",
    "_in_replay",
    "_kwargs",
    "_last_say_args",
    "_last_say_kwargs",
    "_last_say_what",
    "_last_say_who",
    "_layout_class",
    "_live2d_fade",
    "_menu",
    "_overlay_screens",
    "_predict_screen",
    "_predict_set",
    "_quit_slot",
    "_restart",
    "_return",
    "_rollback",
    "_screenshot_pattern",
    "_side_image_attributes",
    "_side_image_attributes_reset",
    "_skipping",
    "_text_rect",
    "_widget_by_id",
    "_widget_properties",
    "_window",
    "_window_subtitle",
    "adv",
    "color",
    "config",
    "default_transition",
    "eval",
    "library",
    "main_menu",
    "menu",
    "mouse_visible",
    "predict_menu",
    "predict_say ",
    "say",
    "style",
    "suppress_overlay",
]

Matrix: type[renpy.display.matrix.Matrix]
GLTFModel: type[renpy.gl2.assimp.GLTFModel]
