import bge

cont = bge.logic.getCurrentController()
own = cont.owner

scene = bge.logic.getSceneList()

for i in scene:
    for j in i.objects:
        if 'text' in str(j).lower():
            j.resolution = 4