from typing import Any, Callable, Literal, IO, Protocol, TypedDict, Unpack, NotRequired, type_check_only
import re
import collections
from _typeshed import Incomplete as Incomplete

import renpy
from renpy.display.transform import Transform
from renpy.error import TracebackException as TracebackException
from renpy.text.shader import TextShader as TextShader
from renpy.types import DisplayableLike, Unused

locked: bool
window_title: str | None
window_icon: str | None
windows_icon: str | None
screen_width: int
screen_height: int
sound: bool
debug: bool
debug_sound: bool
rollback_enabled: bool
rollback_length: int
keep_rollback_data: bool
fix_rollback_without_choice: bool
hard_rollback_limit: int
overlay_functions: list[Callable[[], None]]
underlay: list[renpy.display.displayable.Displayable]
profile: bool
savedir: str | None
image_cache_size: int | None
image_cache_size_mb: int
preload_threads: int
preload_thread_autocap: int
predict_statements: int
debug_image_cache: bool
allow_skipping: bool
fast_skipping: bool
skipping: Literal["slow", "fast", None]
skip_delay: int
archives: list[str]
searchpath: list[str]
force_archives: bool
mouse: dict[str, list[tuple[str, int, int]]] | None
sound_sample_rate: int
fadeout_audio: float
fade_music: float | None
sticky_positions: bool
layers: list[str]
transient_layers: list[str]
overlay_layers: list[str]
context_clear_layers: list[str]
top_layers: list[str]
bottom_layers: list[str]
sticky_layers: list[str]
detached_layers: list[str]
overlay_during_with: bool
enable_fast_dissolve: bool
focus_crossrange_penalty: int
load_before_transition: bool
keymap: dict[str, list[str]]
default_keymap: dict[str, list[str]]
joystick: bool
interact_callbacks: list[Callable[[], None]]
start_interact_callbacks: list[Callable[[], None]]
say_sustain_callbacks: list[Callable[[], None]]
say_allow_dismiss: Callable[[], bool] | None
text_tokenizer: Unused | None
afm_characters: int
afm_bonus: int
afm_callback: Callable[[], bool] | None
auto_choice_delay: float | None
font_replacement_map: dict[tuple[str, bool, bool], tuple[str, bool, bool]]
with_callback: (
    Callable[
        [renpy.display.transition.TransitionFunction, renpy.display.transition.TransitionFunction | None],
        renpy.display.transition.TransitionFunction,
    ]
    | None
)
framerate: int
frames: int
editor: Unused
editor_transient: Unused
editor_file_separator: Unused
developer: bool
original_developer: Literal["auto"] | bool
default_developer: bool
log: str | None
clear_log: bool
lint_hooks: list[Callable[[], None]]
hyperlink_styler: Callable[[str], renpy.style.StyleCore] | None
hyperlink_callback: Callable[[str], Any | None] | None
hyperlink_focus: Callable[[str], Any | None] | None
recolor_sfonts: bool
text_layout: Unused
periodic_callback: Callable[[], None] | None
periodic_callbacks: list[Callable[[], None]]
check_properties: bool
implicit_with_none: bool
layer_clipping: dict[str, tuple[int, int, int, int]]
disable_fullscreen_opt: bool
reject_midi: bool

@type_check_only
class CharacterCallbackParameters(TypedDict):
    interact: bool
    type: Literal["nvl", "adv", "bubble"]
    what: str
    multiple: Incomplete

    start: NotRequired[int]
    end: NotRequired[int]
    delay: NotRequired[float | None]
    last_segment: NotRequired[bool]

    exception: bool
    please_ignore_unknown_keyword_arguments: NotRequired[None]

@type_check_only
class CharacterCallback(Protocol):
    def __call__(
        self,
        event: Literal["begin", "show", "show_done", "slow_done", "interact_done", "end"],
        **kwargs: Unpack[CharacterCallbackParameters],
    ) -> None: ...

character_callback: CharacterCallback | None
all_character_callbacks: list[CharacterCallback]
has_autosave: bool
autosave_slots: int
autosave_frequency: int
scene: Callable[[str | None], None] | None
show: Incomplete | None
hide: Incomplete | None
use_cpickle: bool
inspector: Callable[[list[tuple[int, int, int, renpy.display.displayable.Displayable]]], None] | None
reject_backslash: bool
mouse_hide_time: int
missing_image_callback: Callable[[str], renpy.display.im.ImageBase | None] | None
say_menu_text_filter: Callable[[str], str] | None
label_overrides: dict[renpy.ast.NodeName, renpy.ast.NodeName]
auto_save_extra_info: Callable[[], str] | None
save_directory: str | None
missing_scene: Callable[[str], bool] | None
missing_show: Callable[[tuple[str, ...], tuple[str, ...], str], renpy.display.displayable.Displayable] | None
missing_hide: Callable[[tuple[str, ...], str], bool] | None
label_callback: Callable[[str, bool], None] | None
label_callbacks: list[Callable[[str, bool], None]]
empty_window: Callable[[], None] | None
window_overlay_functions: list[Callable[[], None]]
rtl: bool
file_open_callback: Callable[[str], IO | None] | None
thumbnail_width: int
thumbnail_height: int
end_game_transition: Incomplete | None
default_transform: renpy.display.transform.Transform | None
transform_uses_child_position: bool
quit_action: renpy.display.behavior.ActionType | None
screenshot_crop: renpy.pygame.rect.RectLike | None
gamedir: str
basedir: str
renpy_base: str
commondir: str | None
logdir: str | None
gl_enable: bool
mode_callbacks: list[Callable[[str, list[str]], None]]
movetransition_respects_offsets: bool
imagereference_respects_position: bool
simulate_android: bool
imagemap_cache: bool
predict_callbacks: list[Callable[[], None]]
expensive_predict_callbacks: list[Callable[[], Incomplete | None]]
predict_screens: bool
choice_screen_chosen: bool
narrator_menu: bool
variants: list[str | None]
imagemap_auto_function: Callable[[str, str], DisplayableLike] | None
keep_running_transform: bool
image_attributes: bool
new_character_image_argument: bool
say_attribute_transition: Incomplete | None
say_attribute_transition_layer: Incomplete | None
name: str
version: str
log_enable: bool
debug_text_overflow: bool
allow_underfull_grids: bool
save_physical_size: bool
new_substitutions: bool
old_substitutions: bool
renderer: str
translator: Unused
broken_line_spacing: bool
python_callbacks: list[Callable[[], None]]
save_dump: bool
gl_resize: bool
change_language_callbacks: list[Callable[[str | None], None]]
tl_directory: str
key_repeat: tuple[float, float]
voice_tag_callback: Callable[[Incomplete | None], None] | None
save_json_callbacks: list[Callable[[dict[str, Any]], None]]
longpress_duration: float
longpress_radius: int
longpress_vibrate: float
statement_callbacks: list[Callable[[str], None]]
autoreload_blacklist: list[str]
reload_modules: list[str]
say_layer: str
choice_layer: str
nvl_choice_layer: str
raw_tracebacks: bool
tts_function: Callable[[str], None] | None
tts_voice_channels: list[str]
screen_cache_size: int
adjust_view_size: Callable[[int, int], tuple[int, int]] | None
autosave_on_choice: bool
autosave_on_input: bool
emphasize_audio_channels: list[str]
emphasize_audio_volume: float
emphasize_audio_time: float
transition_screens: bool
predict_statements_callback: Callable[[renpy.ast.NodeName], list[renpy.ast.NodeName]] | None
hw_video: bool
dispatch_gesture: Callable[[str], None | Any] | None
gestures: dict[str, str]
gesture_component_size: float
gesture_stroke_size: float
log_to_stdout: bool

@type_check_only
class TextTagFunction(Protocol):
    def __call__(
        self, tag: str, argument: str, contents: list[renpy.text.text.Token], /
    ) -> list[renpy.text.text.Token]: ...

@type_check_only
class TextTagSelfClosingFunction(Protocol):
    def __call__(self, tag: str, argument: str, /) -> list[renpy.text.text.Token]: ...

custom_text_tags: dict[str, TextTagFunction]
self_closing_custom_text_tags: dict[str, TextTagSelfClosingFunction]
replace_text: Callable[[str], str] | None
missing_label_callback: Callable[[renpy.ast.NodeName], renpy.ast.NodeName | None] | None
preserve_zorder: bool
lint_ignore_replaces: list[str]
minimum_presplash_time: float
nearest_neighbor: bool
use_drawable_resolution: bool
drawable_resolution_text: bool
draw_virtual_text_box: bool
pad_bindings: dict[str, list[str]]
pygame_events: list[int]
map_pad_event: Callable[[str], list[str]] | None
after_replay_callback: Callable[[], None] | None
wrap_shown_transforms: bool
search_prefixes: list[str]
clear_lines: bool
special_namespaces: dict[str, Incomplete]
line_log: bool
dynamic_images: bool
save_on_mobile_background: bool
quit_on_mobile_background: bool
pass_joystick_events: bool
pass_controller_events: bool
overlay_screens: list[str]
always_shown_screens: list[str]
tag_layer: dict[str, str]
default_tag_layer: str
tag_transform: dict[str, Transform | list[Transform]]
tag_zorder: dict[str, int]
log_width: int
rollback_side_size: float
de_minimus_dpi_scale: float
windows_dpi_scale_head: float | Unused
enable_rollback_side: bool
replay_scope: dict[str, Any]
movie_mixer: str
auto_channels: dict[str, tuple[str, str, str]]
play_channel: str
speaking_attribute: str | None
list_compression_length: int
history_length: int | None
history_callbacks: list[Callable[[renpy.character.HistoryEntry], None]]
history_current_dialogue: bool
new_translate_order: bool
defer_styles: bool
translate_clean_stores: list[str]
translate_files: list[str]
translate_comments: list[str]
enable_language_autodetect: bool
locale_to_language_function: Callable[[str, str], str] | None
locale_to_language_map: dict[str, str]
old_say_args: bool
tts_voice: str | None
max_fit_size: int
enforce_window_max_size: bool
translate_launcher: bool
language_callbacks: collections.defaultdict[str | None, list[Callable[[], None]]]
init_system_styles: Callable[[], None] | None
build_styles_callbacks: list[Callable[[], None]]
auto_movie_channel: bool
ignore_duplicate_labels: bool
line_log_callbacks: Callable[[renpy.execution.LineLogEntry], None]
profile_screens: list[str]
allow_sysfonts: bool
tight_loop_default: bool
prefix_viewport_scrollbar_styles: bool
needs_redraw_callbacks: list[Callable[[], bool]]
hyperlink_inherit_size: bool
stdout_callbacks: list[Callable[[str], None]]
stderr_callbacks: list[Callable[[str], None]]
automatic_polar_motion: bool
lint_stats_callbacks: list[Callable[[], None]]
position_viewport_side: bool
character_id_prefixes: list[str]
nw_voice: bool
say_arguments_callback: Callable | None
atl_one_frame: bool
atl_function_always_blocks: bool
keep_show_layer_state: bool
fast_skipping_callbacks: list[Callable[[], None]]
audio_periodic_thread: bool
preload_fonts: list[str]
atl_multiple_events: bool
loadable_callback: Callable[[str], bool] | None
fast_redraw_frames: int
gl_clear_color: str
per_frame_screens: list[str]
performance_window: float
profile_time: float
profile_to_event: str
fast_unhandled_event: bool
fast_empty_window: bool
all_nodes_rollback: bool
manage_gc: bool
gc_thresholds: tuple[int, int, int]
idle_gc_count: int
gc_print_unreachable: bool
idle_frame: int
take_state_from_target: bool
scrollbar_child_size: bool
cache_surfaces: bool
optimize_texture_bounds: bool
conditionswitch_predict_all: bool
repeat_transform_events: list[str]
warp_limit: int
dissolve_force_alpha: bool
displayable_prefix: dict[str, Callable[[str], DisplayableLike]]
replay_movie_sprites: bool
context_callback: Callable[[], None] | None
reject_relative: bool
side_image_prefix_tag: str
say_attributes_use_side_image: bool
menu_showed_window: bool
menu_actions: bool
menu_include_disabled: bool
report_extraneous_attributes: bool
skip_sounds: bool
lint_screens_without_parameters: bool
menu_arguments_callback: Callable | None
auto_clear_screenshot: bool
allow_duplicate_labels: bool
font_transforms: dict[str, Incomplete]
ftfont_scale: dict[str, float]
ftfont_vertical_extent_scale: dict[str, float]
default_shader: str
preserve_volume_when_muted: bool

def say_attribute_transition_callback(*args) -> tuple[Incomplete, Incomplete]: ...

say_attribute_transition_callback_attrs: bool
notify: Callable[[str], None] | None
keyword_after_python: bool
load_failed_label: renpy.ast.NodeName | Callable[[], renpy.ast.NodeName] | None
equal_mono: bool
disable_input: bool
keep_side_render_order: bool
gl2: bool
depth_size: int
context_copy_remove_screens: list[str]
exception_handler: Callable[[renpy.error.TracebackException], bool] | None
return_not_found_label: renpy.ast.NodeName | None
autoreload_functions: list[tuple[str | re.Pattern[str], Callable[[str], None]]]
voice_mixers: list[str]
debug_text_alignment: bool
profile_init: float
live2d_interpolate: bool
tts_filter_tags: list[str]
merge_uniforms: dict[str, Callable[[Any, Any], Any]]
side_image_requires_attributes: bool
max_mipmap_level: int
touch_keyboard: bool
max_texture_size: tuple[int, int]
fbo_size = max_texture_size
lint_ignore_redefine: list[str]
quit_callbacks: list[Callable[[], None]]
steam_appid: int | None
controller_first_repeat: float
controller_repeat: float
controller_repeat_states: set[str]
side_image_only_not_showing: bool
expand_texture_bounds: int
modal_timeevent: bool
gl_set_attributes: Callable[[], None] | None
controller_blocklist: list[str]
mipmap: bool | Literal["auto"]
mipmap_dissolves: bool
mipmap_movies: bool
mipmap_text: bool
allow_screensaver: bool
context_fadein_music: int
context_fadeout_music: int
dismiss_blocking_transitions: bool
log_gl_extensions: bool
log_gl_shaders: bool
gl_blend_func: dict[str, tuple[int, int, int, int, int, int]]
pause_after_rollback: bool
perspective: tuple[float, float, float]
scene_clears_layer_at_list: bool
mouse_displayable: renpy.display.displayable.Displayable | Callable[[], renpy.display.displayable.Displayable] | None
gl_lod_bias: float
adjust_attributes: dict[str | None, Callable[[tuple[str, ...]], tuple[str, ...]]]
default_attribute_callbacks: dict[str | None, Callable[[tuple[str, ...]], tuple[str, ...]]]
who_what_sub_compat: int
compat_viewport_minimum: bool
webaudio: bool
webaudio_required_types: list[str]
audio_filename_callback: Callable[[str], str] | None
adjust_minimums: bool
atl_start_on_show: bool
input_caret_blink: float
single_movie_channel: str | None
raise_image_exceptions: bool | None
relative_transform_size: bool
tts_front_to_back: bool
tts_queue: bool
log_live2d_loading: bool
debug_prediction: bool
mouse_focus_clickthrough: bool
always_unfocus: bool
at_exit_callbacks: list[Callable[[], None]]
lint_character_statistics: bool
allow_unfull_vpgrids: bool
box_skip: bool
crop_relative_default: bool
nointeract_callbacks: list[Callable[[], None]]
layeredimage_offer_screen: bool
call_screen_roll_forward: bool

@type_check_only
class ChoiceEmptyWindowFunction(Protocol):
    def __call__(self, what: str, *, interact: bool) -> None: ...

choice_empty_window: ChoiceEmptyWindowFunction
open_file_encoding: bool | str
gl2_modify_window_flags: Callable[[int], int] | None
skip_during_text: bool
alternate_unelide_path: str | None
modal_blocks_pause: bool
modal_blocks_timer: bool
volume_db_range: int
font_name_map: dict[str, str]
relative_spacing: bool
autosave_callback: renpy.display.behavior.ActionType | None
viewport_drag_radius: int
scene_callbacks: list[Callable[[str], None]] | None
physical_width: int | None
physical_height: int | None
lenticular_bracket_ruby: bool
web_input: bool
key_aliases: dict[str, str]
save_token_keys: list[str]
viewport_inertia_amplitude: float
viewport_inertia_time_constant: float
after_default_callbacks: list[Callable[[], None]]
check_conflicting_properties: bool
extra_savedirs: list[str]
tts_substitutions: list[tuple[str | re.Pattern, str]]
web_video_base: str
scry_extend: bool
check_translate_none: bool
early_developer: bool
autosave_prefix_callback: Callable[[], str] | None
at_transform_compare_full_context: bool
display_start_callbacks: list[Callable[[], None]]
sound_buffer_size: int | None
quadratic_volumes: bool
linear_fades: bool
ex_rollback_classes: list[type]
simple_box_reverse: bool
box_reverse_align: bool
atl_pos_only: bool
atl_pos_only_as_pos_or_kw: bool
font_hinting: dict[str | None, Literal["auto", "auto-light", "bytecode", "none"]]
mixed_position: bool
interpolate_exprs: bool | Literal["fallback"]
generating_documentation: bool
save: bool
save_persistent: bool
drag_group_add_top: bool
defer_tl_scripts: bool
transitions_use_child_placement: bool
containers_pass_transform_events: set[str]
say_replace_event: bool
screens_never_cancel_hide: bool
layer_transforms: dict[str | None, renpy.display.scenelists.AtList]
fill_shrinks_frame: bool
log_events: bool
python_exit_callbacks: list[Callable[[], None]]
raise_image_load_exceptions: bool | None
textshaders: dict[str, TextShader]
textshader_callbacks: dict[str, Callable[[], str]]
default_textshader: str | None
shader_part_filter: Callable[[tuple[str, ...]], tuple[str, ...]] | None
munge_in_strings: bool
character_callback_compat: bool | None
translate_ignore_who: list[str]
interface_layer: str
limit_transform_crop: bool | Literal["only_float"]
dissolve_shrinks: bool
reverse_arabic_presentation_forms: bool
future_annotations: bool
no_replay_seen: bool
old_show_expression: bool
translate_additional_strings_callbacks: list[Callable[[], list[tuple[str, int, str]]]]
keep_screenshot_entering_menu: bool
hash_seen: bool
persistent_callback: Callable[[renpy.persistent.Persistent], None] | None
lint_show_names: bool
cds_label_callbacks: bool
error_suggestion_handlers: dict[type[BaseException], Callable[[Any], str | None]]
auto_voice_predict_callback: Callable[[str], None] | None
clear_history_on_language_change: bool
automatic_oversampling: int | None
web_unload_music: float | None
mesh_pad_compat: bool
emscripten_preload_timeout: float | None
adjust_audio_amplitude: float
zoom_zaxis: bool
context_callbacks: list[Callable[[], None]]
live2d_max_memory: int
gl_vsync: bool
tracesave_screenshot: bool
maximum_embiggens: bool
extend_like_characters: set[str]
tlid_only_considers_say: bool

def init() -> None: ...
def post_init() -> None: ...
