import bge

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()

head = scene.objects['pig headBox']

bulletCollide = cont.sensors['bullet']

pigHit = cont.actuators['pig hit']
duckDone = cont.sensors['duck']

if bulletCollide.positive:
    head['hit'] = True
    own['hit'] = True
if own['hit'] == True or head['hit'] == True:
    if duckDone.positive:
        cont.activate(pigHit) 