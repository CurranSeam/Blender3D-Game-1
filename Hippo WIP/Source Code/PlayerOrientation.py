import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Sensors
forward = cont.sensors['walk']
left = cont.sensors['left']
right = cont.sensors['right']
down = cont.sensors['down']
run = cont.sensors['run'] 
#groundCollide = cont.sensors['ground']

# Actuators
trackUp = cont.actuators['up slow']
trackLeft = cont.actuators['left']
trackRight = cont.actuators['right']
trackDown = cont.actuators['back']
trackUpLeft = cont.actuators['upleft']
trackUpRight = cont.actuators['upright']
trackDownLeft = cont.actuators['downleft']
trackDownRight = cont.actuators['downright']


def main():
    if own.state == 1:
        own['aimed'] = False
        mainTrack()
    else:
        own['aimed'] = True
        aimTrack()

def mainTrack():
    if run.positive and forward.positive and not down.positive:
        cont.activate(trackUp)
        cont.deactivate(trackDown)
        cont.deactivate(trackLeft)
        cont.deactivate(trackRight)
        cont.deactivate(trackUpLeft)
        cont.deactivate(trackUpRight)
        cont.deactivate(trackDownLeft)
        cont.deactivate(trackDownRight)
    else:
        if forward.positive:
            cont.activate(trackUp)
        if left.positive and not run.positive:
            cont.activate(trackLeft)
        if right.positive and not run.positive:
            cont.activate(trackRight)
        if forward.positive and left.positive:
            cont.activate(trackUpLeft)
        if forward.positive and right.positive:
            cont.activate(trackUpRight)
        if down.positive:
            cont.activate(trackDown)
        if down.positive and left.positive:
            cont.activate(trackDownLeft)
        if down.positive and right.positive:
            cont.activate(trackDownRight)
        cont.deactivate(trackUp)
        cont.deactivate(trackDown)
        cont.deactivate(trackLeft)
        cont.deactivate(trackRight)
        cont.deactivate(trackUpLeft)
        cont.deactivate(trackUpRight)
        cont.deactivate(trackDownLeft)
        cont.deactivate(trackDownRight)

def aimTrack():
    cont.activate(trackUp)
    if forward.positive:
        cont.activate(trackUp)
    if left.positive:
        cont.activate(trackLeft)
    if right.positive:
        cont.activate(trackRight)
    if forward.positive and left.positive:
        cont.activate(trackUpLeft)
    if forward.positive and right.positive:
        cont.activate(trackUpRight)
    if down.positive:
        cont.activate(trackUp)
    if down.positive and left.positive:
        cont.activate(trackUpRight)
    if down.positive and right.positive:
        cont.activate(trackUpLeft)
    cont.deactivate(trackUp)
    cont.deactivate(trackDown)
    cont.deactivate(trackLeft)
    cont.deactivate(trackRight)
    cont.deactivate(trackUpLeft)
    cont.deactivate(trackUpRight)
    cont.deactivate(trackDownLeft)
    cont.deactivate(trackDownRight)

main()