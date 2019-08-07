import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = scene.objects['Cube']

cont.owner.localOrientation = player.localOrientation 
cont.owner.worldPosition.y = player.worldPosition.y
cont.owner.worldPosition.x = player.worldPosition.x + 1350