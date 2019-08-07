import bge
import random

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

steering = cont.actuators['spot']
disableHandY = cont.actuators['dis hand y']
disableHandZ = cont.actuators['dis hand z']
disHandGunZ = cont.actuators['dis handGun z']
disHandGunXY = cont.actuators['dis handGun xy']
disableNeck = cont.actuators['disable neck']
disableHead = cont.actuators['disable head']
walk = cont.actuators['walk']
nearSpot = cont.sensors['near spot']

randNum = random.randint(0, 3)

cont.activate(disableHandY)
cont.activate(disableHandZ)
cont.activate(disHandGunXY)
cont.activate(disHandGunZ)
cont.activate(disableNeck)
cont.activate(disableHead)

if own['moveSpot'] == True and nearSpot.positive:
    if randNum == 1:
        own['target'] = nearSpot.hitObjectList[1]
    elif randNum == 2:
        own['target'] = nearSpot.hitObjectList[2]
    elif randNum == 3:
        own['target'] = nearSpot.hitObjectList[3]
    else:  
        own['target'] = nearSpot.hitObjectList[0]
    steering.target = own['target']
    #if own['target']['spot'] == 0:
    cont.activate(steering)
    cont.activate(walk)


