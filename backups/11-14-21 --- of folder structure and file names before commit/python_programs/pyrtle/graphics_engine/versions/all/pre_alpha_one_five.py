import math
import turtle
import time
from config_version_one import *
import numpy as np

def pyrtle_engine():
    turtle.tracer(0,0)
    
    if useRGB == 1:
        turtle.colormode(255)
        turtle.bgcolor(bgColorR, bgColorG, bgColorB)
    else:
        turtle.bgcolor(bgColor)
    turtle.setup(windowWidth, windowHeight)
    turtle.title(windowTitle)

    #Calculations
    pixelWidth = windowWidth // displayWidth
    pixelHeight = windowHeight // displayHeight
    startingX = windowWidth / 2 * -1 - pixelWidth
    startingY = windowHeight / 2 * 1 + pixelHeight
    totalPixels = displayWidth * displayHeight
    x = startingX
    y = startingY    

    #Pixel color for testing
    pixelColor = "black"
    
    #numpy is (rows, columns) or (y,x)
    pixelCoords = np.zeros((displayHeight,displayWidth,2))
    pixelX = []
    pixelY = []
    for i in range(displayWidth):
        pixelX.append(startingX + pixelWidth * (i + 1))
    
    for i in range(displayHeight):
        pixelY.append(startingY - pixelHeight * (i + 1))
    
    arrayRow = 0
    arrayCol = 0
    
    for i in range(totalPixels):
        pixelCoords[arrayRow,arrayCol,0] = pixelX[arrayCol]
        pixelCoords[arrayRow,arrayCol,1] = pixelY[arrayRow]
        arrayCol += 1
        if arrayCol >= displayWidth:
            arrayRow += 1
            arrayCol = 0    
    
    pixel = turtle.Turtle()
    pixel.hideturtle()
    pixel.pensize(1)
    
    #Setting variables for loop
    xPos = 0
    yPos = 0
    run = 1
    count = 0
    
    pixelStartTime = time.time() 
    
    while(run == 1):
        #count += 1
        #print("Pixel Number:", count)
        #pixelStartTime = time.time()        
        
        draw_pixel(pixelCoords[yPos,xPos,0], pixelCoords[yPos,xPos,1], pixelColor, pixelStartTime, pixel)
        xPos += 1
        if xPos >= displayWidth:
            yPos += 1
            xPos = 0
        if yPos >= displayHeight:
            yPos = 0
            xPos = 0
            turtle.update()
            pixelStopTime = time.time()
            pixelTime = pixelStopTime - pixelStartTime
            print("Time to draw Frame:", pixelTime)
            pixelStartTime = time.time()
            pixelColor = "Green"

def draw_pixel(x, y, pixelColor, pixelStartTime, pixel):
    pixel.penup()
    pixel.goto(x,y)
    pixel.pencolor(pixelColor)
    pixel.fillcolor(pixelColor)
    pixel.setheading(0)
    pixel.pendown()
    pixel.begin_fill()
    for i in range(2):
        pixel.forward(windowWidth / displayWidth)
        pixel.right(90)
        pixel.forward(windowHeight / displayHeight)
        pixel.right(90)
    pixel.end_fill()
    #turtle.update()     
    #pixelStopTime = time.time()
    #pixelTime = pixelStopTime - pixelStartTime
    #print("Time to draw Pixel:", pixelTime)
    #PPS = 1 / (pixelTime + .0000000000001)
    #print("Pixels Per Second (PPS):", PPS)

pyrtle_engine()