'''<br>Copyright (C) 2024-2025 Plasma Hive<br>https://plasmahive.com<br>plasmahivecom@gmail.com<br><br>Created by plasmahive<br><br>This file is part of Remap Materials.<br><br> Remap Materials is free software; you can redistribute it and/or<br> modify it under the terms of the GNU General Public License<br> as published by the Free Software Foundation; either version 3<br> of the License, or (at your option) any later version.<br><br> This program is distributed in the hope that it will be useful,<br> but WITHOUT ANY WARRANTY; without even the implied warranty of<br> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the<br> GNU General Public License for more details.<br><br> You should have received a copy of the GNU General Public License<br> along with this program; if not, see <https://www.gnu.org<br>/licenses>.<br>'''

bl_info = {
    "name": "Remap Materials",
    "description": "Remap multiple materials selected in the Outliner to a single material",
    "author": "plasmahive",
    "version": (1, 0, 0),
    "blender": (4, 3, 2),
    "location": "Outliner > Remap Materials",
    "wiki_url": "https://github.com/plasmahive/remap-materials/wiki",
    "doc_url": "https://github.com/plasmahive/remap-materials/wiki",
    "tracker_url": "https://github.com/plasmahive/remap-materials/issues",
    "category": "Material"
}

import bpy
from .remap_materials import OUTLINER_OT_remap_selected_materials
from .remap_materials import OUTLINER_OT_select_material_popup

def menu_func(self, context):
    self.layout.operator("outliner.remap_selected_materials", icon='MATERIAL')

def register():
    bpy.utils.register_class(OUTLINER_OT_remap_selected_materials)
    bpy.utils.register_class(OUTLINER_OT_select_material_popup)
    bpy.types.OUTLINER_MT_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OUTLINER_OT_remap_selected_materials)
    bpy.utils.unregister_class(OUTLINER_OT_select_material_popup)
    bpy.types.OUTLINER_MT_context_menu.remove(menu_func)