from vpython import *
from vpython.no_notebook import stop_server

import os
import signal

from example_config import *

def physics_test():
    print("Starting Program")
    window = canvas(background = color.white)
    create_env()
    set_camera(window)
    projectile = sphere(pos = vec(0, h, 0), radius = .25, color = color.orange, make_trail = True)
    #box(pos = vec(0,0,-5), size = vec(1,1,1), color = color.blue)
    #box(pos = vec(0,0,0), size = vec(1,1,1), color = color.cyan)
    #box(pos = vec(0,0,5), size = vec(1,1,1), color = color.magenta)
    keyPressed = ""
    print("Starting Loop")
    print(timeOfFlight)
    count = 0
    simMaxHeight = projectile.pos.y
    #while keyPressed != "end":
    while projectile.pos.y >= 0:
        rate(50)
        t = count * .02
        oldProjectileHeight = projectile.pos.y
        projectile.pos.x = horizontal_distance_traveled(t) / 10
        #print(horizontal_distance_traveled(t))
        projectile.pos.y = vertical_distance_from_ground(t) / 10
        #print(vertical_distance_from_ground(t))
        #keyPressed = scene.waitfor("keyup")
        #key_input(keyPressed)
        #keyPressed = keyPressed.key
        if projectile.pos.y > oldProjectileHeight:
            simMaxHeight = projectile.pos.y
        count += 1
    print("Sim Flight Time:", count * .02, "seconds. Expected:", timeOfFlight, "seconds.")
    print("Sim Final Distance:", projectile.pos.x * 10, "meters. Expected:", rangeOfProjectile, "meters.")
    print("Sim Max Height:", simMaxHeight * 10, "meters. Expected:", maxHeight, "meters.")
    
    return
        
        #scene.bind("keyup", key_input)

def create_env():
    ground = box(pos = groundPos, size = groundSize, color = groundColor)
    backdrop = box(pos = backdropPos, size = backdropSize, color = backdropColor)
    platform = box(pos = platformPos, size = platformSize, color = platformColor)
    #lines
    for i in range(groundWidthX + 1):
        if i % 40 == 0:
            create_ground_line("large", i)
            create_backdrop_vertical_line(i)
        elif i % 20 == 0:
            create_ground_line("medium", i)
            create_backdrop_vertical_line(i)
        elif i % 10 == 0:
            create_ground_line("small", i)
    for i in range(backdropHeightY + 1):
        if i % 10 == 0:
            create_backdrop_horizontal_line(i)
    create_cannon()
    print("Created Enviroment")
    return

def key_input(evt):
    keyPressed = evt.key
    print("Key Pressed =", keyPressed)
    if keyPressed == "end":
        stop()
    else:
        return

def stop():
    print("Stopping Program")
    os.kill(os.getpid(), signal.SIGINT)



physics_test()


print("End of Code")
#time.sleep(5)



#print("Stopped Server")