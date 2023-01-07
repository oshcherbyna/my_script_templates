'''
    Adds a custom sub-menu to menu Templates.

    Додає до меню Templates субменю з власними скриптами.
    Для роботи потрібно:
        1. вказати шлях до папки скриптів в налаштуваннях blender
        2. розмістити там папку з власними скриптами та вказати
         її назву в bpy.utils.script_paths(subdir="templates_my"),
'''


bl_info = {
    "name": "My Script Templates",
    "author": "Oleg Shcherbyna",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "location": "TEXT_EDITOR > Templates > My Templates",
    "description": "Adds a custom sub-menu to menu Templates",
    "warning": "",
    "doc_url": "",
    "category": "Templates",
}

import bpy


class TEXT_MT_templates_my(bpy.types.Menu):
    bl_idname = "TEXT_MT_templates_my"
    bl_label = "My Templates"

    def draw(self, _context):
        self.path_menu(
            bpy.utils.script_paths(subdir="templates_my"),
            "text.open",
            props_default={"internal": True},
            filter_ext=lambda ext: (ext.lower() == ".py")
        )

def add_menu_button(self, context):
    self.layout.menu("TEXT_MT_templates_my")

        
def register():
    bpy.utils.register_class(TEXT_MT_templates_my)
    bpy.types.TEXT_MT_templates.append(add_menu_button)


def unregister():
    bpy.utils.unregister_class(TEXT_MT_templates_my)
    bpy.types.TEXT_MT_templates.remove(add_menu_button)


if __name__ == "__main__":
    register()

