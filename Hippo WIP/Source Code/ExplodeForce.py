import bge

scene = bge.logic.getCurrentScene()

def explosion(cont):
    own = cont.owner
    collisionArea = cont.sensors['blast area']
    if str(cont) == 'red chilli':
        if own['health'] <= 0:
            applyExplodeForce(own, collisionArea)
    else:
        applyExplodeForce(own, collisionArea)

def applyExplodeForce(own, collisionArea):
    for object in collisionArea.hitObjectList:
        own.sendMessage("explosion", "", str(object))
        #print(object)
        #object.applyForce(force, True)
        object.applyForce([0, 0, 110000], False)
 
def coconutHit(cont): 
    own = cont.owner
    player = scene.objects['Cube']
    hippo = scene.objects['hippo']
    smoke = cont.actuators['smoke']
    piece = cont.actuators['coconut piece']
    piece2 = cont.actuators['coconut piece 2']  
    end = cont.actuators['end']
    collided = cont.sensors['hit']
    if collided.positive:
        if own['collided'] == False:
            cont.activate(piece)
            cont.activate(piece2)
            own['collided'] = True
        #print(target)
        value = own.localOrientation[1]
        value[1] *= -10
        force = own.localOrientation[1] * -10000
        if collided.hitObject == player or collided.hitObject == hippo:
            player.applyForce(force, True)
            player.applyForce([0, 0, 200000], True)
            #target.applyMovement(value, True)
        explosion(cont)
        cont.activate(smoke)
        cont.activate(end)
        

    
        