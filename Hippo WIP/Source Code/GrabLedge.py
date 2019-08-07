import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    scene = bge.logic.getCurrentScene()
    player = scene.objects["Cube"]

    grabRay = cont.sensors['Ray']
    groundRay = cont.sensors['ground']
    poleRay = cont.sensors['pole ledge']
    
    #bge.render.drawLine(own.children[0].worldPosition+(own.children[0].worldOrientation.col[2]*-1),own.children[0].worldPosition,(1,0,0))
    
    if grabRay.positive and not groundRay.positive:
        own.worldLinearVelocity*=0
        own.applyForce((0,0,30*own.mass),0)
        player['ledgeGrab'] = True
    elif poleRay.positive and not groundRay.positive:
        own.worldLinearVelocity*=0
        own.applyForce((0,0,30*own.mass),0)
        player['poleGrab'] = True
    else:
        player['ledgeGrab'] = False
        player['poleGrab'] = False
main()
