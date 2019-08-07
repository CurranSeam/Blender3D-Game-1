import bge
g=bge.logic

import mathutils
from mathutils import Vector
scene = g.getCurrentScene()



co = bge.logic.getCurrentController()
o= co.owner


ray = co.sensors["Ray"]
untouchables = ['melee cube']

normal_vec = Vector(ray.hitNormal)

Camera = scene.objects["Camera"]


if ray.positive and str(ray.hitObject) not in untouchables:
	Camera.worldPosition= ray.hitPosition
	Camera.localPosition.y += 1.3
