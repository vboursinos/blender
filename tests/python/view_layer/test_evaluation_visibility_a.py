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
    def test_visibility(self):
        """
        See if the depsgraph evaluation is correct
        """
        import bpy

        scene = bpy.context.scene
        window = bpy.context.window
        cube = bpy.data.objects.new('guinea pig', bpy.data.meshes.new('mesh'))

        layer = scene.view_layers.new('Visibility Test')
        if len(layer.layer_collection.children) > 0:
            layer.layer_collection.children[0].exclude = True
        window.view_layer = layer

        scene_collection_mom = bpy.data.collections.new("Mom")
        scene_collection_kid = bpy.data.collections.new("Kid")

        scene.collection.children.link(scene_collection_mom)
        scene.collection.children.link(scene_collection_kid)

        scene_collection_mom.objects.link(cube)
        scene_collection_kid.objects.link(cube)

        layer_collection_mom = layer.layer_collection.children["Mom"]
        layer_collection_kid = layer.layer_collection.children["Kid"]

        layer_collection_mom.exclude = True
        layer_collection_kid.exclude = False

        layer.update()  # update depsgraph
        self.assertTrue(cube.visible_get(), "Object should be visible")


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()