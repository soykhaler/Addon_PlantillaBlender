bl_info = {
    "name": "Plantilla base blender",
    "author": "SoyKhaler",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "Render",
    "description": "Crea una plantilla para crear tus propios addons en blender",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
import mathutils

#funciones

def main(context):
   
#----------------------------------------------------SCRIPT AQUI---------------------------------------------------------------
   
   

#--------------------------------------------------------INTERFAZ GRÁFICA------------------------------------------------------

class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Ejecutar automatización"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)

# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access)
def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.simple_operator()

#interfaz grafica 


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Base para addons"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

       
       
        # Big render button
        layout.label(text="Ejecutar automatización ")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.simple_operator")


def register():
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
