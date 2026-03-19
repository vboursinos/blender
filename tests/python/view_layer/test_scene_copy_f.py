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
        See if scene copying 'FULL_COPY' is keeping collections visibility
        and selectability.
        """
        import bpy

        scene = bpy.context.scene

        enabled_lookup = [True, False, False, True]
        enabled_lookup_sub = [False, True, False]

        selectable_lookup = [True, True, False, False]
        selectable_lookup_sub = [False, True, False]
        new_collections = []

        # clean everything
        for layer in scene.view_layers:
            while layer.collections:
                layer.collections.unlink(layer.collections[0])

        # create new collections
        for i in range(4):
            collection = scene.master_collection.collections.new(str(i))
            new_collections.append(collection)

            for j in range(3):
                collection.collections.new(f"{i}:{j}")

        # link to the original scene
        for layer in scene.view_layers:
            for i, collection in enumerate(new_collections):
                layer.collections.link(collection)
                
                layer_collection = layer.collections[i]
                self.assertEqual(layer.collections[-1], layer_collection)

                layer_collection.enabled = enabled_lookup[i]
                layer_collection.selectable = selectable_lookup[i]

                for j, sub_collection in enumerate(layer_collection.collections):
                    sub_collection.enabled = enabled_lookup_sub[j]
                    sub_collection.selectable = selectable_lookup_sub[j]

        # copy scene
        bpy.ops.scene.new(type='FULL_COPY')
        new_scene = bpy.context.scene
        self.assertNotEqual(scene, new_scene)

        # update depsgraph
        for view_layer in scene.view_layers:
            view_layer.update()  # update depsgraph

        # compare scenes
        for layer, new_layer in zip(scene.view_layers, new_scene.view_layers):
            for i, collection in enumerate(layer.collections):
                new_collection = new_layer.collections[i]
                self.assertEqual(collection.enabled, new_collection.enabled)
                self.assertEqual(collection.selectable, new_collection.selectable)

                for j, sub_collection in enumerate(collection.collections):
                    new_sub_collection = new_collection.collections[j]
                    self.assertEqual(sub_collection.enabled, new_sub_collection.enabled)
                    self.assertEqual(sub_collection.selectable, new_sub_collection.selectable)


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()