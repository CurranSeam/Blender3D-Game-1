import StatelessController
import bge

# Get player, main controller, owner, scene, and scene list
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
player = scene.objects['Cube']

# Enemies and enemy blips
pigBlips = {}
ratBlips = {}
pigs = StatelessController.getPigsInScene()
rats = StatelessController.getRatsInScene()
    
for i in range(len(pigs)):
    enemyBlip = scene.addObject("enemy blip", pigs[i])
    pigBlips[pigs[i]] = enemyBlip
    enemyBlip.worldPosition.y = pigs[i].worldPosition.y
    enemyBlip.worldPosition.x = pigs[i].worldPosition.x + 1350
for i in range(len(rats)):
    enemyBlip = scene.addObject("enemy blip", rats[i])
    ratBlips[rats[i]] = enemyBlip
    enemyBlip.worldPosition.y = rats[i].worldPosition.y
    enemyBlip.worldPosition.x = rats[i].worldPosition.x + 1350

def move():
    for i in pigBlips:
        pigBlips[i].worldPosition.y = i.worldPosition.y
        pigBlips[i].worldPosition.x = i.worldPosition.x + 1350
    for i in ratBlips:
        ratBlips[i].worldPosition.y = i.worldPosition.y
        ratBlips[i].worldPosition.x = i.worldPosition.x + 1350
        
def remove():
    for i in list(pigBlips):
        if i['enemy health'] <= 0:
            pigBlips[i].endObject()
            pigBlips.pop(i, None)
    for i in list(ratBlips):
        if i['enemy health'] <= 0:
            ratBlips[i].endObject()
            ratBlips.pop(i, None)