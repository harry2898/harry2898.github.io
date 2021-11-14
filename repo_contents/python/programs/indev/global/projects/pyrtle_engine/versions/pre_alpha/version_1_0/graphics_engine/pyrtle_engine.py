import math
import turtle
import time
from config import *

def pyrtle_engine():
    turtle.tracer(0,0)
    if useRGB == 1:
        turtle.colormode(255)
        turtle.bgcolor(bgColorR, bgColorG, bgColorB)
    else:
        turtle.bgcolor(bgColor)
    turtle.setup(windowWidth, windowHeight)
    turtle.title(windowTitle)
    pixelWidth = windowWidth // displayWidth
    pixelHeight = windowHeight // displayHeight
    startingX = windowWidth / 2 * -1 - pixelWidth
    startingY = windowHeight / 2 * 1 + pixelHeight
    totalPixels = displayWidth * displayHeight
    pixelColor = "black"
    x = startingX
    y = startingY
    xPos = 0
    yPos = 0
    run = 1
    count = 0
    pixel = turtle.Turtle()
    pixel.hideturtle()
    #pixel.pensize(pixelHeight)
    pixel.pensize(1)
    refresh_screen(startingX, startingY, pixelColor, 0, pixel)
    while(run == 1):
        print("Pixel Number:", count)
        pixelStartTime = time.time()
        if (count >= totalPixels):
            pixelColor = "blue"          
        if(xPos <= windowWidth - pixelWidth):
            x = startingX + xPos
            y = startingY - yPos
            xPos += pixelWidth
            refresh_screen(x, y, pixelColor, pixelStartTime, pixel)
        if(xPos > windowWidth - pixelWidth):
            x = startingX
            y = startingY - yPos - pixelHeight
            xPos = 0
            yPos += pixelHeight
            if(yPos > windowHeight - pixelHeight):
                x = startingX
                y = startingY
                xPos = 0
                yPos = 0
                refresh_screen(x, y, pixelColor, pixelStartTime, pixel)
            else:
                refresh_screen(x, y, pixelColor, pixelStartTime, pixel)
        count = count + 1


def refresh_screen(x, y, pixelColor, pixelStartTime, pixel):
    pixel.penup()
    pixel.goto(x,y)
    pixel.pencolor(pixelColor)
    pixel.fillcolor(pixelColor)
    pixel.setheading(0)
    pixel.forward(windowWidth / displayWidth)
    pixel.pendown()
    #pixel.dot(15)
    pixel.begin_fill()
    for i in range(2):
        pixel.forward(windowWidth / displayWidth)
        pixel.right(90)
        pixel.forward(windowHeight / displayHeight)
        pixel.right(90)
    pixel.end_fill()
    turtle.update()     
    pixelStopTime = time.time()
    pixelTime = pixelStopTime - pixelStartTime
    print("Time to draw Pixel:", pixelTime)
    PPS = 1 / (pixelTime + .0000000000001)
    print("Pixels Per Second (PPS):", PPS)

pyrtle_engine()