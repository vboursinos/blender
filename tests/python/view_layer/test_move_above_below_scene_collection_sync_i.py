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

    def _do_move_and_compare(self, move_callable):
        tree = self.setup_tree()
        self.assertFalse(move_callable(tree))
        self.compare_tree_maps()

    def test_scene_collection_move_a(self):
        """
        Test outliner operations
        """
        self._do_move_and_compare(lambda t: t['C'].move_above(t['2']))

    def test_scene_collection_move_b(self):
        """
        Test outliner operations
        """
        self._do_move_and_compare(lambda t: t['C'].move_below(t['2']))

    def test_scene_collection_move_c(self):
        """
        Test outliner operations
        """
        self._do_move_and_compare(lambda t: t['C'].move_above(t['cat']))

    def test_scene_collection_move_d(self):
        """
        Test outliner operations
        """
        self._do_move_and_compare(lambda t: t['C'].move_below(t['cat']))


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()