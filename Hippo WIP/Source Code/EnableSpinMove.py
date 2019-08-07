# redundant code
import bge

cont = bge.logic.getCurrentController()
own = cont.owner

# Get sensors
forward = cont.sensors['walk']
left = cont.sensors['left']
right = cont.sensors['right']
down = cont.sensors['down']
leftClick = cont.sensors['left button']
groundCollide = cont.sensors['ground']

# Get actuators
spinMove = cont.actuators['spin move']
smokeJump = cont.actuators['smoke jump']
rockChips = cont.actuators['rock chips']

if forward.positive and leftClick.positive and groundCollide.positive:
    cont.activate(spinMove)
    cont.activate(smokeJump)
    cont.activate(rockChips)
elif left.positive and leftClick.positive and groundCollide.positive:
    cont.activate(spinMove)
    cont.activate(smokeJump)
    cont.activate(rockChips)
elif right.positive and leftClick.positive and groundCollide.positive:
    cont.activate(spinMove)
    cont.activate(smokeJump)
    cont.activate(rockChips)
elif down.positive and leftClick.positive and groundCollide.positive:
    cont.activate(spinMove)
    cont.activate(smokeJump)
    cont.activate(rockChips)
else:
    cont.deactivate(spinMove)
    cont.deactivate(smokeJump)
    cont.deactivate(rockChips)