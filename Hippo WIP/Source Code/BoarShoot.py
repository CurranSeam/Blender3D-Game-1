import bge

# Get blender logic
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Get objects
player = scene.objects['Cube']
playerEmpty = scene.objects['player placeholder']
steering = cont.actuators['to player']
navMesh = str(steering.navmesh) + ".001"

# Get properties
timer = own['timer']

# Initialize sensors
alertedDone = cont.sensors['alerted done']
shootInactive = cont.sensors['shoot inactive']
nearPlayer = cont.sensors['near player']
randomShoot = cont.sensors['Random']

# Initialize enabled bone constraints
enableHandY = cont.actuators['en hand y']
enableHandZ = cont.actuators['en hand z']
enHandGunZ = cont.actuators['en handGun z']
enHandGunXY = cont.actuators['en handGun xy']
enableNeck = cont.actuators['enable neck']
enableHead = cont.actuators['enable head']
enableEyeX = cont.actuators['enable eye x']
enableEyeYZ = cont.actuators['enable eye yz']

# Initialize disabled bone constraints
disBazookaXYZ = cont.actuators['dis handToBazooka']
disableHandY = cont.actuators['dis hand y']
disableHandZ = cont.actuators['dis hand z']
disHandGunZ = cont.actuators['dis handGun z']
disHandGunXY = cont.actuators['dis handGun xy']
disableNeck = cont.actuators['disable neck']
disableHead = cont.actuators['disable head']
disableEyeX = cont.actuators['disable eye x']
disableEyeYZ = cont.actuators['disable eye yz']

# Initialize animations and actuators
alerted = cont.actuators['alerted']
trackPlayer = cont.actuators['track player']
walk = cont.actuators['walk']
aim = cont.actuators['aim']
shoot = cont.actuators['shoot']
bullet = cont.actuators['bullet']
shell = cont.actuators['shotgun shell']
flash = cont.actuators['flash']
debris = cont.actuators['shot debris']
gunSmoke = cont.actuators['gun smoke']
search = cont.actuators['search']
bazookaState = cont.actuators['bazooka']


# Shooting states based upon timer value
cont.activate(disBazookaXYZ)
if scene.objects[navMesh]['playerOn'] == False and own['seePlayer'] == True:
    cont.activate(bazookaState)
elif timer == 0:
    if own['status'] == 0:
        cont.activate(alerted)
        own['status'] = 1
    if own['hit'] == True:
        trackPlayer.object = player
    cont.activate(trackPlayer)
    #if trackPlayer.object != None:
    own['timer'] = 1
elif timer == 1 and alertedDone.positive:
    cont.deactivate(alerted)
    cont.activate(walk)
    own['timer'] = 2
elif timer == 2:
    cont.deactivate(trackPlayer)
    cont.activate(aim)
    if own['seePlayer'] == True or own['hit'] == True:
        cont.deactivate(search)
        cont.activate(enableHandY)
        cont.activate(enableHandZ)
        cont.activate(enHandGunZ)
        cont.activate(enHandGunXY)
        cont.activate(enableNeck)
        cont.activate(enableHead)
    else:
        cont.activate(search)
        cont.activate(disableHandY)
        cont.activate(disableHandZ)
        cont.activate(disHandGunZ)
        cont.activate(disHandGunXY)
        cont.activate(disableNeck)
        cont.activate(disableHead)
    cont.activate(steering) 
elif timer == 3 and randomShoot.positive and shootInactive.positive and own['seePlayer'] == True:
    cont.activate(trackPlayer)
    cont.activate(aim)
    if own['seePlayer'] == True:
        cont.deactivate(search)
    if nearPlayer.positive:
        cont.activate(enableNeck)
        cont.activate(enableHead)
        cont.activate(enHandGunZ)
        cont.activate(enableHandZ)
        cont.activate(disHandGunXY)
        cont.activate(shoot)
        cont.activate(bullet)
        cont.activate(flash)
        cont.activate(debris)
        cont.activate(gunSmoke)
        count = 0
        if shootInactive.positive:
            cont.activate(shell)
    cont.activate(steering)
elif timer == 4:
    cont.deactivate(steering)
    cont.deactivate(trackPlayer)
