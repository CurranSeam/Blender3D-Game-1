import bge

cont = bge.logic.getCurrentController()
own = cont.owner

#Sensors
nearPlayer = cont.sensors['near player']
notNearPlayer = cont.sensors['not player']
enableIdle = cont.sensors['enable idle']

#Actuators
idle = cont.actuators['idle']
trackPlayer = cont.actuators['track player']
aim = cont.actuators['looped aim']
enableNeck = cont.actuators['enable neck']
enableHand = cont.actuators['enable hand']
enableHead = cont.actuators['enable head']
enableEyeX = cont.actuators['enable eye x']
enableEyeYZ = cont.actuators['enable eye yz']
disableNeck = cont.actuators['disable neck']
disableHand = cont.actuators['disable hand']


cont.activate(enableHead)
cont.activate(enableEyeX)
cont.activate(enableEyeYZ) 
if nearPlayer.positive:
    own['alerted'] = True
    cont.deactivate(idle)
    cont.activate(enableHand)
    cont.activate(enableNeck)
    cont.activate(aim)
    cont.activate(trackPlayer)
elif notNearPlayer.positive:
    own['alerted'] = False
    cont.deactivate(aim)
    cont.deactivate(enableHand)
    cont.activate(disableHand)
    cont.deactivate(enableNeck)
    cont.activate(disableNeck)
    cont.deactivate(trackPlayer)
    if enableIdle.positive:
        cont.activate(idle)
    else:
        cont.deactivate(idle)   
    