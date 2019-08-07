import bge
import random

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

collide = cont.sensors['target spots']
nearSpot = cont.sensors['nearSpot']

# Logic for walking to points
if own['status'] == 0:
    if (collide.hitObjectList[0] == own['target'] or nearSpot.hitObjectList[0] == own['target']) and collide.hitObjectList[0]['cover'] == 0:
        own['wander'] = True