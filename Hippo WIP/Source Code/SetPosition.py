import bge

cont = bge.logic.getCurrentController()
own = cont.owner

collide = cont.sensors['Collision']
steering = cont.actuators['Steering']
duck = cont.actuators['duck'] 

if len(collide.hitObjectList) != 0 and own['cover_status'] == 0:
    if collide.hitObjectList[0] == own['target'] and collide.hitObjectList[0]['cover'] == 0:
        own.worldPosition.x = collide.hitObjectList[0].worldPosition.x
        own.worldPosition.y = collide.hitObjectList[0].worldPosition.y
        own['last_cover'] = collide.hitObjectList[0]
        own['target'] = ''
        own['cover_status'] = 1
        cont.deactivate(steering)
        cont.activate(duck)
        #own.suspendDynamics()