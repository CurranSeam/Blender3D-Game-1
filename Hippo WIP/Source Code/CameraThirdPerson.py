import bge
from bge import render
g=bge.logic
scene = g.getCurrentScene()


def main():
    co = bge.logic.getCurrentController()
    o= co.owner
    
    #sensor
    mouse = co.sensors["mousesensor"]
    
    #objects
    Cube= scene.objects["Cube"]
    cameraTarget= scene.objects["cameraTarget"]
    
    #####mouse movemente
    
    movSpeed = 0.02
    rotSpeed = (0.0003, 0.0001)
    
     # mouse look
    x = (render.getWindowWidth() / 2 - mouse.position[0])
    y = (render.getWindowHeight() / 2 - mouse.position[1])
    
    
    Cube.applyRotation((0 , 0, int(x) * rotSpeed[0]), False)
    cameraTarget.applyRotation((int(y) * rotSpeed[1], 0, 0), True)
    render.setMousePosition(int(render.getWindowWidth() / 2), int(render.getWindowHeight() / 2))

def trackEnemy():
    import math
    
    controller = bge.logic.getCurrentController()
    nearEnemy = controller.sensors['near enemy']
    aiming = controller.sensors['aim']
    trackEnemy = controller.actuators['track enemy']
    
    player = bge.logic.getCurrentScene().objects['Cube']
    own = controller.owner
    
    if nearEnemy.positive and aiming.positive and player['haveGun'] == False:
        closest = 500
        for i in nearEnemy.hitObjectList:
            if own.getDistanceTo(i) < closest:
                trackEnemy.object = i
        controller.activate(trackEnemy)
        cameraTargetOrient = own.localOrientation.to_euler()
        playerOrient = player.localOrientation.to_euler()
        playerOrient[2] = cameraTargetOrient[2]
        print(math.degrees(playerOrient[2])) 
        print(math.degrees(cameraTargetOrient[2])) 
        player.localOrientation = playerOrient.to_matrix()
    else:
        trackEnemy.object = None
        controller.deactivate(trackEnemy)