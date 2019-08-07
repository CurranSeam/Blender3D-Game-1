######################################################
#
#    RenderToTexture.py        Blender 2.50
#
#    Tutorial for using RenderToTexture.py can be found at
#
#    www.tutorialsforblender3d.com
#
#    Released under the Creative Commons Attribution 3.0 Unported License.	
#
#    If you use this code, please include this information header.
#
######################################################

#import GameLogic
import GameLogic
import bge

# get current scene
scene = bge.logic.getCurrentScene()
        
# get the current controller
controller = bge.logic.getCurrentController()

# get object script is attached to
obj = controller.owner

# check to see RenderToTexture has been added
if "RenderToTexture" in obj:
				
	# update the texture
	obj["RenderToTexture"].refresh(True)

# if RenderToTexture hasn't been added 
else:
    
    # import VideoTexture module
    import VideoTexture
	
	# get a list of objects in the scene
    objList = scene.objects
            
    # get camera name being used for render to texture
    camName = obj['cam']
            
    # get camera object
    cam = objList[camName]
            
    # get the texture material ID
    matID = VideoTexture.materialID(obj, "MA" + obj['material'])
            
    # set the texture
    renderToTexture = VideoTexture.Texture(obj, matID)
            
    # get the texture image
    renderToTexture.source = VideoTexture.ImageRender(scene,cam)
            
    # save RenderToTexture as an object variable
    obj["RenderToTexture"] = renderToTexture
	