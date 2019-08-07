import bge
import random

cont = bge.logic.getCurrentController()
own = cont.owner

timer = own['timer']
random_boolean = cont.sensors['Random']
healthChange = cont.sensors['health change']

#sensor actuators
shoot_act = cont.sensors['shoot act']
aim_act = cont.sensors['aim']
duck_act = cont.sensors['duck']
crouch_act = cont.sensors['crouchIdle']
reload_act = cont.sensors['reload']
getUp_act = cont.sensors['getUp']
pigHit_act = cont.sensors['pig hit']
bulletRay = cont.sensors['bullet']
#mag_act = cont.sensors['magazine']

#normal actuators
idle_c = cont.actuators['crouchIdle']
getup = cont.actuators['getUp']
aim = cont.actuators['aim']
shoot = cont.actuators['shoot']
bullet = cont.sensors['bullet']
duck = cont.actuators['duck']
#magazine = cont.actuators['magazine']
reload = cont.actuators['reload']
flash1 = cont.actuators['flash1']
flash2 = cont.actuators['flash2']
bullet = cont.actuators['spawn bullet']

randNum = random.randint(0, 2)
if healthChange.positive:
    own['timer'] = 7
    cont.deactivate(idle_c)
    cont.deactivate(getup)
    cont.deactivate(aim)
    cont.deactivate(shoot)
    cont.deactivate(duck)
    #cont.deactivate(magazine)
    cont.deactivate(reload)
if timer == 0 and duck_act.positive and randNum == 0:
    own['timer'] = 1
    own['headCons'] = True
    cont.activate(idle_c)
elif timer == 0 and duck_act.positive and randNum == 1:
    own['timer'] = 2
elif timer == 1 and crouch_act.positive or timer == 2:
    cont.deactivate(idle_c)
    cont.activate(getup)
    own['timer'] = 3
elif timer == 3 and getUp_act.positive:
    cont.deactivate(getup)
    own['neckHandCons'] = True
    cont.activate(aim)
    own['timer'] = 4
elif timer == 4 and random_boolean.positive and own['ammo'] > 0 and shoot_act.positive and aim_act.positive:
    own['ammo'] -= 1
    cont.activate(shoot)
    cont.activate(flash1)
    cont.activate(flash2)
    cont.activate(bullet)
    if bulletRay.positive:
        if str(bulletRay.hitObject) == 'Cube':
            own.sendMessage('hit', "", 'Cube')
elif timer == 4 and own['ammo'] == 0 and shoot_act.positive:
    own['neckHandCons'] = False
    cont.deactivate(shoot)
    own['timer'] = 5
    cont.activate(duck)
elif timer == 5 and duck_act.positive:
    own['headCons'] = False
    cont.deactivate(duck)  
    cont.activate(reload)
    #cont.activate(magazine) 
    own['timer'] = 6
elif timer == 6 and reload_act.positive: #and mag_act.positive
    cont.deactivate(reload)
    #cont.deactivate(magazine)
    own['ammo'] = 20
    own['timer'] = 0
elif timer == 7 and pigHit_act.positive:
    own['neckHandCons'] = False
    cont.activate(duck)
    own['timer'] = 0