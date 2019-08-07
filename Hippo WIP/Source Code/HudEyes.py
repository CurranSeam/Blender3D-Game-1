import bge
import StatelessController

# Blender logic
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

# Actuators
addEyes = cont.actuators['add eyes']

# Get boars in main scene
boarList = StatelessController.getBoarsInScene()

for boar in boarList:
    if boar['timer'] == 2 and boar['seePlayer'] == False:
        if own['added'] == False:
            own['added'] = True
            cont.activate(addEyes)
        break
    if boar['timer'] != 2 or boar['seePlayer'] == True:
        own.sendMessage("remove", "", "hud_eyes")
        own['added'] = False
