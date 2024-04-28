'''
    Reads the user's scripts folder in blender preferences.
    Adds subdirectories with custom scripts to the TextEditor's Templates menu.
    To use it:
        1. set path to custom scripts folder in Preferences.
        2. install the addon or run it from within TextEditor.
        3. add necessary subfolders and files to the custom scripts folder.
    
    Читає шлях до папки скриптів користувача в налаштуваннях blender.
    Додає знайдені підкаталоги з скриптами користувача до меню Templates редактора скриптів.
    Для роботи потрібно:
        1. вказати шлях до папки скриптів в налаштуваннях blender.
        2. встановити адон або виконати його код з редактора скриптів блендер.
        3. додати в папку кастомних скриптів потрібні підкаталоги та файли.
'''

bl_info = {
    "name": "My Script Templates v2",
    "author": "Oleg Shcherbyna",
    "version": (2, 0),
    "blender": (4, 0, 0),
    "location": "TEXT_EDITOR > Templates > .. custom script templates",
    "description": "Reads the user's scripts folder. Adds subdirectories with custom scripts to the TextEditor's Templates menu.",
    "warning": "",
    "doc_url": "",
    "category": "Templates",
}

import bpy, os

class TEXT_MT_template_my(bpy.types.Menu):
    bl_idname = "TEXT_MT_template_my"
    bl_label = "template_my"
    
    def draw(self, _context):
        self.path_menu(
            bpy.utils.script_paths(subdir=self.bl_label),
            "text.open",
            props_default={"internal": True},
            filter_ext=lambda ext: (ext.lower() == ".py")
        )
        
custom_templ = []

def register_custom_templ():
    
    if len(bpy.context.preferences.filepaths.script_directories) == 0:
        print("ERROR: You have to add a path to the user's scripts folder: Go to Preferences => File Paths => Script Directories")
        return
    
    subdir_list = []
    for dir in bpy.context.preferences.filepaths.script_directories:
        script_directory = bpy.context.preferences.filepaths.script_directories[dir.name].directory
        subdir_list += [name for name in os.listdir(script_directory) if "__" not in name and os.path.isdir(os.path.join(script_directory, name))]
    
    subdir_list.sort()    
    for obj_name in subdir_list:
        c = type(  'TEXT_MT_' + obj_name,
                    (TEXT_MT_template_my, ),
                    {'bl_idname': 'TEXT_MT_' + obj_name,
                    'bl_label': obj_name
                })
        custom_templ.append(c)
        bpy.utils.register_class(c)

def unregister_custom_templ():
    for c in custom_templ:
        bpy.utils.unregister_class(c)
        
def add_menu_buttons(self, context):
    for c in custom_templ:
        self.layout.menu(c.bl_idname)
        
def register():
    bpy.utils.register_class(TEXT_MT_template_my)
    register_custom_templ()
    bpy.types.TEXT_MT_templates.append(add_menu_buttons)


def unregister():
    bpy.types.TEXT_MT_templates.remove(add_menu_buttons)
    unregister_custom_templ()
    bpy.utils.unregister_class(TEXT_MT_template_my)


if __name__ == "__main__":
    register()



