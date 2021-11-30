from vpython import *

groundWidthX = 160
groundHeightY = 2
groundDepthZ = 10
groundSize = vec(groundWidthX, groundHeightY, groundDepthZ)

groundPosX = groundWidthX / 2
groundPosY = groundHeightY / -2
groundPosZ = 0
groundPos = vec(groundPosX, groundPosY, groundPosZ)

groundColor = color.green


backdropWidthX = groundWidthX
backdropHeightY = 40
backdropDepthZ = 1
backdropSize = vec(backdropWidthX, backdropHeightY, backdropDepthZ)

backdropPosX = backdropWidthX / 2
backdropPosY = backdropHeightY / 2
backdropPosZ = (backdropDepthZ / -2) + (groundPosZ - (groundDepthZ * .5))
backdropPos = vec(backdropPosX, backdropPosY, backdropPosZ)

backdropColor = color.cyan


platformWidthX = groundDepthZ
platformHeightY = groundHeightY
platformDepthZ = groundDepthZ
platformSize = vec(platformWidthX, platformHeightY, platformDepthZ)

platformPosX = groundPosX - (groundWidthX / 2) - (platformWidthX / 2)
platformPosY = platformHeightY / -2
platformPosZ = groundPosZ
platformPos = vec(platformPosX, platformPosY, platformPosZ)

platformColor = color.black


smallLineWidthX = 1
smallLineHeightY = .5
smallLineDepthZ = groundDepthZ / 4
smallLineSize = vec(smallLineWidthX, smallLineHeightY, smallLineDepthZ)
smallLineColor = color.yellow

mediumLineWidthX = 1
mediumLineHeightY = .5
mediumLineDepthZ = groundDepthZ / 2
mediumLineSize = vec(mediumLineWidthX, mediumLineHeightY, mediumLineDepthZ)
mediumLineColor = color.yellow

largeLineWidthX = 1
largeLineHeightY = .5
largeLineDepthZ = groundDepthZ
largeLineSize = vec(largeLineWidthX, largeLineHeightY, largeLineDepthZ)
largeLineColor = color.yellow

def create_ground_line(lineType, xPos):
    if type(lineType) != str:
        print("Argument 'lineType' must be type str")
        print("Was given 'lineType' =", lineType, "whose type is:", type(lineType))
    elif type(xPos) != int:
        print("Argument 'xPos' must be type int")
        print("Was given 'xPos' =", xPos, "whose type is:", type(xPos))        
    elif lineType.lower() == "small":
        box(pos = vec(xPos, (smallLineHeightY / -2) + .1, groundPosZ + (groundDepthZ * .5) - (smallLineDepthZ * .5)), size = smallLineSize, color = smallLineColor)
        #smallLinePos = vec(xPos, (smallLineHeightY / -2) + .1, groundDepthZ - (smallLineDepthZ * 1.5))
        box(pos = vec(xPos, (smallLineHeightY / -4) + .2, groundPosZ + (groundDepthZ * .5) - (smallLineDepthZ * .5)), size = vec(smallLineWidthX / 4, smallLineHeightY / 2, smallLineDepthZ), color = color.black)
        return 
    elif lineType.lower() == "medium":
        box(pos = vec(xPos, (mediumLineHeightY / -2) + .1, groundPosZ + (groundDepthZ * .5) - (mediumLineDepthZ * .5)), size = mediumLineSize, color = mediumLineColor)
        #mediumLinePos = vec(xPos, (mediumLineHeightY / -2) + .1, groundDepthZ - (mediumLineDepthZ * 1.5))
        box(pos = vec(xPos, (mediumLineHeightY / -4) + .2, groundPosZ + (groundDepthZ * .5) - (mediumLineDepthZ * .5)), size = vec(mediumLineWidthX / 4, mediumLineHeightY / 2, mediumLineDepthZ), color = color.black)
        return 
    elif lineType.lower() == "large":
        box(pos = vec(xPos, (largeLineHeightY / -2) + .1, groundPosZ + (groundDepthZ * .5) - (largeLineDepthZ * .5)), size = largeLineSize, color = largeLineColor)
        #largeLinePos = vec(xPos, (largeLineHeightY / -2) + .1, groundDepthZ - largeLineDepthZ)
        box(pos = vec(xPos, (largeLineHeightY / -4) + .2, groundPosZ + (groundDepthZ * .5) - (largeLineDepthZ * .5)), size = vec(largeLineWidthX / 4, largeLineHeightY / 2, largeLineDepthZ), color = color.black)
        return 
    else:
        print("Unkown Error in 'line_pos(lineType, xPos)")
        print("Was given 'lineType' =", lineType, "whose type is:", type(lineType))
        print("Was given 'xPos' =", xPos, "whose type is:", type(xPos))
        
def create_backdrop_horizontal_line(yPos):
    box(pos = vec(backdropPosX, yPos, backdropPosZ + .35), size = vec(backdropWidthX, 1, .5), color = color.black)
    
def create_backdrop_vertical_line(xPos):
    box(pos = vec(xPos, backdropPosY, backdropPosZ + .35), size = vec(1, backdropHeightY, .5), color = color.black)
    
    
def create_cannon():
    #trailer floor
    box(pos = vec(-2, .5, 0), size = vec(3, .1, 3), color = color.magenta)
    #trailer length side rails
    box(pos = vec(-2, .7, 1.5), size = vec(3, .3, .2), color = color.orange)
    box(pos = vec(-2, .7, -1.5), size = vec(3, .3, .2), color = color.orange)
    #trailer width side rails
    box(pos = vec(-.5, .7, 0), size = vec(.2, .3, 3), color = color.orange)
    box(pos = vec(-3.5, .7, 0), size = vec(.2, .3, 3), color = color.orange)
    # front passenger corner: top = vec(-3.6, 8.5, -1.6) bottom = vec(-3.6, .45, -1.6)
    # back passenger corner: top = vec(-.4, 8.5, -1.6) bottom = vec(-.4, .45, -1.6)
    # back driver corner: top = vec(-.4, 8.5, 1.6) bottom = vec(-.4, .45, 1.6)
    # front driver corner: top = vec(-3.6, 8.5, 1.6) bottom = vec(-3.6, .45, 1.6)
    
    #trailer passenger wheel
    cylinder(pos = vec(-2, .3, -1.7), axis = vec(0, 0, .2), radius = .6, color = color.magenta)
    #trailer driver wheel
    cylinder(pos = vec(-2, .3, 1.7), axis = vec(0, 0, .2), radius = .6, color = color.magenta)
    
    #pressure vessel
    cylinder(pos = vec(((7 * sqrt(2)) * .25) * -1, .55 + (sqrt(2) * .25), 0), axis = vec(sqrt(2) * .5, sqrt(2) * .5, 0), radius = .3, color = color.purple)
    #barrel
    cylinder(pos = vec(((5 * sqrt(2)) * .25) * -1, .55 + ((3 * sqrt(2)) * .25), 0), axis = vec((3 * sqrt(2)) * .5, (3 * sqrt(2)) * .5, 0), radius = .1, color = color.red)
    #end of barrel = vec(0, .55 + 2 * sqrt(2) [== 3.3784], 0)
    #box(pos = vec(0, .55 + (2 * sqrt(2)), 0), size = vec(.25, .25, .25), color = color.blue)

    
def set_camera(window):
    window.camera.pos = vec(groundPosX + platformPosX, 35, -90)
    #window.camera.pos = vec(platformPosX / 2, 5, -180)
    

#Initial Velocity
V = 125
#Angle of Launch
alpha = pi / 4
#Initial Height
h = 3.5

#Gravity (m/s^2)
g = 9.807

#Initial Horizontal Velocity
iVx = V * cos(alpha)
#Initial Vertical Velocity
iVy = V * sin(alpha)

def horizontal_distance_traveled(time_t):
    t = time_t
    VxDistance = iVx * t
    return VxDistance

def vertical_distance_from_ground(time_t):
    t = time_t
    VyHeight = (h + (iVy * t)) - ((g * (t ** 2)) / 2)
    return VyHeight

Vx = iVx

def Vy(time_t):
    t = time_t
    Vy = iVy - (g * t)
    return Vy

#Horizontal Acceleration
Ax = 0
#Vertical Acceleration
Ay = g * -1

timeOfFlight = (iVy + sqrt((iVy ** 2)+ ((2 * g) * h))) / g

#rangeOfProjectile = iVx * (iVy + (sqrt(iVy) ** 2) + ((2 * g) * h)) / g
rangeOfProjectile = iVx * timeOfFlight

maxHeight = h + ((V ** 2) * ((sin(alpha) ** 2) / (2 * g)))

