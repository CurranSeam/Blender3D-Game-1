import bge
from mathutils import Vector

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
         
space = 1.5
         
# sensors
ray = cont.sensors["surface ray"]        
         
if ray.positive:
    # Get info
    pos_vec = Vector(ray.hitPosition)
    normal_vec = Vector(ray.hitNormal)
         
    # position hole
    own.alignAxisToVect(normal_vec.xyz, 2, 1)
    normal_vec.magnitude = space
    own.worldPosition = (pos_vec + normal_vec).xyz