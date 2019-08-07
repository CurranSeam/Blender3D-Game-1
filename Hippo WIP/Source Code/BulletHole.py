from bge import logic as GameLogic
from mathutils import Vector
c = GameLogic.getCurrentController()
own = c.owner
         
space = 0.003
         
# sensors
ray = c.sensors["ray"]        
         
# actuator
spawn = c.actuators["spawn"]
         
if ray.positive:
 # Get info
  pos_vec = Vector(ray.hitPosition)
  normal_vec = Vector(ray.hitNormal)
         
 # make object
  spawn.instantAddObject()
  bullet_hole = spawn.objectLastCreated
         
 # position hole
  bullet_hole.alignAxisToVect(normal_vec.xyz, 2, 1)
  normal_vec.magnitude = space
  bullet_hole.worldPosition = (pos_vec + normal_vec).xyz