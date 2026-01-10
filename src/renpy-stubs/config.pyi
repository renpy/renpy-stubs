import renpy
from _typeshed import Incomplete as Incomplete
from renpy.error import TracebackException as TracebackException
from renpy.text.shader import TextShader as TextShader
from renpy.types import DisplayableLike
from typing import Any, Callable, Literal, IO, Protocol, TypedDict, Unpack, NotRequired
import re

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
overlay_functions: Incomplete
underlay: Incomplete
profile: bool
savedir: Incomplete
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
archives: Incomplete
searchpath: Incomplete
force_archives: bool
mouse: Incomplete
sound_sample_rate: int
fadeout_audio: float
fade_music: Incomplete
sticky_positions: bool
layers: list[str]
transient_layers: Incomplete
overlay_layers: Incomplete
context_clear_layers: Incomplete
top_layers: Incomplete
bottom_layers: Incomplete
sticky_layers: Incomplete
detached_layers: Incomplete
overlay_during_with: bool
enable_fast_dissolve: bool
focus_crossrange_penalty: int
load_before_transition: bool
keymap: dict[str, list[str]]
default_keymap: dict[str, list[str]]
joystick: bool
interact_callbacks: Incomplete
start_interact_callbacks: Incomplete
say_sustain_callbacks: Incomplete
say_allow_dismiss: Incomplete
text_tokenizer: Incomplete
afm_characters: int
afm_bonus: int
afm_callback: Callable[[], bool] | None
auto_choice_delay: Incomplete
font_replacement_map: Incomplete
with_callback: Callable[[Incomplete, Incomplete | None], Incomplete] | None
framerate: int
frames: int
editor: Incomplete
editor_transient: Incomplete
editor_file_separator: Incomplete
developer: bool
original_developer: Literal["auto"] | bool
default_developer: bool
log: Incomplete
clear_log: bool
lint_hooks: Incomplete
hyperlink_styler: Incomplete
hyperlink_callback: Incomplete
hyperlink_focus: Incomplete
recolor_sfonts: bool
text_layout: Incomplete
periodic_callback: Incomplete
periodic_callbacks: Incomplete
check_properties: bool
implicit_with_none: bool
layer_clipping: Incomplete
disable_fullscreen_opt: bool
reject_midi: bool
character_callback: Incomplete

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

class CharacterCallback(Protocol):
    def __call__(
        self,
        event: Literal["begin", "show", "show_done", "slow_done", "interact_done", "end"],
        **kwargs: Unpack[CharacterCallbackParameters],
    ) -> None: ...

all_character_callbacks: list[CharacterCallback]
has_autosave: bool
autosave_slots: int
autosave_frequency: Incomplete
scene: Callable[[str | None], None] | None
show: Incomplete
hide: Incomplete
use_cpickle: bool
inspector: Incomplete
reject_backslash: bool
mouse_hide_time: int
missing_image_callback: Callable[[str], renpy.display.im.ImageBase | None] | None
say_menu_text_filter: Callable[[str], str] | None
label_overrides: dict[renpy.ast.NodeName, renpy.ast.NodeName]
auto_save_extra_info: Incomplete
save_directory: str | None
missing_scene: Incomplete
missing_show: Incomplete
missing_hide: Incomplete
label_callback: Incomplete
label_callbacks: Incomplete
empty_window: Incomplete
window_overlay_functions: Incomplete
rtl: bool
file_open_callback: Callable[[str], IO | None] | None
thumbnail_width: int
thumbnail_height: int
end_game_transition: Incomplete
default_transform: Incomplete
transform_uses_child_position: bool
quit_action: Incomplete
screenshot_crop: Incomplete
gamedir: str
basedir: str
renpy_base: str
commondir: str | None
logdir: str | None
gl_enable: bool
mode_callbacks: Incomplete
movetransition_respects_offsets: bool
imagereference_respects_position: bool
simulate_android: bool
imagemap_cache: bool
predict_callbacks: Incomplete
expensive_predict_callbacks: Incomplete
predict_screens: bool
choice_screen_chosen: bool
narrator_menu: bool
variants: list
imagemap_auto_function: Callable[[str, str], DisplayableLike] | None
keep_running_transform: bool
image_attributes: bool
new_character_image_argument: bool
say_attribute_transition: Incomplete
say_attribute_transition_layer: Incomplete
name: str
version: str
log_enable: bool
debug_text_overflow: bool
allow_underfull_grids: bool
save_physical_size: bool
new_substitutions: bool
old_substitutions: bool
renderer: str
translator: Incomplete
broken_line_spacing: bool
python_callbacks: Incomplete
save_dump: bool
gl_resize: bool
change_language_callbacks: Incomplete
tl_directory: str
key_repeat: Incomplete
voice_tag_callback: Incomplete
save_json_callbacks: Incomplete
longpress_duration: float
longpress_radius: int
longpress_vibrate: float
statement_callbacks: Incomplete
autoreload_blacklist: Incomplete
reload_modules: Incomplete
say_layer: str
choice_layer: str
nvl_choice_layer: str
raw_tracebacks: Incomplete
tts_function: Callable[[str], None] | None
tts_voice_channels: Incomplete
screen_cache_size: int
adjust_view_size: Incomplete
autosave_on_choice: bool
autosave_on_input: bool
emphasize_audio_channels: Incomplete
emphasize_audio_volume: float
emphasize_audio_time: float
transition_screens: bool
predict_statements_callback: Incomplete
hw_video: bool
dispatch_gesture: Callable[[str], None | Any] | None
gestures: dict[str, str]
gesture_component_size: float
gesture_stroke_size: float
log_to_stdout: Incomplete
custom_text_tags: Incomplete
self_closing_custom_text_tags: Incomplete
replace_text: Incomplete
missing_label_callback: Callable[[renpy.ast.NodeName], renpy.ast.NodeName | None] | None
preserve_zorder: bool
lint_ignore_replaces: Incomplete
minimum_presplash_time: float
nearest_neighbor: bool
use_drawable_resolution: bool
drawable_resolution_text: bool
draw_virtual_text_box: bool
pad_bindings: dict[str, list[str]]
pygame_events: Incomplete
map_pad_event: Callable[[str], list[str]] | None
after_replay_callback: Incomplete
wrap_shown_transforms: bool
search_prefixes: Incomplete
clear_lines: bool
special_namespaces: Incomplete
line_log: bool
dynamic_images: bool
save_on_mobile_background: bool
quit_on_mobile_background: bool
pass_joystick_events: bool
pass_controller_events: bool
overlay_screens: Incomplete
always_shown_screens: Incomplete
tag_layer: Incomplete
default_tag_layer: str
tag_transform: Incomplete
tag_zorder: Incomplete
log_width: int
rollback_side_size: float
de_minimus_dpi_scale: float
windows_dpi_scale_head: float
enable_rollback_side: bool
replay_scope: Incomplete
movie_mixer: str
auto_channels: Incomplete
play_channel: str
speaking_attribute: Incomplete
list_compression_length: int
history_length: Incomplete
history_callbacks: Incomplete
history_current_dialogue: bool
new_translate_order: bool
defer_styles: bool
translate_clean_stores: Incomplete
translate_files: Incomplete
translate_comments: Incomplete
enable_language_autodetect: bool
locale_to_language_function: Incomplete
locale_to_language_map: dict[str, str]
old_say_args: bool
tts_voice: str | None
max_fit_size: int
enforce_window_max_size: bool
translate_launcher: bool
language_callbacks: Incomplete
init_system_styles: Incomplete
build_styles_callbacks: Incomplete
auto_movie_channel: bool
ignore_duplicate_labels: bool
line_log_callbacks: Callable[[renpy.execution.LineLogEntry], None]
profile_screens: Incomplete
allow_sysfonts: bool
tight_loop_default: bool
prefix_viewport_scrollbar_styles: bool
needs_redraw_callbacks: Incomplete
hyperlink_inherit_size: bool
stdout_callbacks: list[Callable[[str], None]]
stderr_callbacks: list[Callable[[str], None]]
automatic_polar_motion: bool
lint_stats_callbacks: Incomplete
position_viewport_side: bool
character_id_prefixes: Incomplete
nw_voice: bool
say_arguments_callback: Callable | None
atl_one_frame: bool
atl_function_always_blocks: bool
keep_show_layer_state: bool
fast_skipping_callbacks: Incomplete
audio_periodic_thread: bool
preload_fonts: Incomplete
atl_multiple_events: bool
loadable_callback: Incomplete
fast_redraw_frames: int
gl_clear_color: str
per_frame_screens: Incomplete
performance_window: float
profile_time: Incomplete
profile_to_event: str
fast_unhandled_event: bool
fast_empty_window: bool
all_nodes_rollback: bool
manage_gc: bool
gc_thresholds: Incomplete
idle_gc_count: int
gc_print_unreachable: Incomplete
idle_frame: int
take_state_from_target: bool
scrollbar_child_size: bool
cache_surfaces: bool
optimize_texture_bounds: bool
conditionswitch_predict_all: bool
repeat_transform_events: Incomplete
warp_limit: int
dissolve_force_alpha: bool
displayable_prefix: Incomplete
replay_movie_sprites: bool
context_callback: Incomplete
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
font_transforms: Incomplete
ftfont_scale: Incomplete
ftfont_vertical_extent_scale: Incomplete
default_shader: str
preserve_volume_when_muted: bool

def say_attribute_transition_callback(*args) -> Incomplete: ...

say_attribute_transition_callback_attrs: bool
notify: Callable[[str], None] | None
keyword_after_python: bool
load_failed_label: Incomplete
equal_mono: bool
disable_input: bool
keep_side_render_order: bool
gl2: bool
depth_size: int
context_copy_remove_screens: Incomplete
exception_handler: Callable[[renpy.error.TracebackException], bool] | None
return_not_found_label: Incomplete
autoreload_functions: Incomplete
voice_mixers: Incomplete
debug_text_alignment: bool
profile_init: float
live2d_interpolate: bool
tts_filter_tags: Incomplete
merge_uniforms: Incomplete
side_image_requires_attributes: bool
max_mipmap_level: int
touch_keyboard: Incomplete
max_texture_size: Incomplete
fbo_size = max_texture_size
lint_ignore_redefine: Incomplete
quit_callbacks: Incomplete
steam_appid: Incomplete
controller_first_repeat: float
controller_repeat: float
controller_repeat_states: set[str]
side_image_only_not_showing: bool
expand_texture_bounds: int
modal_timeevent: bool
gl_set_attributes: Incomplete
controller_blocklist: list[str]
mipmap: bool
mipmap_dissolves: bool
mipmap_movies: bool
mipmap_text: bool
allow_screensaver: bool
context_fadein_music: int
context_fadeout_music: int
dismiss_blocking_transitions: bool
log_gl_extensions: bool
log_gl_shaders: bool
gl_blend_func: Incomplete
pause_after_rollback: bool
perspective: Incomplete
scene_clears_layer_at_list: bool
mouse_displayable: Incomplete
gl_lod_bias: float
adjust_attributes: Incomplete
default_attribute_callbacks: Incomplete
who_what_sub_compat: int
compat_viewport_minimum: bool
webaudio: bool
webaudio_required_types: Incomplete
audio_filename_callback: Incomplete
adjust_minimums: bool
atl_start_on_show: bool
input_caret_blink: float
single_movie_channel: Incomplete
raise_image_exceptions: Incomplete
relative_transform_size: bool
tts_front_to_back: bool
tts_queue: bool
log_live2d_loading: bool
debug_prediction: bool
mouse_focus_clickthrough: bool
always_unfocus: bool
at_exit_callbacks: Incomplete
lint_character_statistics: bool
allow_unfull_vpgrids: bool
box_skip: bool
crop_relative_default: bool
nointeract_callbacks: Incomplete
layeredimage_offer_screen: bool
call_screen_roll_forward: bool
choice_empty_window: Incomplete
open_file_encoding: Incomplete
gl2_modify_window_flags: Incomplete
skip_during_text: bool
alternate_unelide_path: Incomplete
modal_blocks_pause: bool
modal_blocks_timer: bool
volume_db_range: int
font_name_map: Incomplete
relative_spacing: bool
autosave_callback: Incomplete
viewport_drag_radius: int
scene_callbacks: Incomplete
physical_width: Incomplete
physical_height: Incomplete
lenticular_bracket_ruby: bool
web_input: bool
key_aliases: dict[str, str]
save_token_keys: Incomplete
viewport_inertia_amplitude: float
viewport_inertia_time_constant: float
after_default_callbacks: Incomplete
check_conflicting_properties: bool
extra_savedirs: Incomplete
tts_substitutions: list[tuple[str | re.Pattern, str]]
web_video_base: str
scry_extend: bool
check_translate_none: bool
early_developer: bool
autosave_prefix_callback: Incomplete
at_transform_compare_full_context: bool
display_start_callbacks: Incomplete
sound_buffer_size: Incomplete
quadratic_volumes: bool
linear_fades: bool
ex_rollback_classes: Incomplete
simple_box_reverse: bool
box_reverse_align: bool
atl_pos_only: bool
atl_pos_only_as_pos_or_kw: bool
font_hinting: Incomplete
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
layer_transforms: Incomplete
fill_shrinks_frame: bool
log_events: Incomplete
python_exit_callbacks: Incomplete
raise_image_load_exceptions: bool | None
textshaders: dict[str, TextShader]
textshader_callbacks: dict[str, Callable[[], str]]
default_textshader: str | None
shader_part_filter: Callable[[tuple[str]], tuple[str]] | None
munge_in_strings: bool
character_callback_compat: Incomplete
translate_ignore_who: Incomplete
interface_layer: str
limit_transform_crop: bool | Literal["only_float"]
dissolve_shrinks: bool
reverse_arabic_presentation_forms: bool
future_annotations: bool
no_replay_seen: bool
old_show_expression: bool
translate_additional_strings_callbacks: Incomplete
keep_screenshot_entering_menu: bool
hash_seen: bool
persistent_callback: Incomplete
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
