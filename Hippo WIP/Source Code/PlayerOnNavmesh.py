import bge

# Get blender logic
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Get sensors
ray = cont.sensors['navmesh']

# Navmeshes List
navMeshes = []
for i in scene.objects:
    if "navmesh" in str(i).lower() and ".001" in str(i):
        navMeshes.append(i)

def main():
    if ray.positive:
        if ray.hitObject in navMeshes:
            ray.hitObject['playerOn'] = True
    else:
        for i in navMeshes:
            i['playerOn'] = False
main()           