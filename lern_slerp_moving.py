import bpy
from mathutils import Vector

CU = bpy.data.objects['Cube']
SU = bpy.data.objects['Suzanne']

def obj_move_to_target(obj1, obj2, rot_speed = 0.1, move_speed = 0.01, distance = 0.1):
    '''
     Рух та орієнтація обʼєкта у 3D-просторі за допомогою
     лінійної та сферичної інтерполяції векторів.
    - https://docs.blender.org/api/current/mathutils.html#mathutils.Vector.lerp
    - https://docs.blender.org/api/current/mathutils.html#mathutils.Vector.slerp
       obj1: обʼєкт що рухається
       obj2: обʼєкт-ціль, до якої рухається obj1
       rot_speed: швидкість обертання
       move_speed: швидкість руху
       distance: мінімальна дістанція наближення до цілі
    '''
    
    #====== slerp rotation =====
    
    # Змінити орієнтацію об'єкта на інтерпольований кватерніон.
    obj1.rotation_mode = 'QUATERNION'
    obj1.rotation_quaternion = interpolated_quat
    
    # Обчислити вектор напрямку.
    direction = obj1.location - obj2.location

    # Створити кватерніонні об'єкти.
    start_quat = obj1.rotation_quaternion
    end_quat = direction.to_track_quat('Y', 'Z')

    # Інтерполювати між початковим і кінцевим кватерніонами за допомогою slerp.
    interpolated_quat = start_quat.slerp(end_quat, rot_speed)

    
    #===== lerp moving =====

    if direction.length > distance:
        obj1.location = obj1.location.lerp(Vector(obj2.location), move_speed)

def game_loop(self, context):
    obj_move_to_target(SU, CU, 0.1, 0.01, 5)
    
bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(game_loop)

