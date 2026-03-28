# SPDX-FileCopyrightText: 2017-2022 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

# ############################################################
# Importing - Same For All Render Layer Tests
# ############################################################

import unittest

from view_layer_common import (
    MoveSceneCollectionSyncTesting,
    setup_extra_arguments,
)


# ############################################################
# Testing
# ############################################################

class UnitTesting(MoveSceneCollectionSyncTesting):
    def get_reference_scene_tree_map(self):
        # original tree, no changes
        return self.get_initial_scene_tree_map()

    def _assert_no_move_from_master(self, tree, method_name):
        """
        Helper: ensure master_collection cannot move a child relative to it.
        """
        import bpy
        master_collection = bpy.context.scene.master_collection
        move = getattr(master_collection, method_name)
        for collection in tree.values():
            self.assertFalse(move(collection))

    def _assert_no_move_to_master(self, tree, method_name):
        """
        Helper: ensure a child cannot move relative to the master_collection.
        """
        import bpy
        master_collection = bpy.context.scene.master_collection
        for collection in tree.values():
            self.assertFalse(getattr(collection, method_name)(master_collection))

    def test_scene_collection_move_a(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        self._assert_no_move_from_master(tree, 'move_above')

        self.compare_tree_maps()

    def test_scene_collection_move_b(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        self._assert_no_move_from_master(tree, 'move_below')

        self.compare_tree_maps()

    def test_scene_collection_move_c(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        self._assert_no_move_to_master(tree, 'move_above')

        self.compare_tree_maps()

    def test_scene_collection_move_d(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        self._assert_no_move_to_master(tree, 'move_below')

        self.compare_tree_maps()


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()