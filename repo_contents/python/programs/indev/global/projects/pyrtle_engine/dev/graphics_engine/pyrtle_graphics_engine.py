import math
import turtle
import time
import numpy as np
import random

from config import *
from active_performance_reporter import *

#from graphics_engine.config import *
#from graphics_engine.active_performance_reporter import *

#from .config import *
#from .performance_tester import *

#Configures and runs Pyrtle Engine
def pyrtle_engine():
    #Creates a turtle screen named "turtle".
    turtle.tracer(0,0)
    
    #Checks the config to see whether to use RGB or string color names
    if useRGB == 1:
        #Config is set to use RGB
        #Sets colormode of "turtle" to RGB
        turtle.colormode(255)
        #Sets the background color of "turtle"
        turtle.bgcolor(bgColorR, bgColorG, bgColorB)
    else:
        #Config is set to use string color names
        #Sets the background color of "turtle"
        turtle.bgcolor(bgColor)
    '''
    offSet = 15
    '''
    winOffSet = 9 #9
    #Checks the config for the window dimensions and sets "turtle" accordingly
    turtle.setup(windowWidth+winOffSet, windowHeight+winOffSet)
    #Checks the config for the window title and sets "turtle" accordingly
    turtle.title(windowTitle)
    
    #screenBoarder = turtle.Turtle()
    #screenBoarder.color("green")
    ##screenBoarder.speed(0)
    #screenBoarder.penup()
    #boarderOffSet = 5
    #screenBoarder.goto(windowWidth / -2 - boarderOffSet, windowHeight / 2 + boarderOffSet)
    #screenBoarder.pendown()
    ##print(screenBoarder.pos())
    #for i in range(2):
        #screenBoarder.forward(windowWidth + (boarderOffSet * 2))
        ##print(screenBoarder.pos())
        #screenBoarder.right(90)
        #screenBoarder.forward(windowHeight + (boarderOffSet * 2))
        #screenBoarder.right(90)
        ##print(screenBoarder.pos())    

    #Calculates the dimensions of the pixels displayed within "turtle"
    pixelWidth = windowWidth // displayWidth
    pixelHeight = windowHeight // displayHeight
    #Calculates the location of the top left most pixel within "turtle" --- Starting point for drawing pixels
    '''
    startingX = windowWidth / -2 - pixelWidth /1.5
    startingY = windowHeight / 2 + pixelHeight /1.5
    '''
    startingXOffSet = 3 #3
    startingYOffSet = 2 #2 (3 for 64 x 48)
    startingX, startingY = (windowWidth / -2) + (pixelWidth / 2) - startingXOffSet, (windowHeight / 2) - (pixelHeight / 2) + startingYOffSet
    
    #Calculates the total number of pixels displayed within "turtle"
    totalPixels = displayWidth * displayHeight
    
    #**NOTE: numpy is (rows, columns) or (y,x)**
    #Creates a 3D array of zeros whose 2D dimesions are equal to the displayed pixel resolution within "turtle" along with two 3D layers of debth
    #The array's 2D coordinates define the pixel's location within "turtle"
    #The array's 3D 'depth' coordinates define the x and y coordinates of that location within "turtle"
    pixelCoords = np.zeros((displayHeight,displayWidth,2))
    #Creates a 2D array to hold the x coordinate of each pixel's location witin "turtle"
    pixelX = []
    #Creates a 2D array to hold the y coordinate of each pixel's location witin "turtle"
    pixelY = []
    #Populates "pixelX" with the x coordinate of each pixel's location witin "turtle"
    for i in range(displayWidth):
        if i == 0:
            pixelX.append(startingX)
        else:
            pixelX.append(startingX + (pixelWidth * i))
    #Populates "pixelY" with the y coordinate of each pixel's location witin "turtle"
    for i in range(displayHeight):
        if i == 0:
            pixelY.append(startingY)
        else:
            pixelY.append(startingY - (pixelHeight * i))
    
    #2D coordinates of "pixelCoords" --- Used within the loop below to track and populate "pixelCoords"
    arrayRow = 0
    arrayCol = 0
    
    #Populates "pixelCoords" with each pixel's respective x and y coordinate at the 2D coordinate location of the pixel within "turtle"
    for i in range(totalPixels):
        #Populates the pixel's x coordinate into "pixelCoords" at its 2D coordinate location within "turtle"
        pixelCoords[arrayRow,arrayCol,0] = pixelX[arrayCol]
        #Populates the pixel's y coordinate into "pixelCoords" at its 2D coordinate location within "turtle"
        pixelCoords[arrayRow,arrayCol,1] = pixelY[arrayRow]
        #Moves the loop one position to the right in respect to the 2D coordinates of "pixelCoords"
        arrayCol += 1
        #If the current 2D coordinate row of "pixelCoords" is full; moves the loop down one row then over to the left most coordinate within that row
        if arrayCol >= displayWidth:
            #Moves the loop one possition down in respect to the 2D coordinates of "pixelCoords"
            arrayRow += 1
            #Moves the loop to the left most coordinate within the new row
            arrayCol = 0    
    
    #Creates a turtle named "pixel"
    pixel = turtle.Turtle()
    #Sets the body of "pixel" to be invisible
    pixel.hideturtle()
    #Sets the body of "pixel" to be square shape
    pixel.shape("square")
    #Sets the ability to resize the body of "pixel" to be changable/ definable
    pixel.resizemode("user")
    #**NOTE: pixelScale = .45 for 64 x 48   ---    .95 for 32 x 24     ---    1.95 for 16 x 12**
    #The scale/ size that will be assigned to "pixel"
    pixelScaleX = round(pixelWidth / 19, 2)
    pixelScaleY = round(pixelHeight / 19, 2)
    #
    #TESTING -- LEAVE:
    #pixel.shapesize(pixelWidth,pixelHeight)
    #
    #Sets the size/ scale of the body of "pixel"
    pixel.shapesize(pixelScaleX,pixelScaleY,0)
    #Sets "pixel" in the 'do not draw' state
    pixel.penup()
    
    #2D coordinates of "pixelCoords" --- Used within the loop below to track the current pixel being drawn by "pixel" within "turtle"
    xPos = 0
    yPos = 0

    '''
    #The number of frames that have been drawn by "pixel" within "turtle" and rendered by "turtle"
    frames_rendered = 0
    
    #The time at which "pixel" begins drawing pixels within "turtle"
    loop_start_time = time.time()    
    #The time at which the current frame begins being drawn by "pixel" within "turtle"
    frame_start_time = time.time()
    '''

    #line = ""
    #with open("pixel_coords.txt", "w+") as f:
        #for i in range(31):
            #for j in range(24):
                ##lineList.append(pixelCoords[i][j])
                #line = "".join(line + "[" + str(pixelCoords[j][i][0]) + ", " + str(pixelCoords[j][i][1]) + "] ")
            #line = "".join(line + "\n")
            ##print(line)
            #f.write(line)
            #line = ""
    
    #reportInterval --> Number of frames --- if equal to 0: updates every frame
    reportInterval = 0
    pyrtleGraphicsEngine = active_performance_reporter(reportInterval, [displayWidth, displayHeight], detailedReport = True, includeAcronymInfo = True)
    
    fullColor = True
    
    #Variable used to keep Pyrtle Engine's while loop going
    run = 1    
    while(run == 1):
        #**TESTING: generates a random RGB value for the pixel being drawn by "pixel" within "turtle"**
        if fullColor is True:
            p_color_r = random.randrange(255)
            p_color_g = random.randrange(255)
            p_color_b = random.randrange(255)
        else:
            color = random.randint(0, 2)
            if color == 0:
                p_color_r = 0
                p_color_g = 0
                p_color_b = 255
            elif color == 1:
                p_color_r = 0
                p_color_g = 255
                p_color_b = 0
            else:
                p_color_r = 255
                p_color_g = 0
                p_color_b = 0
        #Uses "pixel" to draw the defined pixel within "turtle"
        draw_pixel(pixelCoords[yPos,xPos,0], pixelCoords[yPos,xPos,1], p_color_r, p_color_g, p_color_b, pixel)
        #Moves the loop one position to the right in respect to the 2D coordinates of the displayed pixel resolution within "turtle"
        xPos += 1
        #If the current 2D coordinate row of the displayed pixel resolution within "turtle" is full; >>> 
        #>>> moves the loop down one row then over to the left most coordinate within that row
        if xPos >= displayWidth:
            #Moves the loop one possition down in respect to the 2D coordinates of the displayed pixel resolution within "turtle"
            yPos += 1
            #Moves the loop to the left most coordinate within the new row
            xPos = 0
        #If the current 2D coordinate row of the displayed pixel resolution within "turtle" is full and it is the last coordinate row; >>>
        #>>> resets the position of the loop to the top left most coordinate 
        #>>> updates "turtle" therefore rendering the frame drawn by "pixel"
        #>>> clears the current pixels drawn by "pixel" to reduce lag, as, since "turtle" has been updated, clearing the pixels will not impact the frame currently rendered
        if yPos >= displayHeight:
            #Resets the position of the loop to the top left most coordinate
            yPos = 0
            xPos = 0
            #Updates "turtle" rendering the pixels drawn by "pixel"
            turtle.update()
            
            pyrtleGraphicsEngine.report_performance()
            '''
            #The time at which the current frame drawn by "pixel" is rendered by "turtle"
            frame_finish_time = time.time()
            #The amount of time taken for "pixel" to draw and "turtle" to render the current frame
            frame_time = frame_finish_time - frame_start_time
            #Increases the total number of frames drawn by "pixel" and rendered by "turtle" by one
            frames_rendered += 1
            #**TESTING: logs the performance of the Pyrtle Engine using the given metrics**
            if performanceTesterReportInterval == -1:
                pass
            elif performanceTesterReportInterval == 0:
                report_performance(loop_start_time, frame_time, frames_rendered)
            elif frames_rendered == 1:
                report_performance(loop_start_time, frame_time, frames_rendered)
            elif frames_rendered % performanceTesterReportInterval == 0:
                report_performance(loop_start_time, frame_time, frames_rendered)
            #Sets the time at which the new frame begins being drawn by "pixel" within "turtle"
            frame_start_time = time.time()
            '''
            
            #Clears the current pixels drawn by "pixel" to reduce lag
            pixel.clearstamps()

#Uses "pixel" to draw the defined pixel within "turtle"                
def draw_pixel(x, y, p_color_r, p_color_g, p_color_b, pixel):
    #Moves "pixel" to the specified 2D coordinate loaction of the displayed pixel resolution within "turtle"
    pixel.goto(x,y)
    #Sets colormode of "pixel" to RGB
    turtle.colormode(255)
    #Sets the color of the body of "pixel"
    pixel.color(p_color_r,p_color_g,p_color_b)
    #Tells "pixel" to draw a pixel at its current location colored the same as the color of its body
    pixel.stamp()

#Starts Pyrtle Engine
pyrtle_engine()

#TODO
#Add addition "pixel" turtles to "draw_pixel" and make sure they work with the loop
#Try and draw multiple pixels each loop