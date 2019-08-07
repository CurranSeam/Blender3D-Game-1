import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

player = scene.objects['Cube']
rat = scene.objects['rat cube']
nearPlayer = cont.sensors['close to player']
keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
pickedUpState = cont.actuators['picked up']
gun = scene.objects['head empty']
upEmpty = scene.objects['UP']
trackDown = cont.actuators['track down']

# Animations
lay = cont.actuators['rat lay']
punched = cont.actuators['rat punched']
backroll = cont.actuators['rat backroll']
knockdown = cont.actuators['rat knockdown']
walk = cont.actuators['rat walk']
idle = cont.actuators['rat idle']
run = cont.actuators['rat run']

# Parent actuators
parentToCube = cont.actuators['parent Cube']
parentToHippo = cont.actuators['parent hippo']

if nearPlayer.positive and keyboard.events[bge.events.FKEY] == JUST_ACTIVATED:
    if player['aimed'] == True:
        for i in range(70):
            cont.activate(trackDown)
        cont.activate(parentToCube)
        own.worldPosition.x = upEmpty.worldPosition.x
        own.worldPosition.y = upEmpty.worldPosition.y
        own.worldPosition.z = upEmpty.worldPosition.z + 2
    else:
        cont.activate(parentToHippo)
        own.worldPosition.x = gun.worldPosition.x
        own.worldPosition.y = gun.worldPosition.y
        own.worldPosition.z = gun.worldPosition.z + 2
    cont.deactivate(run)
    cont.deactivate(lay)
    cont.deactivate(punched)
    cont.deactivate(backroll)
    cont.deactivate(knockdown)
    cont.deactivate(walk)
    cont.deactivate(idle)
    #own.applyRotation([-1.57, 0, 0], True)
    cont.activate(pickedUpState)