import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

nearLadder = cont.sensors['near ladder']
trackLadder = cont.actuators['track ladder']

trackLadder.object = nearLadder.hitObjectList[0] 
cont.activate(trackLadder)
#print(str(nearLadder.hitObjectList[0]))