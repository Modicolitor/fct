#
# Copyright (C) 2020 by Modicolitor
#
# This file is part of PuzzleUrPrint.
#
# License Text
#
# You should have received a copy of the GNU General Public License along with PuzzleUrPrint. If
# not, see <https://www.gnu.org/licenses/>.

import bpy


'''UI -Elements'''


class FC_PT_FCTree_Panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Tree Options"
    bl_category = "FCT"
    #bl_options = {'DEFAULT_CLOSED'}

    @ classmethod
    def poll(cls, context):
        # if context.mode == 'OBJECT' and context.area.type == 'VIEW_3D':
        return True  # hasattr(context.scene, "PUrP")

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        flow = layout.grid_flow(row_major=True, columns=0,
                                even_columns=False, even_rows=False, align=True)
        col = flow.column()
        row = layout.row()

        subcol = col.column()

        # if not hasattr(context.scene, "PUrP"):
        #    col.operator("purp.window_draw_operator", text="Start Tutorial", icon="LIGHT_DATA")
        # else:

        col.operator("fct.mktree",
                     text="Make Tree", icon="LIGHT_DATA")
