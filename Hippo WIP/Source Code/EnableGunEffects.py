import bge

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()

shoot = cont.actuators['shoot']
ammo = own['ammo']
trigger = cont.sensors['Mouse']
player = scene.objects["Cube"]
aim = cont.sensors['aim']
hasPistol = player['hasPistol']

if hasPistol and aim.positive:
    if ammo >= 1 and trigger.positive:
        cont.activate(shoot)
else:
    cont.deactivate(shoot)   