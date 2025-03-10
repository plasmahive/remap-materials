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

class OUTLINER_OT_remap_selected_materials(bpy.types.Operator):
    """Remap Materials from Outliner"""
    bl_idname = "outliner.remap_selected_materials"
    bl_label = "Remap Materials"

    selected_materials = set()

    def execute(self, context):
        self.selected_materials.clear()

        for area in context.screen.areas:
            if area.type == 'OUTLINER':
                # Get selected materials from Outliner
                for material in bpy.data.materials:
                    if material in context.selected_ids:
                        self.selected_materials.add(material)

        # If no materials were selected, show a warning
        if not self.selected_materials:
            self.report({'WARNING'}, "No materials selected in the Outliner")
            return {'CANCELLED'}

        # Open the popup for material selection
        bpy.ops.outliner.select_material_popup('INVOKE_DEFAULT')
        return {'FINISHED'}

class OUTLINER_OT_select_material_popup(bpy.types.Operator):
    """Select a Material"""
    bl_idname = "outliner.select_material_popup"
    bl_label = "Remap Selected Materials"

    material_options: bpy.props.EnumProperty(
        name="New Material",
        description="Select a material",
        items=lambda self, context: [(mat.name, mat.name, "") for mat in bpy.data.materials] if bpy.data.materials else [("None", "None", "No Materials Available")]
    )

    def execute(self, context):
        chosen_material = bpy.data.materials.get(self.material_options)
        if not chosen_material:
            self.report({'WARNING'}, "No material selected")
            return {'CANCELLED'}

        # Apply the chosen material to all selected Outliner materials
        selected_names = []
        for mat in OUTLINER_OT_remap_selected_materials.selected_materials:
            selected_names.append(mat.name)
            self.apply_material(mat, chosen_material)

        self.report({'INFO'}, f"Remapped {', '.join(selected_names)} to {chosen_material.name}")
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def apply_material(self, target_material, chosen_material):
        target_material.user_remap(chosen_material)

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

if __name__ == "__main__":
    register()
