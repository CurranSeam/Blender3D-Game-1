import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

status = own['status']
idleDone = cont.sensors['idle']

#flash1 = cont.actuators['flash1']
#flash2 = cont.actuators['flash2']

if idleDone.positive and status == 1:
    #cont.deactivate(flash1)
    #cont.deactivate(flash2)
    boar_spot = scene.objects[str(own['last_cover'])]
    #boar_spot['spot'] = 0
    own['status'] = 0
    own['moveSpot'] = True
    own.restoreDynamics()