import bmesh
import bpy
import mathutils
from math import radians, sqrt
import numpy as np
from bpy.types import Scene, Image, Object

from .functions import make_fctree
import copy


class FC_OT_AddSingleCoupling(bpy.types.Operator):
    '''Add a new Connector to the scene at the position of the 3D cursor. It will be mapped to the selected or the last center object and  the shape will be defined by the current settings in this panel.'''

    bl_label = "Make A Tree"
    bl_idname = "fct.mktree"
    bl_options = {'REGISTER', "UNDO"}

    @classmethod
    def poll(cls, context):

        return True

    def execute(self, context):
        make_fctree(context)
        return{"FINISHED"}
