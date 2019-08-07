import bge

# Get blender logic
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Get sensors
randomShoot = cont.sensors['Random']
steering = cont.actuators['to player']
navMesh = str(steering.navmesh) + ".001"

# Get actuator sensors
reloadDone = cont.sensors['reload done']
alertedDone = cont.sensors['alerted done']
playerHit = cont.sensors['player hit']

# Get actuators
trackPlayer = cont.actuators['track player']
patrolState = cont.actuators['patrol']
shotgunState = cont.actuators['shotgun']
walk = cont.actuators['walk']
bazookaAim = cont.actuators['bazooka aim']
coconut = cont.actuators['coconut']
smoke = cont.actuators['smoke']
debris = cont.actuators['rock chips']
reload = cont.actuators['bazooka reload']
alerted = cont.actuators['alerted']

# Enabled bone constraints
enHandBazooka = cont.actuators['handToBazooka']
enBazookaZ = cont.actuators['en bazooka z']
enableHandY = cont.actuators['en hand y']
enableHead = cont.actuators['enable head']

# Disabled bone constraints
disHandBazooka = cont.actuators['dis handToBazooka']
disHandGunXY = cont.actuators['dis handGun xy']
disHandGunZ = cont.actuators['dis handGun z']
disableHandY = cont.actuators['dis hand y']
disBazookaZ = cont.actuators['dis bazooka z']
disableHead = cont.actuators['disable head']


def main():
    own.suspendDynamics()
    state = own['bazookaState']
    cont.activate(disableHandY)
    cont.activate(disHandGunXY)
    cont.activate(disHandGunZ)
    cont.activate(disableHead)
    if own['seePlayer'] == True or own['hit'] == True:
        trackPlayer.object = scene.objects['Cube']
        cont.activate(trackPlayer)
        cont.activate(enBazookaZ)
    if state == 0:
        state0()
    elif state == 1 and alertedDone.positive:
        state1()
        own['bazookaState'] = 2
    elif state == 2 and randomShoot.positive and reloadDone.positive and own['seePlayer'] == True:
        state2()
    elif scene.objects[navMesh]['playerOn'] == True and own['seePlayer'] == True or scene.objects[navMesh]['playerOn'] == True and playerHit.positive:
        shotgun()
    elif own['seePlayer'] == False and own['hit'] == False and own.getDistanceTo('Cube') > 100:
        patrol()

def state0():
    if own['status'] == 0:
        cont.activate(alerted)
        own['status'] = 1
    own['hit'] = False
    own['bazookaState'] = 1

def state1():
    alertedAnim = False
    while alertedAnim:
        if alertedDone.positive:
            alertedAnim = True
    else:
        cont.deactivate(alerted)
        cont.activate(enHandBazooka)
        cont.activate(enableHandY)
        cont.activate(bazookaAim)

def state2():
    if own['seePlayer'] == True:
        cont.activate(trackPlayer)
        cont.activate(enableHead)
        cont.activate(smoke)
        cont.activate(debris)
        cont.activate(coconut)
        cont.activate(disHandBazooka)
        cont.activate(disableHandY)
        cont.activate(reload)
    else:
        trackPlayer.object = None
        cont.activate(disableHead)
        cont.activate(disBazookaZ)
        cont.deactivate(enBazookaZ)
    
def shotgun():
    cont.deactivate(trackPlayer)
    trackPlayer.object = None
    cont.activate(walk)
    own['bazookaState'] = 0
    own.restoreDynamics()
    cont.activate(shotgunState)

def patrol():
    cont.deactivate(trackPlayer)
    cont.deactivate(steering)
    own['bazookaState'] = 0
    own['hit'] = False
    own.restoreDynamics()
    cont.activate(patrolState)

main()