import bge

cont = bge.logic.getCurrentController()
own = cont.owner

near = cont.sensors['Near']
steering = cont.actuators['Steering']
run = cont.actuators['run']
dirt = cont.actuators['dirt']
trackPlayer = cont.actuators['track player']

if near.positive:
    short_dist = 150
    dist_object = own['target']
    for i in near.hitObjectList:
        if own.getDistanceTo(i) < short_dist and i['cover'] == 0:
            short_dist = own.getDistanceTo(i)
            own['target'] = i      
    steering.target = own['target']
    cont.activate(steering)
    cont.deactivate(trackPlayer)
if own['cover_status'] == 0:
    cont.activate(run)
    cont.activate(dirt)
else:
    cont.deactivate(run)
    cont.deactivate(dirt)