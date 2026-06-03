**IMPORTANT**: make sure the header title matches exactly

## ^^artemis_code^^

# SPDX-FileCopyrightText: 2017-2022 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later
#
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
    def test_object_delete_data(self):
        """
        Verify that deleting an object via bpy.data.objects.remove() properly
        updates all related collections to ensure consistency.
        """
        self.do_object_delete('DATA')


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    UnitTesting._extra_arguments = setup_extra_arguments(__file__)
    unittest.main()