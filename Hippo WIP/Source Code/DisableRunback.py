import bge

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()

forward = cont.sensors['walk']
back = cont.sensors['down']
backMotion = cont.actuators['back']

if forward.positive:
    cont.deactivate(backMotion)
