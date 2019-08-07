import bge

# Get blender logic
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Get objects
player = scene.objects['Cube']
hippo = scene.objects['hippo']
playerEmpty = scene.objects['player placeholder']
steering = cont.actuators['to player']
navMesh = str(steering.navmesh) + ".001"

# Get sensors
radar = cont.sensors['seePlayer']

# Get actuators
trackPlayer = cont.actuators['track player']

# Determines if enemy saw player
for obj in radar.hitObjectList:
    #print(obj)
    if obj is own.rayCastTo(obj, radar.distance):
        if obj == player or obj == hippo or own['hit'] == True:
            own['seePlayer'] = True
            trackPlayer.object = player
            steering.target = player
            if scene.objects[navMesh]['playerOn'] == True:
                if own['timer'] > 1:
                    own['timer'] = 3
        elif obj != player or obj != hippo:
            own['seePlayer'] = False
            if scene.objects[navMesh]['playerOn'] == True:
                playerEmpty.worldPosition.x = player.worldPosition.x
                playerEmpty.worldPosition.y = player.worldPosition.y
                #playerEmpty.worldPosition.z = player.worldPosition.z
            steering.target = playerEmpty
            if own['timer'] > 1:
                trackPlayer.object = None
                own['timer'] = 2
            else:
                trackPlayer.object = playerEmpty
        elif own['timer'] == 4 and own['seePlayer'] == False:
            trackPlayer.object = None
            steering.target = None