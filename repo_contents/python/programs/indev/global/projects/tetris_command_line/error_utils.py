from checker_utils import *
from config import *

#Up to date
def general_error(functionName, argumentNames, argumentValues, causeOfError = None, valuesThatCausedError = None, printThis = None, iterateThroughPrintThis = False, generatedErrorFunctionErrorReport = None):
    error_report("ERROR", functionName, argumentNames, argumentValues, causeOfError, valuesThatCausedError, printThis, iterateThroughPrintThis, generatedErrorFunctionErrorReport)

#Up to date
def unknown_error(functionName, argumentNames, argumentValues, printThis = None, iterateThroughPrintThis = False, generatedErrorFunctionErrorReport = None):
    error_report("UNKNOWN ERROR", functionName, argumentNames, argumentValues, printThis, iterateThroughPrintThis, generatedErrorFunctionErrorReport)

#Up to date
def dev_error(functionName, argumentNames, argumentValues, causeOfError = None, valuesThatCausedError = None, printThis = None, iterateThroughPrintThis = False, generatedErrorFunctionErrorReport = None):
    error_report("DEV ERROR", functionName, argumentNames, argumentValues, causeOfError, valuesThatCausedError, printThis, iterateThroughPrintThis, generatedErrorFunctionErrorReport)

#Up to date
def not_int_error(functionName, argumentNames, argumentValues):
    error_report("NOT INT ERROR", functionName, argumentNames, argumentValues, causeOfError = "At least one of the given arguments is not an int!")

#Up to date
#Prints, empty returns only when disabled
#detailed_error_report and error_report Could be condensed/ optimized
def error_report(errorType, functionName, argumentNames, argumentValues, causeOfError = None, valuesThatCausedError = None, printThis = None, iterateThroughPrintThis = False, generatedErrorFunctionErrorReport = None):
    if errorReportingEnabled is False:
        return
    textBreak = ""
    for i in range(40):
        textBreak = textBreak + "-"
    print(textBreak)
    if detailedErrorReportingEnabled is True:
        detailed_error_report(errorType, functionName, argumentNames, argumentValues, causeOfError, valuesThatCausedError, printThis, iterateThroughPrintThis, generatedErrorFunctionErrorReport)
    else:
        print("\t\t*ERROR REPORT*")
        print(errorType.upper(), "- Function Name:", functionName)
        print("Argument Names:", argumentNames)
        print("Argument Values:", argumentValues)
        argumentNamesAndValuesPairedList = combine_lists_into_pairs(argumentNames, argumentValues)
        if type(argumentNamesAndValuesPairedList) == list:
            print("Argument Names and Argument Values Paired List", argumentNamesAndValuesPairedList)
        if causeOfError is not None:
            print("Cause of Error:", causeOfError)
        if valuesThatCausedError is not None:
            print("Values That Caused Error:", valuesThatCausedError)
        print_this(printThis, iterateThroughPrintThis)
        if generatedErrorFunctionErrorReport is not None:
            print_error_function_error_report(generatedErrorFunctionErrorReport)
    print(textBreak)

#Up to date
#Prints, does not return
#detailed_error_report and error_report Could be condensed/ optimized
def detailed_error_report(errorType, functionName, argumentNames, argumentValues, causeOfError = None, valuesThatCausedError = None, printThis = None, iterateThroughPrintThis = False, generatedErrorFunctionErrorReport = None):
    print("\t\t*DETAILED ERROR REPORT*")
    print(errorType.upper(), "- Function Name:", functionName)
    analyze_variable("Argument Names", argumentNames)
    analyze_variable("Argument Values", argumentValues)
    argumentNamesAndValuesPairedList = combine_lists_into_pairs(argumentNames, argumentValues)
    if type(argumentNamesAndValuesPairedList) == list:
        print("Argument Names and Argument Values Paired List", argumentNamesAndValuesPairedList)
    if causeOfError is not None:
        print("Cause of Error:", causeOfError)
    if valuesThatCausedError is not None:
        analyze_variable("Values That Caused Error", valuesThatCausedError)
    print_this(printThis, iterateThroughPrintThis)
    if generatedErrorFunctionErrorReport is not None:
        print_error_function_error_report(generatedErrorFunctionErrorReport)    

#Up to date
#Success returns list --- Failure returns None
#Does not print
#Uses a crude system to validate list
def generate_error_function_error_report(errorFunctionName, causeOfError = None, valuesThatCausedError = None, printThis = None, iterateThroughPrintThis = False):
    #MAKE SURE TO UPDATE THIS IF CHANGES ARE MADE!!!
    numOfArgumentsForThisFunction = 5
    generatedErrorFunctionErrorReport = []
    #Error Check
    generatedErrorFunctionErrorReport.append(numOfArgumentsForThisFunction)    
    generatedErrorFunctionErrorReport.append(errorFunctionName)
    generatedErrorFunctionErrorReport.append(causeOfError)
    generatedErrorFunctionErrorReport.append(valuesThatCausedError)
    generatedErrorFunctionErrorReport.append(printThis)
    generatedErrorFunctionErrorReport.append(iterateThroughPrintThis)
    #Error Check (add one as numOfArgumentsForThisFunction does not include itself)
    if len(generatedErrorFunctionErrorReport) != (generatedErrorFunctionErrorReport[0] + 1):
        error_function_error_report_error(generatedErrorFunctionErrorReport, duringGeneration = True, errorFunctionName, causeOfError, valuesThatCausedError, printThis, iterateThroughPrintThis)
        return None
    return generatedErrorFunctionErrorReport

#Up to date
#Prints, (somewhat crudely) does not return
def print_error_function_error_report(generatedErrorFunctionErrorReport):
    if is_iterable(generatedErrorFunctionErrorReport, notString = True) is False:
        error_function_error_report_error(generatedErrorFunctionErrorReport, duringGeneration = False)
        return
    #Error Check (add one as numOfArgumentsForThisFunction does not include itself)
    if len(generatedErrorFunctionErrorReport) != (generatedErrorFunctionErrorReport[0] + 1):
        error_function_error_report_error(generatedErrorFunctionErrorReport, duringGeneration = False)
        return
    print("ERROR FUNCTION ERROR - Error Function Name:", generatedErrorFunctionErrorReport[1])
    if generatedErrorFunctionErrorReport[2] is not None:
        print("Cause of Error:", generatedErrorFunctionErrorReport[2])
    if generatedErrorFunctionErrorReport[3] is not None:
        analyze_variable("Values That Caused Error", generatedErrorFunctionErrorReport[3])
    print_this(generatedErrorFunctionErrorReport[4], generatedErrorFunctionErrorReport[5])

#Up to date
#Prints does not return    
def error_function_error_report_error(generatedErrorFunctionErrorReport, duringGeneration = False, errorFunctionName = None, causeOfError = None, valuesThatCausedError = None, printThis = None, iterateThroughPrintThis = False):
    if duringGeneration is False:
        print("ERROR FUNCTION ERROR REPORT ERROR - Error Function Name: print_error_function_error_report")
        analyze_variable("Generated Error Function Error Report", generatedErrorFunctionErrorReport)
    else:
        print("ERROR FUNCTION ERROR REPORT ERROR - Error Function Name: generate_error_function_error_report")
        print("Error Function Name:", errorFunctionName)
        print("Cause of Error:", causeOfError)
        print("Values That Caused Error:", valuesThatCausedError)
        print_this(printThis, iterateThroughPrintThis)
        analyze_variable("Generated Error Function Error Report", generatedErrorFunctionErrorReport)

#Up to date
#Prints, does not return
#Warnings and error take up a lot of space
def print_this(printThis, iterateThroughPrintThis):
    if printThis is not None:
        if iterateThroughPrintThis is True:
            isIterable = is_iterable(printThis)
            if isIterable is True:
                print("Print This:")
                for i in range(len(printThis)):
                    print(printThis[i])
            else:
                print("PRINT THIS ERROR - given argument iterateThroughPrintThis =", iterateThroughPrintThis, "  but argument printThis is of type:", type(printThis), "  which is not iterable")
                print("Printing argument printThis non iteratively:")
                print("Print This:", printThis)
        else:
            print("Print This:", printThis)
    if (printThis is None) and (iterateThroughPrintThis is True):
        print("WARNING - PRINT THIS --- given argument iterateThroughPrintThis =", iterateThroughPrintThis, "  but argument printThis has value:", printThis)   

#Up to date
#Prints, does not return
def analyze_variable(nameOfVariableToAnalyze, variableToAnalyze):
    print(nameOfVariableToAnalyze, ": ", variableToAnalyze)
    print("Type of", nameOfVariableToAnalyze, ": ", type(variableToAnalyze))
    if is_iterable(variableToAnalyze, notString = True):
        print("Length of", nameOfVariableToAnalyze, ": ", len(variableToAnalyze))
        typeOfValuesInVariable = []
        for i in range(len(variableToAnalyze)):
            typeOfValuesInVariable.append([variableToAnalyze[i], type(variableToAnalyze[i])])
        print("Type of", nameOfVariableToAnalyze, "Contents: ", typeOfValuesInVariable)

#Up to date
#Success returns list and does not print --- Failure returns False and does print
#Warnings and error take up a lot of space
def combine_lists_into_pairs(listOne, listTwo):
    errorType = None
    if (is_iterable(listOne, notString = True) is False) and (is_iterable(listTwo, notString = True) is False):
        pairedLists = [listOne, listTwo]
        print("WARNING - Combine Lists into Pairs --- Neither given argument was iterable")
        print("Given listOne =", listOne, "  With Type of:", type(listOne))
        print("Given listOne =", listTwo, "  With Type of:", type(listTwo))
        print("Combined the two arguments into a pair --- Result may be buggy")
        return pairedLists
    elif (is_iterable(listOne, notString = True) is False) or (is_iterable(listTwo, notString = True) is False):
        errorType = "type_error"
    elif len(listOne) != len(listTwo):
        errorType = "length_error"
    elif len(listOne) == len(listTwo):
        pairedLists = []
        for i in range(len(listOne)):
            pairedLists.append([listOne[i], listTwo[i]])
        return pairedLists
    else:
        errorType = "unknown_error"
    if errorType == "type_error":
        errorFunctionCauseOfError = "Only one of the given arguments was iterable"
    elif errorType == "length_error":
        errorFunctionCauseOfError = "The given arguments do not have equal lengths"
    elif errorType == "unknown_error":
        errorFunctionCauseOfError = "Unknown"
    else:
        errorFunctionCauseOfError = "Unknown --- Returned an unrecognized value"
    errorFunctionName = "combine_lists_into_pairs"
    errorFunctionValuesThatCausedError = [listOne, listTwo]
    print_error_function_error_report(generate_error_function_error_report(errorFunctionName, causeOfError = errorFunctionCauseOfError, valuesThatCausedError = errorFunctionValuesThatCausedError))    
    return False
    