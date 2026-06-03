# SPDX-FileCopyrightText: 2017-2023 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

# --env-system-scripts allows to run without the install target.

# Use '--write-blend=/tmp/test.blend' to view output

set(TEST_SRC_DIR ${CMAKE_SOURCE_DIR}/tests/files)
set(TEST_OUT_DIR ${CMAKE_BINARY_DIR}/tests)

# ugh, any better way to do this on testing only?
execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${TEST_OUT_DIR})

# if(NOT IS_DIRECTORY ${TEST_SRC_DIR})
#   message(FATAL_ERROR "CMake test directory not found!")
# endif()

# For testing with VALGRIND prefix: `valgrind --track-origins=yes --error-limit=no`
set(TEST_BLENDER_EXE
  $<TARGET_FILE:blender>
  --background
  --factory-startup
  --debug-memory
  --debug-exit-on-error
  --env-system-scripts ${CMAKE_SOURCE_DIR}/scripts
)

# ------------------------------------------------------------------------------

function(view_layer_test test_name)
  # Adds ${CMAKE_CURRENT_LIST_DIR} to sys.path so that the tests can import
  # things from view_layer_common.py
  add_test(
    NAME view_layer_${test_name}
    COMMAND ${TEST_BLENDER_EXE}
    --python-expr "import sys; sys.path.append('${CMAKE_CURRENT_LIST_DIR}')"
    --python-exit-code 1
    --python ${CMAKE_CURRENT_LIST_DIR}/test_${test_name}.py --
    --testdir="${TEST_SRC_DIR}/layers"
  )
endfunction()

set(TESTS
  active_collection
  background_set
  collection_new_sync
  collection_rename_a
  collection_rename_b
  # evaluation_render_settings_a
  # evaluation_render_settings_b
  # evaluation_render_settings_c
  # evaluation_render_settings_d
  # evaluation_render_settings_e
  # evaluation_render_settings_f
  # evaluation_render_settings_g
  # evaluation_render_settings_h
  # evaluation_render_settings_i
  evaluation_visibility_a
  evaluation_visibility_b
  evaluation_visibility_c
  evaluation_visibility_d
  evaluation_visibility_e
  evaluation_visibility_f
  evaluation_visibility_g
  evaluation_visibility_h
  evaluation_visibility_i
  evaluation_visibility_j
  evaluation_selectability_a
  evaluation_selectability_b
  evaluation_selectability_c
  evaluation_selectability_d
  evaluation_selectability_e
  evaluation_selectability_f
  group_a
  group_b
  group_c
  group_d
  group_e
  object_add_cylinder
  object_add_empty
  object_add_torus
  object_add_no_collection_cylinder
  object_add_no_collection_empty
  object_add_no_collection_torus
  object_copy
  object_delete_a
  object_delete_b
  object_link_a
  object_link_b
  object_link_c
  operator_context
  make_single_user
  move_above_below_scene_collection_a
  move_above_below_scene_collection_b
  move_above_below_scene_collection_c
  move_above_below_scene_collection_d
  move_above_below_scene_collection_e
  move_above_below_scene_collection_f
  move_above_below_scene_collection_g
  move_above_below_scene_collection_h
  move_above_below_scene_collection_i
  move_above_below_scene_collection_sync_a
  move_above_below_scene_collection_sync_b
  move_above_below_scene_collection_sync_c
  move_above_below_scene_collection_sync_d
  move_above_below_scene_collection_sync_e
  move_above_below_scene_collection_sync_f
  move_above_below_scene_collection_sync_g
  move_above_below_scene_collection_sync_h
  move_above_below_scene_collection_sync_i
  move_into_scene_collection_a
  move_into_scene_collection_b
  move_into_scene_collection_c
  move_into_scene_collection_d
  move_into_scene_collection_e
  move_into_scene_collection_f
  move_into_scene_collection_g
  move_into_scene_collection_h
  move_into_scene_collection_i
  move_into_scene_collection_j
  move_into_scene_collection_k
  move_into_scene_collection_l
  move_into_scene_collection_sync_a
  move_into_scene_collection_sync_b
  move_into_scene_collection_sync_c
  move_into_scene_collection_sync_d
  move_into_scene_collection_sync_e
  move_into_scene_collection_sync_f
  move_into_scene_collection_sync_g
  move_into_scene_collection_sync_h
  move_into_scene_collection_sync_i
  move_into_scene_collection_sync_j
  move_into_scene_collection_sync_k
  move_into_scene_collection_sync_l
  move_above_below_layer_collection_a
  move_above_below_layer_collection_b
  move_above_below_layer_collection_c
  move_above_below_layer_collection_d
  move_above_below_layer_collection_e
  move_above_below_layer_collection_f
  move_above_below_layer_collection_g
  move_above_below_layer_collection_h
  move_above_below_layer_collection_i
  move_above_below_layer_collection_j
  move_above_below_layer_collection_k
  move_above_below_layer_collection_l
  move_into_layer_collection_a
  move_into_layer_collection_b
  move_into_layer_collection_c
  move_into_layer_collection_d
  move_into_layer_collection_e
  move_into_layer_collection_f
  move_into_layer_collection_g
  move_into_layer_collection_h
  move_into_layer_collection_i
  move_into_layer_collection_j
  layer_linking
  layer_syncing
  scene_collection_delete
  scene_copy_a
  scene_copy_b
  scene_copy_c
  scene_copy_d
  scene_copy_e
  scene_copy_f
  scene_delete
  scene_objects
  scene_write_read
  view_layer_rename
)

foreach(test_name ${TESTS})
  view_layer_test(${test_name})
endforeach()