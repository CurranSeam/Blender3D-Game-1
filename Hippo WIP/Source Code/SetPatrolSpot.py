import bge

cont = bge.logic.getCurrentController()
own = cont.owner

collide = cont.sensors['spot']
steering = cont.actuators['spot']
idle = cont.actuators['idle'] 
walk = cont.actuators['walk']

if len(collide.hitObjectList) != 0 and own['status'] == 0:
    if collide.hitObjectList[0] == own['target']: #and collide.hitObjectList[0]['spot'] == 0:
        own.worldPosition.x = collide.hitObjectList[0].worldPosition.x
        own.worldPosition.y = collide.hitObjectList[0].worldPosition.y
        own['last_cover'] = collide.hitObjectList[0]
        #own['target'] = ''
        own['status'] = 1
        cont.deactivate(steering)
        own['moveSpot'] = False
        cont.deactivate(walk)
        cont.activate(idle)
        own.suspendDynamics()