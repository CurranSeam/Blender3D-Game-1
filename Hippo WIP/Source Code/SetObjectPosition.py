import bge

cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Get Objects
camera = scene.objects['Camera']
planecamera = scene.objects['Planecamera']
ledgeRay = scene.objects['ledge ray']

# Set camera to first person view location
def setCameraThirdPerson():
    own.worldPosition = planecamera.worldPosition

# Set camera to third person view location
def setCameraFirstPerson():
    own.worldPosition.x = ledgeRay.worldPosition.x
    own.worldPosition.y = ledgeRay.worldPosition.y - 1
    own.worldPosition.z = ledgeRay.worldPosition.z - 0.2