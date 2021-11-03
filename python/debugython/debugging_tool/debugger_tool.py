import turtle
import os
import subprocess

from config import *
from calculations import *
from debugger_files.debugger_config import *
from debugger_files.debugger_utils import *

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
    
    runDebuggerUtilsTest()
    
    #debugLog.write(make_list_all_strings("Testing to_string with only a string. Not a list.", True))
    
    #debugLog.write("||\tSurrounding Buffer Width:   surroundingBuffer = " + "".join(str(surroundingBuffer)) + "\n")
    #debugLog.write("Left Buffer Width:   leftBuffer = " + "".join(str(leftBuffer)) + "\n")
    #debugLog.write("Right Buffer Width:   rightBuffer = " + "".join(str(rightBuffer)) + "\n")
    #debugLog.write("Top Buffer Height:   topBuffer = " + "".join(str(topBuffer)) + "\n")
    #debugLog.write("Bottom Buffer Height:   bottomBuffer = " + "".join(str(bottomBuffer)) + "\n")
    #debugLog.write("Turtle() Default Screen Buffer Size:   defaultBuffer = " + "".join(str(defaultScreenBuffer)) + "\n\n")
 
    #debugLog.write("Values Anticipated (calculated by physics_debug.py)\t\t|\t\tValues Calculated and Used (by physics_app.py)\n")
    #debugLog.write("Screen Dimensions: " + "".join(str(debug_calculations("dc_screenSize"))) + "\n")    
    
    #debugLog.write("Values Calculated and Used (by physics_app.py):\n")
    #debugLog.write("Screen dimensions:   screenSize = " + "".join(str(screenSize)) + "\n")
        
    
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

def runDebuggerUtilsTest(testSubmission = None, listOfUtilsToTest = None):
    if testSubmission is None:
        testSubmission = ["words here", "more words"]
    if listOfUtilsToTest is None:
        listOfUtilsToTest = make_list_of_utils_to_test(runAllTests = True)
    for i in range(len(listOfUtilsToTest)):
        if listOfUtilsToTest[i] == 1:
            if i == 0:
                test_to_string(testSubmission)
                i += 1
            elif i == 1:
                test_retained_to_string(testSubmission)
                i += 1
            elif i == 2:
                test_make_list_all_strings(testSubmission)
                i += 1
            elif i == 3:
                test_to_list_of_chars(testSubmission)
                i += 1
            elif i == 4:
                test_retained_to_list_of_chars(testSubmission)
                i += 1
            else:
                print("Error: For Loop in debugger_tool.py on line 104")
        else:
            i += 1

def make_list_of_utils_to_test(runTest__to_string = False, runTest__retained_to_string = False, runTest__make_list_all_strings = False, runTest__to_list_of_chars = False, runTest__retained_to_list_of_chars = False, runAllTests = False):
    if runAllTests is True:
        listOfUtilsToTest = [1, 1, 1, 1, 1]
        return listOfUtilsToTest
    listOfUtilsToTest = [0, 0, 0, 0, 0]
    if runTest__to_string is True:
        listOfUtilsToTest[0] = 1
    if runTest__retained_to_string is True:
        listOfUtilsToTest[1] = 1
    if runTest__make_list_all_strings is True:
        listOfUtilsToTest[2] = 1
    if runTest__to_list_of_chars is True:
        listOfUtilsToTest[3] = 1
    if runTest__retained_to_list_of_chars is True:
        listOfUtilsToTest[4] = 1
    return listOfUtilsToTest

def test_to_string(testSubmission, expectedTestResult = None):
    testResult = to_string(testSubmission)
    print_results("to_string", testSubmission, testResult, expectedTestResult)
    return

def test_retained_to_string(testSubmission, expectedTestResult = None):
    testResult = to_string(testSubmission, True)
    print_results("to_string", testSubmission, testResult, expectedTestResult, "retained = True")
    return
    
def test_make_list_all_strings(testSubmission, expectedTestResult = None):
    testResult = make_list_all_strings(testSubmission)
    print_results("make_list_all_strings", testSubmission, testResult, expectedTestResult)
    return
    
def test_to_list_of_chars(testSubmission, expectedTestResult = None):
    testResult = to_list_of_chars(testSubmission)
    print_results("to_list_of_chars", testSubmission, testResult, expectedTestResult)
    return

def test_retained_to_list_of_chars(testSubmission, expectedTestResult = None):
    testResult = to_list_of_chars(testSubmission, True)
    print_results("to_list_of_chars", testSubmission, testResult, expectedTestResult, "retained = True")
    return

def print_results(functionTested, testSubmission, testResult, expectedTestResult, optionalFunctionArgument = None):
    if optionalFunctionArgument is None:
        print(functionTested, "(", testSubmission, ")")
    else:
        print(functionTested, "(", testSubmission, ",", optionalFunctionArgument, ")")
    if (expectedTestResult is None):
        print("     Test Result:", testResult)
        print("     Result Type:", type(testResult))
        print("")
        return
    else:
        print("     Test Result:         ", testResult)
        print("     Expected Test Result:", expectedTestResult)
        print("     Test Result Correct:", (testResult == expectedTestResult) is True)
        print("     Result Type:         ", type(testResult))
        print("     Expected Result Type:", type(expectedTestResult))
        print("     Result Type Correct:", (type(testResult) == type(expectedTestResult)) is True)
        print("")
        return        