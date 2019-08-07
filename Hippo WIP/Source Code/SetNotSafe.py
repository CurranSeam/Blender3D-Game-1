import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

status = own['cover_status']
last_cover = own['last_cover']

ray = cont.sensors['Ray']
moveRandom = cont.sensors['move random']

flash1 = cont.actuators['flash1']
flash2 = cont.actuators['flash2']

if ray.positive and status == 1 or moveRandom.positive and status == 1:
    cont.deactivate(flash1)
    cont.deactivate(flash2)
    cover_point = scene.objects[str(own['last_cover'])]
    cover_point['cover'] = 3
    own['cover_status'] = 0
    own.restoreDynamics()