from _typeshed import Incomplete

from . import actionexports as actionexports
from . import commonexports as commonexports
from . import contextexports as contextexports
from . import debugexports as debugexports
from . import displayexports as displayexports
from . import fetchexports as fetchexports
from . import inputexports as inputexports
from . import loaderexports as loaderexports
from . import mediaexports as mediaexports
from . import menuexports as menuexports
from . import persistentexports as persistentexports
from . import platformexports as platformexports
from . import predictexports as predictexports
from . import restartexports as restartexports
from . import rollbackexports as rollbackexports
from . import sayexports as sayexports
from . import scriptexports as scriptexports
from . import statementexports as statementexports

from renpy.ast import eval_who as eval_who
from renpy.atl import atl_warper as atl_warper
from renpy.bootstrap import get_alternate_base as get_alternate_base
from renpy.character import (
    display_say as display_say,
    predict_show_display_say as predict_show_display_say,
    show_display_say as show_display_say,
)

from renpy.curry import curry as curry, partial as partial
from renpy.display.behavior import (
    Keymap as Keymap,
    clear_keymap_cache as clear_keymap_cache,
    is_selected as is_selected,
    is_sensitive as is_sensitive,
    map_event as map_event,
    queue_event as queue_event,
    run as run,
    run_periodic as run_periodic,
    run_unhovered as run_unhovered,
)
from renpy.display.focus import (
    capture_focus as capture_focus,
    clear_capture_focus as clear_capture_focus,
    focus_coordinates as focus_coordinates,
    get_focus_rect as get_focus_rect,
)
from renpy.display.im import load_image as load_image, load_rgba as load_rgba, load_surface as load_surface
from renpy.display.image import (
    check_image_attributes as check_image_attributes,
    get_available_image_attributes as get_available_image_attributes,
    get_available_image_tags as get_available_image_tags,
    get_ordered_image_attributes as get_ordered_image_attributes,
    get_registered_image as get_registered_image,
    image_exists as image_exists,
    list_images as list_images,
)
from renpy.display.minigame import Minigame as Minigame
from renpy.display.scenelists import layer_has_transforms as layer_has_transforms
from renpy.display.screen import (
    current_screen as current_screen,
    define_screen as define_screen,
    get_displayable as get_displayable,
    get_displayable_properties as get_displayable_properties,
    get_screen as get_screen,
    get_screen_docstring as get_screen_docstring,
    get_screen_variable as get_screen_variable,
    get_widget as get_widget,
    get_widget_properties as get_widget_properties,
    has_screen as has_screen,
    hide_screen as hide_screen,
    set_screen_variable as set_screen_variable,
    show_screen as show_screen,
    use_screen as use_screen,
)
from renpy.display.tts import speak_extra_alt as speak_extra_alt, stop_tts as stop_tts
from renpy.display.video import (
    movie_start_displayable as movie_start_displayable,
    movie_start_fullscreen as movie_start_fullscreen,
    movie_stop as movie_stop,
)
from renpy.easy import displayable as displayable, predict as predict, split_properties as split_properties
from renpy.editor import launch_editor as launch_editor
from renpy.execution import not_infinite_loop as not_infinite_loop, reset_all_contexts as reset_all_contexts
from renpy.exports.actionexports import confirm as confirm, display_notify as display_notify, notify as notify
from renpy.exports.commonexports import renpy_pure as renpy_pure
from renpy.exports.contextexports import (
    add_to_all_stores as add_to_all_stores,
    call_in_new_context as call_in_new_context,
    call_replay as call_replay,
    call_stack_depth as call_stack_depth,
    clear_game_runtime as clear_game_runtime,
    clear_line_log as clear_line_log,
    context as context,
    context_dynamic as context_dynamic,
    context_nesting_level as context_nesting_level,
    current_interact_type as current_interact_type,
    curried_call_in_new_context as curried_call_in_new_context,
    curried_invoke_in_new_context as curried_invoke_in_new_context,
    dynamic as dynamic,
    end_replay as end_replay,
    game_menu as game_menu,
    get_game_runtime as get_game_runtime,
    get_line_log as get_line_log,
    get_mode as get_mode,
    get_return_stack as get_return_stack,
    get_skipping as get_skipping,
    get_statement_name as get_statement_name,
    invoke_in_new_context as invoke_in_new_context,
    is_in_test as is_in_test,
    is_init_phase as is_init_phase,
    is_skipping as is_skipping,
    jump_out_of_context as jump_out_of_context,
    last_interact_type as last_interact_type,
    mode as mode,
    pop_call as pop_call,
    pop_return as pop_return,
    scry as scry,
    set_return_stack as set_return_stack,
    stop_skipping as stop_skipping,
)
from renpy.exports.debugexports import (
    error as error,
    filename_line_override as filename_line_override,
    get_filename_line as get_filename_line,
    log as log,
    pop_error_handler as pop_error_handler,
    push_error_handler as push_error_handler,
    warp_to_line as warp_to_line,
    write_log as write_log,
)
from renpy.exports.displayexports import (
    Container as Container,
    Displayable as Displayable,
    IgnoreEvent as IgnoreEvent,
    Render as Render,
    add_layer as add_layer,
    can_fullscreen as can_fullscreen,
    can_show as can_show,
    cancel_gesture as cancel_gesture,
    change_zorder as change_zorder,
    clear_attributes as clear_attributes,
    clear_retain as clear_retain,
    copy_images as copy_images,
    count_displayables_in_layer as count_displayables_in_layer,
    default_layer as default_layer,
    display_reset as display_reset,
    easy_displayable as easy_displayable,
    end_interaction as end_interaction,
    flush_cache_file as flush_cache_file,
    force_full_redraw as force_full_redraw,
    free_memory as free_memory,
    get_adjustment as get_adjustment,
    get_at_list as get_at_list,
    get_attributes as get_attributes,
    get_hidden_tags as get_hidden_tags,
    get_image_bounds as get_image_bounds,
    get_image_load_log as get_image_load_log,
    get_mouse_name as get_mouse_name,
    get_mouse_names as get_mouse_names,
    get_mouse_pos as get_mouse_pos,
    get_ongoing_transition as get_ongoing_transition,
    get_physical_size as get_physical_size,
    get_placement as get_placement,
    get_refresh_rate as get_refresh_rate,
    get_renderer_info as get_renderer_info,
    get_showing_tags as get_showing_tags,
    get_texture_size as get_texture_size,
    get_transition as get_transition,
    get_zorder_list as get_zorder_list,
    hide as hide,
    iconify as iconify,
    image as image,
    image_size as image_size,
    is_mouse_visible as is_mouse_visible,
    is_pixel_opaque as is_pixel_opaque,
    is_start_interact as is_start_interact,
    layer_at_list as layer_at_list,
    maximum_framerate as maximum_framerate,
    placement as placement,
    predict_show as predict_show,
    quit_event as quit_event,
    redraw as redraw,
    render as render,
    render_to_file as render_to_file,
    render_to_surface as render_to_surface,
    reset_physical_size as reset_physical_size,
    restart_interaction as restart_interaction,
    scene as scene,
    scene_lists as scene_lists,
    screenshot as screenshot,
    screenshot_to_bytes as screenshot_to_bytes,
    set_focus as set_focus,
    set_mouse_pos as set_mouse_pos,
    set_physical_size as set_physical_size,
    set_tag_attributes as set_tag_attributes,
    show as show,
    show_layer_at as show_layer_at,
    showing as showing,
    shown_window as shown_window,
    take_screenshot as take_screenshot,
    timeout as timeout,
    toggle_fullscreen as toggle_fullscreen,
    transition as transition,
)
from renpy.exports.fetchexports import (
    FetchError as FetchError,
    fetch as fetch,
    fetch_emscripten as fetch_emscripten,
    fetch_pause as fetch_pause,
    fetch_requests as fetch_requests,
    proxies as proxies,
)
from renpy.exports.inputexports import (
    get_editable_input_value as get_editable_input_value,
    input as input,
    set_editable_input_value as set_editable_input_value,
    web_input as web_input,
)
from renpy.exports.loaderexports import (
    exists as exists,
    file as file,
    fsdecode as fsdecode,
    fsencode as fsencode,
    list_files as list_files,
    loadable as loadable,
    munge as munge,
    notl_file as notl_file,
    open_file as open_file,
)
from renpy.exports.mediaexports import (
    movie_cutscene as movie_cutscene,
    music_start as music_start,
    music_stop as music_stop,
    play as play,
    toggle_music as toggle_music,
)
from renpy.exports.menuexports import (
    MenuEntry as MenuEntry,
    choice_for_skipping as choice_for_skipping,
    display_menu as display_menu,
    get_menu_args as get_menu_args,
    menu as menu,
    predict_menu as predict_menu,
)
from renpy.exports.persistentexports import (
    is_seen as is_seen,
    is_seen_allowed as is_seen_allowed,
    mark_audio_seen as mark_audio_seen,
    mark_audio_unseen as mark_audio_unseen,
    mark_image_seen as mark_image_seen,
    mark_image_unseen as mark_image_unseen,
    mark_label_seen as mark_label_seen,
    mark_label_unseen as mark_label_unseen,
    mark_translation_seen as mark_translation_seen,
    mark_translation_unseen as mark_translation_unseen,
    save_persistent as save_persistent,
    seen_audio as seen_audio,
    seen_image as seen_image,
    seen_label as seen_label,
    seen_translation as seen_translation,
)
from renpy.exports.platformexports import (
    check_permission as check_permission,
    get_on_battery as get_on_battery,
    get_sdl_dll as get_sdl_dll,
    get_sdl_window_pointer as get_sdl_window_pointer,
    invoke_in_main_thread as invoke_in_main_thread,
    invoke_in_thread as invoke_in_thread,
    open_url as open_url,
    request_permission as request_permission,
    variant as variant,
    vibrate as vibrate,
)
from renpy.exports.predictexports import (
    cache_pin as cache_pin,
    cache_unpin as cache_unpin,
    expand_predict as expand_predict,
    predicting as predicting,
    start_predict as start_predict,
    start_predict_screen as start_predict_screen,
    stop_predict as stop_predict,
    stop_predict_screen as stop_predict_screen,
)
from renpy.exports.restartexports import (
    full_restart as full_restart,
    get_autoreload as get_autoreload,
    quit as quit,
    reload_script as reload_script,
    set_autoreload as set_autoreload,
    utter_restart as utter_restart,
)
from renpy.exports.rollbackexports import (
    block_rollback as block_rollback,
    can_rollback as can_rollback,
    checkpoint as checkpoint,
    fix_rollback as fix_rollback,
    get_identifier_checkpoints as get_identifier_checkpoints,
    get_roll_forward as get_roll_forward,
    in_fixed_rollback as in_fixed_rollback,
    in_rollback as in_rollback,
    retain_after_load as retain_after_load,
    roll_forward_core as roll_forward_core,
    roll_forward_info as roll_forward_info,
    rollback as rollback,
    suspend_rollback as suspend_rollback,
)
from renpy.exports.sayexports import (
    LastSay as LastSay,
    TagQuotingDict as TagQuotingDict,
    count_dialogue_blocks as count_dialogue_blocks,
    count_newly_seen_dialogue_blocks as count_newly_seen_dialogue_blocks,
    count_seen_dialogue_blocks as count_seen_dialogue_blocks,
    curried_do_reshow_say as curried_do_reshow_say,
    do_reshow_say as do_reshow_say,
    get_reshow_say as get_reshow_say,
    get_say_attributes as get_say_attributes,
    get_say_image_tag as get_say_image_tag,
    get_side_image as get_side_image,
    last_say as last_say,
    predict_say as predict_say,
    reshow_say as reshow_say,
    say as say,
    scry_say as scry_say,
    substitute as substitute,
    tag_quoting_dict as tag_quoting_dict,
)
from renpy.exports.scriptexports import (
    get_all_labels as get_all_labels,
    has_label as has_label,
    include_module as include_module,
    load_language as load_language,
    load_module as load_module,
    load_string as load_string,
    munged_filename as munged_filename,
)
from renpy.exports.statementexports import (
    call as call,
    call_screen as call_screen,
    execute_default_statement as execute_default_statement,
    imagemap as imagemap,
    jump as jump,
    pause as pause,
    return_statement as return_statement,
    with_statement as with_statement,
)
from renpy.gl2.gl2shadercache import register_shader as register_shader
from renpy.gl2.live2d import has_live2d as has_live2d
from renpy.importer import add_python_directory as add_python_directory
from renpy.lexer import lex_string as lex_string, unelide_filename as unelide_filename
from renpy.lint import try_compile as try_compile, try_eval as try_eval
from renpy.loadsave import (
    can_load as can_load,
    copy_save as copy_save,
    force_autosave as force_autosave,
    get_save_data as get_save_data,
    list_saved_games as list_saved_games,
    list_slots as list_slots,
    load as load,
    newest_slot as newest_slot,
    rename_save as rename_save,
    save as save,
    scan_saved_game as scan_saved_game,
    slot_json as slot_json,
    slot_mtime as slot_mtime,
    slot_screenshot as slot_screenshot,
    unlink_save as unlink_save,
)
from renpy.memory import (
    diff_memory as diff_memory,
    profile_memory as profile_memory,
    profile_rollback as profile_rollback,
)
from renpy.parser import get_parse_errors as get_parse_errors
from renpy.persistent import register_persistent as register_persistent
from renpy.pyanalysis import const as const, not_const as not_const, pure as pure
from renpy.python import mark_changed as mark_changed
from renpy.savetoken import get_save_token_keys as get_save_token_keys
from renpy.sl2.slparser import register_sl_displayable as register_sl_displayable
from renpy.text.extras import (
    ParameterizedText as ParameterizedText,
    check_text_tags as check_text_tags,
    filter_text_tags as filter_text_tags,
)
from renpy.text.font import (
    register_bmfont as register_bmfont,
    register_mudgefont as register_mudgefont,
    register_sfont as register_sfont,
    variable_font_info as variable_font_info,
)
from renpy.text.shader import TextShader as TextShader, register_textshader as register_textshader
from renpy.text.text import BASELINE as BASELINE, language_tailor as language_tailor
from renpy.translation import (
    change_language as change_language,
    get_translation_identifier as get_translation_identifier,
    get_translation_info as get_translation_info,
    known_languages as known_languages,
    translate_string as translate_string,
)
from renpy.ui import Choice as Choice

menu_args: Incomplete
menu_kwargs: Incomplete
bits: int

@renpy_pure
def version(tuple: bool = False): ...

version_string: Incomplete
version_only: Incomplete
version_name: Incomplete
version_tuple: Incomplete
license: str
platform: Incomplete
