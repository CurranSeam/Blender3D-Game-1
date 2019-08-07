import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

own.worldLinearVelocity*=0
own.applyForce((0,0,30*own.mass),0)