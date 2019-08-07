import bge
import random

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Get objects
player = scene.objects['Cube']

# Get sensors
closeToPlayer = cont.sensors['close to player']
jumpDone = cont.sensors['not jump']
groundCollide = cont.sensors['ground']
nearLadder = cont.sensors['ladder']
notClimbing = cont.sensors['not climbing']

# Get actuators
steering = cont.actuators['to player']
run = cont.actuators['rat run']
rightHook = cont.actuators['rat right hook']
trackPlayer = cont.actuators['track player']
airMotionXY = cont.actuators['in air xy']
jump = cont.actuators['rat jump']
falling = cont.actuators['rat falling']
punchDust = cont.actuators['punch dust']
trackLadder = cont.actuators['track ladder']
walk = cont.actuators['rat walk']

# Stores all navmeshes in the scene into an array
navmeshes = []
for object in scene.objects:
    if "navmesh" in str(object).lower() and ".001" not in str(object).lower():
        navmeshes.append(object)

def main():
    cont.deactivate(walk)
    steering.navmesh = scene.objects['Navmesh']
    changedNav = False
    for i in navmeshes:
        if player.getDistanceTo(i) < player.getDistanceTo(steering.navmesh):
            steering.navmesh = i
            changedNav = True
    navSensor = str(steering.navmesh) + ".001"
    if (changedNav == True or scene.objects[navSensor]['playerOn'] == False) and groundCollide.positive: 
        cont.deactivate(rightHook)
        if own['target ladder'] != "":
            steering.target = own['target ladder']
            trackLadder.object = own['target ladder']
            cont.deactivate(airMotionXY)
            cont.deactivate(trackPlayer)
            cont.activate(steering)
            cont.activate(run)
            if nearLadder.positive:
                cont.activate(trackLadder)
        else:
            steering.target = player
            cont.deactivate(run)
            cont.deactivate(steering)
            cont.activate(jump)
            if jumpDone.positive:
                cont.deactivate(jump)
                cont.activate(falling)
                cont.activate(trackPlayer)
                if own.worldPosition.z < player.worldPosition.z + 5:
                    own.applyForce([0, 0, 140000], True)
                if own.worldPosition.x + own.worldPosition.y != player.worldPosition.x + player.worldPosition.y:
                    cont.activate(airMotionXY)
    if not closeToPlayer.positive and scene.objects[navSensor]['playerOn'] == True:
        cont.deactivate(trackLadder)
        cont.activate(airMotionXY)
        cont.deactivate(trackPlayer)
        cont.deactivate(rightHook)
        steering.target = player
        cont.activate(steering)
        cont.activate(run)
    if closeToPlayer.positive and notClimbing.positive:
        cont.deactivate(trackLadder)
        cont.deactivate(airMotionXY)
        cont.deactivate(steering)
        cont.deactivate(run)
        cont.activate(trackPlayer)
        punchBool = random.randint(0, 50)
        own.worldPosition.y = player.worldPosition.y + 2
        if punchBool == 1:
            cont.activate(rightHook)
            own.sendMessage('rat punch', "", 'stateless controller')
            cont.activate(punchDust)
            cont.deactivate(punchDust)
        cont.deactivate(rightHook)
        cont.deactivate(punchDust)
main()