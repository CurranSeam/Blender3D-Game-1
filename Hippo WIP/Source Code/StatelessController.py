import bge

# Get player, main controller, owner, scene, and scene list
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
scenes = bge.logic.getSceneList()
own = cont.owner
player = scene.objects['Cube']

# Action events
mouse = bge.logic.mouse
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

# Set hud weapon visibility from start
own.sendMessage("remove on hud", "", "hud pistol") 
own.sendMessage("remove on hud", "", "hud bazooka")
own.sendMessage("remove on hud", "", "hud revolver")
#own.sendMessage("remove on hud", "", "hud shotgun")

# Weapon array for weapons that the player has
weaponsOnPlayer = []

# Returns all rats present in the scene.
def getRatsInScene():
    ratList = []
    for object in scene.objects:
        if "rat cube" in str(object).lower():
            ratList.append(object)
    return ratList

# Returns all pigs present in the scene.
def getPigsInScene():
    pigList = []
    for object in scene.objects:
        if "pig cube" in str(object).lower():
            pigList.append(object)
    return pigList

# Returns all boars present in the scene.
def getBoarsInScene():
    boarList = []
    for i in scene.objects:
        if 'boar cube' in str(i).lower():
            boarList.append(i)
    return boarList

# Activates death state for player (hippo)
def death():
    deadState = cont.actuators['dead']
    deathMessage = cont.sensors['dead']
    if deathMessage.positive:
        #print("dead")
        cont.activate(deadState)
        
def throwItem(cont):
    throwMessage = cont.sensors['throw']
    throwItem = cont.actuators['throw item']
    if throwMessage.positive:
        throwItem.object = own['currentItem']
        cont.activate(throwItem)
        own['currentItem'] = None

# Determines which ladder player is near or on and sets 
# the ladder as a target for all rats
def playerNearLadder(cont):
    nearLadder = cont.sensors['near ladder']
    ladderCollide = cont.sensors['ladder']
    highSpotCollide = cont.sensors['high spot']
    targetLadder = ""
    if ladderCollide.positive:
        setRatTargetLadder(ladderCollide.hitObject)
    elif highSpotCollide.positive:
        highSpot = highSpotCollide.hitObject
        targetLadder = scene.objects[highSpot['attachedLadder']]
        setRatTargetLadder(targetLadder)
    elif len(nearLadder.hitObjectList) != 0:
        targetLadder = nearLadder.hitObjectList[0]
        setRatTargetLadder(targetLadder)    
    else:
        setRatTargetLadder(targetLadder)

# Sets given ladder as a target for all rats to go to
def setRatTargetLadder(ladder):
    ratList = getRatsInScene()
    for rat in ratList:
        rat['target ladder'] = ladder

# Sets player weapon booleans based on pickup and
# gives pertinent weapon ammo to player if new weapon
# is picked up.
def acquireWeapons():
    acquiredPistol = cont.sensors['gun end']
    acquiredBazooka = cont.sensors['bazooka end']
    acquiredRevolver = cont.sensors['revolver end']
    #acquiredShotgun = con.sensors['shotgun end']
    if acquiredPistol.positive:
        player['haveGun'] = True
        if player['hasPistol'] == False:
            player['hasPistol'] = True
            addWeapon("pistol")
        own.sendMessage("refill pistol", "", "")
    if acquiredBazooka.positive:
        player['haveGun'] = True
        if player['hasBazooka'] == False:
            player['hasBazooka'] = True
            addWeapon("bazooka")
        own.sendMessage("refill bazooka", "", "")
    if acquiredRevolver.positive:
        player['haveGun'] = True
        if player['hasRevolver'] == False:
            player['hasRevolver'] = True
            addWeapon("revolver")
        own.sendMessage("refill revolver", "", "")

# Adds given weapon to player's weapon collection.
# Then sets the given weapon to be the equipped weapon 
# and then set visibility accordingly.   
def addWeapon(weapon):
    weaponsOnPlayer.append(weapon)
    player['equippedWeapon'] = weapon
    if weapon == "pistol":
        own.sendMessage("show on hud", "", "hud pistol")
        own.sendMessage("remove on hud", "", "hud bazooka") 
        own.sendMessage("remove on hud", "", "hud revolver") 
    elif weapon == "bazooka":
        own.sendMessage("show on hud", "", "hud bazooka")
        own.sendMessage("remove on hud", "", "hud pistol")
        own.sendMessage("remove on hud", "", "hud revolver") 
    elif weapon == "revolver":
        own.sendMessage("show on hud", "", "hud revolver")
        own.sendMessage("remove on hud", "", "hud pistol")
        own.sendMessage("remove on hud", "", "hud bazooka") 
    elif weapon == "shotgun":
        #own.sendMessage("show on hud", "", "hud shotgun")
        own.sendMessage("remove on hud", "", "hud pistol")
        own.sendMessage("remove on hud", "", "hud bazooka") 
        own.sendMessage("remove on hud", "", "hud revolver") 

# Pre: player must possess at least one weapon.
# Controls weapon scrolling for player collection
# and then sets the chosen weapon to the equipped weapon.
def setEquippedWeapon():
    weaponAmount = len(weaponsOnPlayer)
    if player['haveGun'] == True:
        if mouse.events[bge.events.WHEELUPMOUSE] == JUST_ACTIVATED:
            if weaponAmount > 1:
                if "pistol" in weaponsOnPlayer[player['weaponIndex']]:
                    if player['hasPistol'] == True:
                        player['equippedWeapon'] = "pistol"
                        own.sendMessage("show on hud", "", "hud pistol")
                        own.sendMessage("remove on hud", "", "hud bazooka")
                        own.sendMessage("remove on hud", "", "hud revolver")
                elif "revolver" in weaponsOnPlayer[player['weaponIndex']]:
                    if player['hasRevolver'] == True:
                        player['equippedWeapon'] = "revolver"
                        own.sendMessage("show on hud", "", "hud revolver")
                        own.sendMessage("remove on hud", "", "hud bazooka")
                        own.sendMessage("remove on hud", "", "hud pistol")
                elif "shotgun" in weaponsOnPlayer[player['weaponIndex']]:
                    if player['hasShotgun'] == True:
                        player['equippedWeapon'] = "shotgun"
                elif "bazooka" in weaponsOnPlayer[player['weaponIndex']]:
                    if player['hasBazooka'] == True:
                        player['equippedWeapon'] = "bazooka"
                        own.sendMessage("show on hud", "", "hud bazooka")
                        own.sendMessage("remove on hud", "", "hud pistol")
                        own.sendMessage("remove on hud", "", "hud revolver")
                if player['weaponIndex'] < weaponAmount - 1:
                    player['weaponIndex'] += 1
                else:
                    player['weaponIndex'] = 0
            
        