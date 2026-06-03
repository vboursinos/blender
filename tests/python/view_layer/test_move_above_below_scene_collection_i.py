# SPDX-FileCopyrightText: 2017-2022 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

# ############################################################
# Importing - Same For All Render Layer Tests
# ############################################################

import unittest

from view_layer_common import (
    MoveSceneCollectionTesting,
    setup_extra_arguments,
)


# ############################################################
# Testing
# ############################################################

class UnitTesting(MoveSceneCollectionTesting):
    def get_reference_scene_tree_map(self):
        # original tree, no changes
        return self.get_initial_scene_tree_map()

    def _assert_move_will_fail(self, move_func, target_key):
        """
        Helper to assert a move operation is not allowed and the tree remains consistent.
        """
        tree = self.setup_tree()
        self.assertFalse(getattr(tree['C'], move_func)(tree[target_key]))
        self.compare_tree_maps()

    def test_scene_collection_move_a(self):
        """
        Test outliner operations
        """
        self._assert_move_will_fail('move_above', '2')

    def test_scene_collection_move_b(self):
        """
        Test outliner operations
        """
        self._assert_move_will_fail('move_below', '2')

    def test_scene_collection_move_c(self):
        """
        Test outliner operations
        """
        self._assert_move_will_fail('move_above', 'cat')

    def test_scene_collection_move_d(self):
        """
        Test outliner operations
        """
        self._assert_move_will_fail('move_below', 'cat')


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()