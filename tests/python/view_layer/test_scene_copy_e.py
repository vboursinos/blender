# SPDX-FileCopyrightText: 2017-2022 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

# ############################################################
# Importing - Same For All Render Layer Tests
# ############################################################

import unittest

from view_layer_common import (
    ViewLayerTesting,
    setup_extra_arguments,
)


# ############################################################
# Testing
# ############################################################

class UnitTesting(ViewLayerTesting):
    def test_shared_layer_collections_copy_full(self):
        """
        See if scene copying 'FULL_COPY' is working for scene collections
        with a shared object
        """
        import bpy

        layer = bpy.context.view_layer

        original_cube = layer.objects.get('Cube')
        self.assertIsNotNone(original_cube, "Original 'Cube' object not found in the view layer")
        
        original_cube.select_set(True)
        self.assertTrue(original_cube.select_get())

        bpy.ops.scene.new(type='FULL_COPY')
        new_layer = bpy.context.view_layer

        self.assertNotEqual(layer, new_layer)
        
        new_cube = new_layer.objects.get('Cube.001')
        self.assertIsNotNone(new_cube, "Copied 'Cube.001' object not found in the new view layer")
        
        self.assertNotEqual(original_cube, new_cube)
        self.assertTrue(new_cube.select_get())


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()