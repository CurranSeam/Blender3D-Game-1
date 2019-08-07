import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Dirt sensors
w = cont.sensors['w']
a = cont.sensors['a']
s = cont.sensors['s']
d = cont.sensors['d']
shift = cont.sensors['shift']
groundCollide = cont.sensors['ground']

# Dirt actuator
dirt = cont.actuators['dirt']

if (w.positive or a.positive or s.positive or d.positive or shift.positive) and groundCollide.positive:
    cont.activate(dirt)