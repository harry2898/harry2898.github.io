import turtle
from tkinter import *
import math
import time
import numpy as np

from .config import *
from .calculations import *
from .utils import *
from ...debugython.debugging_tool.debugger_tool import *

def start():    
    screen = turtle.Screen()
    screen.setup(screenSize[0],screenSize[1])    
    screen.setworldcoordinates(screenZeroZero[0], screenZeroZero[1], screenZeroZero[0] + graphSize[0], screenZeroZero[1] + graphSize[1])
    
    test = turtle.Turtle()
    test.speed(0)
    test.penup()
    
    #for i in range(8):
        #test.goto(screenCenter)
        #test.setheading(i * 45)
        #test.pendown()
        #test.forward(100)
        #test.penup()
    #test.goto(translate_coord_pair(screenCenter,-100))
    #test.setheading(270)
    #test.pendown()
    #test.circle(100)
    #test.penup()
    
    #test.goto(screenBottomLeft)
    #test.pendown()
    #test.goto(screenTopLeft)
    #test.goto(screenTopRight)
    #test.goto(screenBottomRight)
    #test.goto(screenBottomLeft)
    #test.penup()

    #test.goto(translate_coord_pair(screenBottomLeft,universalChange = 10))
    #test.pendown()
    #test.goto(translate_coord_pair(screenTopLeft, 10, -10))
    #test.goto(translate_coord_pair(screenTopRight, -10, -10, -10, [-10, -10]))
    #test.goto(translate_coord_pair(screenBottomRight, xyChange = [-10, 10]))
    #test.goto(translate_coord_pair(screenBottomLeft,10, 10, 10))
    
    debug_app(calibrateScreen = False, clearScreen = False, tracerOn = False, printDebugLog = True, autoOpenDebugLog = True, pathOfTextEditor = r"C:\Program Files (x86)\Notepad++\notepad++.exe")
    
    #test.penup()
    #test.goto(0,0)
    #test.pendown()
    #test.goto(0,600)
    #test.goto(1000,600)
    #test.goto(1000,0)
    #test.goto(0,0)    
    
    screen.exitonclick()
    
        

start()