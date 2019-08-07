import bge

keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

def pickupObject():
    cont = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    own = cont.owner
    
    pickUpAnim = cont.actuators['pick up']
    leftMouse = cont.sensors['left button']
    nearObject = cont.sensors['near grabable']
    
    if nearObject.positive and keyboard.events[bge.events.FKEY] == JUST_ACTIVATED:
        own.sendMessage('picked up', "", str(nearObject.hitObjectList[0]))
        cont.activate(pickUpAnim)
    if nearObject.positive and leftMouse.positive: 
        own.sendMessage('thrown', "", str(nearObject.hitObjectList[0]))
        cont.deactivate(pickUpAnim)

def throwObject():
    cont = bge.logic.getCurrentController()
    scene = bge.logic.getCurrentScene()
    own = cont.owner

    # Sensors and actuators
    pickedUp = cont.sensors['picked up']
    thrown = cont.sensors['thrown']
    parentToPlayer = cont.actuators['parent player']
    unparent = cont.actuators['remove parent']
    lessMass = cont.actuators['less mass']
    restoreMass = cont.actuators['restore mass']
    collision = cont.sensors['anything']
    end = cont.actuators['end']
    
    #Objects
    hippo = scene.objects['hippo']
    statelessCont = scene.objects['stateless controller']
    
    if pickedUp.positive:
        cont.activate(lessMass)
        cont.activate(parentToPlayer)
        own.worldPosition.x = hippo.worldPosition.x
        own.worldPosition.y = hippo.worldPosition.y
        own.worldPosition.z = hippo.worldPosition.z + 2.5
        statelessCont['currentItem'] = str(own) + '.001'
    if thrown.positive:
        own.sendMessage('throw', "", 'stateless controller')
        cont.activate(end)
    
    