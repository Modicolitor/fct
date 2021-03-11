#
# Copyright (C) 2020 by Modicolitor
#
# This file is part of PuzzleUrPrint.
#
# License Text
#
# You should have received a copy of the GNU General Public License along with PuzzleUrPrint. If
# not, see <https://www.gnu.org/licenses/>.


from .ui import FC_PT_FCTree_Panel
from .operators import FC_OT_AddSingleCoupling

#from .properties import PUrPropertyGroup


#from .modalops import PP_OT_PlanarZScaleMenu


#from bpy.types import Scene, Image, Object
import bpy


#from .utils import addon_auto_imports

bl_info = {  # für export als addon
    "name": "FCT",
    "author": "Modicolitor",
    "version": (0, 1),
    "blender": (2, 91, 0),
    "location": "View3D > Tools",
    "description": "Cut your Objects into pieces and reassemble them easily after 3d printing",
    "doc_url": "http://purp.modicolitor.com/Dokumentation.html",
    "category": "Object"}

# modules = addon_auto_imports.setup_addon_modules(
#    __path__, __name__, ignore_packages=[], ignore_modules=[]
# )


classes = (
    FC_PT_FCTree_Panel,
    FC_OT_AddSingleCoupling,

)
#classes = ()
register, unregister = bpy.utils.register_classes_factory(classes)
