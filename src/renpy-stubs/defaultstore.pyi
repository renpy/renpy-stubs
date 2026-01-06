from renpy.minstore import *
import renpy
import renpy.display.anim as anim
from _typeshed import Incomplete as Incomplete

main_menu: bool

class _Config(object):
    def __getattr__(self, name: Incomplete) -> Incomplete: ...
    def __setattr__(self, name: Incomplete, value: Incomplete) -> None: ...
    def __delattr__(self, name: Incomplete) -> None: ...

style: Incomplete
config: Incomplete
library = config
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
Alpha: Incomplete
Position: Incomplete
Pan: Incomplete
Move: Incomplete
Motion: Incomplete
Revolve: Incomplete
Zoom: Incomplete
RotoZoom: Incomplete
FactorZoom: Incomplete
SizeZoom: Incomplete
Fade: Incomplete
Dissolve: Incomplete
ImageDissolve: Incomplete
AlphaDissolve: Incomplete
CropMove: Incomplete
PushMove: Incomplete
Pixellate: Incomplete
OldMoveTransition: Incomplete
MoveTransition: Incomplete
MoveFactory: Incomplete
MoveIn: Incomplete
MoveOut: Incomplete
ZoomInOut: Incomplete
RevolveInOut: Incomplete
MultipleTransition: Incomplete
ComposeTransition: Incomplete
Pause: Incomplete
SubTransition: Incomplete
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

class _layout_class(__builtins__["object"]):
    cls: Incomplete
    nargs: Incomplete
    extra_kwargs: Incomplete
    __doc__: Incomplete
    def __init__(self, cls: Incomplete, doc: Incomplete, nargs: int = 0, **extra_kwargs: Incomplete) -> None: ...
    def __call__(self, *args, **properties) -> Incomplete: ...

Fixed: Incomplete
HBox: Incomplete
VBox: Incomplete
Grid: Incomplete

def AlphaBlend(control: Incomplete, old: Incomplete, new: Incomplete, alpha: bool = False) -> Incomplete: ...
def At(d: Incomplete, *args) -> Incomplete: ...

Color = renpy.color.Color
color = renpy.color.Color
menu = renpy.exports.display_menu
predict_menu = renpy.exports.predict_menu
default_transition: Incomplete
mouse_visible: bool
suppress_overlay: bool
adv: Incomplete

def predict_say(who: Incomplete, what: Incomplete) -> None: ...
def say(who: Incomplete, what: Incomplete, interact: bool = True, *args, **kwargs) -> None: ...
