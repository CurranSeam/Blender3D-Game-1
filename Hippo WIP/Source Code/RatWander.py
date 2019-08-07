import bge
import random

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

def main():

    # coverpoint array with spots to walk to
    spots = []
    for i in scene.objects:
        if 'cover_point' in str(i):
            spots.append(i)
        
    # Actuators
    rat = scene.objects['rat cube']
    steering = cont.actuators['spot']
    walk = cont.actuators['rat walk']
    
    # Animations
    lay = cont.actuators['rat lay']
    punched = cont.actuators['rat punched']
    backroll = cont.actuators['rat backroll']
    knockdown = cont.actuators['rat knockdown']
    walk = cont.actuators['rat walk']
    idle = cont.actuators['rat idle']
    
    cont.deactivate(idle)
    cont.deactivate(lay) 
    cont.deactivate(knockdown)
    cont.deactivate(backroll)
    cont.deactivate(punched)

    # Logic for walking to points
    own['wander'] = False
    randNum = random.randint(0, len(spots) - 1)
    targetSpot = spots[randNum]
    own['target'] = targetSpot
    steering.target = targetSpot
    cont.activate(steering)
    cont.activate(walk)
main() 