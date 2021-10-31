import turtle
import os
import subprocess

from physics_config import *
from physics_calculations import *
from physics_debug_utils import *
from physics_debug_config import *

def debug_app(calibrateScreen = True, clearScreen = False, tracerOn = False, printDebugLog = False, autoOpenDebugLog = True, pathOfTextEditor = None):

    debug_calculations()
    
    if calibrateScreen is True:
        calibrate_screen(clearScreen, tracerOn)
    
    log_debug_data(printDebugLog, autoOpenDebugLog, pathOfTextEditor)
    return

def calibrate_screen(clearScreen, tracerOn):
    if clearScreen is True:
        turtle.clearscreen()
    if tracerOn is True:
        turtle.tracer(0,0)
        
    ts = turtle.Turtle()
    ts.color("red")
    ts.speed(0)
    
    for i in range(10):
        ts.penup()
        ts.goto(25 * i, 25 * i)
        ts.pendown()
        ts.forward(250 - (25 * i))
   
    if tracerOn is True:
        turtle.update()
    return

def debug_calculations(nameOfCalcuation = None):
    if nameOfCalcuation is None:
        #TODO
        return
    elif nameOfCalcuation == "dc_screenSize":
        temp_dc_ScreenSize = turtle.screensize()
        dc_screenSize = [temp_dc_ScreenSize[0], temp_dc_ScreenSize[1]]
        return dc_screenSize
    else:
        print("ERROR: Debug Calculation Not Found!")
        return
    
def log_debug_data(printDebugLog, autoOpenDebugLog, pathOfTextEditor):
    debugLog = open("Debug_Log.txt","w+")
    
    debugLog.write(double_dash_line())
    debugLog.write(blank_line())
    debugLog.write(center_text("Screen Debugging Info"))
    debugLog.write(blank_line())
    debugLog.write(dash_line())
    debugLog.write(center_text("Values Given or Set in Config (constants)"))
    debugLog.write(left_align_text("Test to see if left allign works."))
    
    dummy = list(graphSize)
    dummy[0] += -300
    dummy[1] += 300
    debugLog.write(standard_column("Graph Dimensions", "graphSize=", graphSize, dummy))
    
    debugLog.write("||\tSurrounding Buffer Width:   surroundingBuffer = " + "".join(str(surroundingBuffer)) + "\n")
    debugLog.write("Left Buffer Width:   leftBuffer = " + "".join(str(leftBuffer)) + "\n")
    debugLog.write("Right Buffer Width:   rightBuffer = " + "".join(str(rightBuffer)) + "\n")
    debugLog.write("Top Buffer Height:   topBuffer = " + "".join(str(topBuffer)) + "\n")
    debugLog.write("Bottom Buffer Height:   bottomBuffer = " + "".join(str(bottomBuffer)) + "\n")
    debugLog.write("Turtle() Default Screen Buffer Size:   defaultBuffer = " + "".join(str(defaultScreenBuffer)) + "\n\n")
 
    debugLog.write("Values Anticipated (calculated by physics_debug.py)\t\t|\t\tValues Calculated and Used (by physics_app.py)\n")
    debugLog.write("Screen Dimensions: " + "".join(str(debug_calculations("dc_screenSize"))) + "\n")    
    
    debugLog.write("Values Calculated and Used (by physics_app.py):\n")
    debugLog.write("Screen dimensions:   screenSize = " + "".join(str(screenSize)) + "\n")
        
    
    if printDebugLog is True:
        printing = True
        #TODO
    
    debugLog.close()
    
    if autoOpenDebugLog is True:
        if pathOfTextEditor is None:
            os.open("Debug_Log.txt")
        else:
            sp = subprocess.Popen([pathOfTextEditor, "Debug_Log.txt"])
    return

