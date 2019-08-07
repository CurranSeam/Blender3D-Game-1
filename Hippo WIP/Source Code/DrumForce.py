import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

collide = cont.sensors['Collision']
bounce = cont.actuators['bounce']
squish = cont.actuators['squish']

armature = scene.objects['Armature']
player = scene.objects['Cube']

keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

player['jump'] = 2
if collide.positive:
    cont.activate(bounce) 
    cont.activate(squish)
    target = collide.hitObject
    own['collided'] = True
    force = [0, 0, 100000]
    local = False
    if collide.hitObject == player:
        #print("hit")
        if keyboard.events[bge.events.SPACEKEY] == JUST_ACTIVATED:
            player['jump'] = 1
            force = [0, 0, 200000] 
    target.applyForce(force, local)
    
        