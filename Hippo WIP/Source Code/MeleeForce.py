import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

rat = scene.objects['rat cube']
collide = cont.sensors['Collision']
#smoke = cont.actuators['smoke']
ratKnockdown = cont.actuators['knockdown']
steering = cont.actuators['to player']
ratRun = cont.actuators['rat run']
end = cont.actuators['end']
ratHealthSubtract = cont.actuators['health -= 25']

if collide.positive:
    if own['collided'] == False:
        #cont.activate(smoke)
        own['collided'] = True
    target = collide.hitObject
    #print(target)
    value = own.localOrientation[1]
    value[1] *= -10
    force = own.localOrientation[1] * -10000
    if collide.hitObject == rat:
        rat.applyForce(force * 1.5, True)
        rat.applyForce([0, 0, 70000], False)
        #target.applyMovement(value, True)
        cont.deactivate(steering)
        cont.deactivate(ratRun)
        cont.activate(ratHealthSubtract)
        cont.activate(ratKnockdown)
    cont.activate(end) 