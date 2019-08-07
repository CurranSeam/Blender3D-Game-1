import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

player = scene.objects['Cube']
rat = scene.objects['rat cube']
keyboard = bge.logic.keyboard
mouse = bge.logic.mouse
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
dynamics = cont.actuators['dynamics']
unparent = cont.actuators['no parent']
ratKnockdown = cont.actuators['knockdown']
thrown = cont.actuators['thrown']
playerBlasted = cont.sensors['ouch3']
restoreMass = cont.actuators['mass = 100']
notAimed = cont.sensors['not aimed']

# Animations
lay = cont.actuators['rat lay']
punched = cont.actuators['rat punched']
backroll = cont.actuators['rat backroll']
knockdown = cont.actuators['rat knockdown']
walk = cont.actuators['rat walk']
idle = cont.actuators['rat idle']

def main():
    if player['aimed'] == True:
        cont.activate(idle)
        if mouse.events[bge.events.LEFTMOUSE] == JUST_ACTIVATED or keyboard.events[bge.events.SPACEKEY] == JUST_ACTIVATED or playerBlasted.positive or notAimed.positive:
            throw()
    else:
        cont.activate(lay)
        if mouse.events[bge.events.LEFTMOUSE] == JUST_ACTIVATED or keyboard.events[bge.events.SPACEKEY] == JUST_ACTIVATED or playerBlasted.positive:
            throw()

def throw():
    cont.activate(unparent)
    cont.activate(restoreMass)
    cont.activate(dynamics)
    value = own.localOrientation[1]
    value[1] *= 2
    force = own.localOrientation[1] * 10000
    rat.applyForce(force * 50, True)
    rat.applyForce([0, 0, 100000], False)
    rat.applyMovement(-value, True)
    cont.deactivate(lay)
    cont.deactivate(punched)
    cont.deactivate(backroll)
    cont.deactivate(knockdown)
    cont.deactivate(walk)
    cont.deactivate(idle)
    cont.activate(thrown)
    cont.activate(ratKnockdown)

main()
    