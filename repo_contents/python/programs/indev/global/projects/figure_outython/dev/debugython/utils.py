from collections.abc import Iterable

from debugython.config import *


def blank_line():
    text = multi_char(space, charLineLength, True, True)
    return text

def empty_line():
    return nextLine

def dash_line():
    text = multi_char(dash, charLineLength, True, True)
    return text

def double_dash_line():
    text = multi_char(doubleDash, charLineLength, True, True)
    return text

#def multi_tab(numTabs, beginning = False, end = False, givenList = None, returnList = False):
    #if givenList is None:
        #charList = []
    #else:
        #charList = list(givenList)
    
    #if beginning is True:
        #charList.append(lineStart)
    #for i in range(numTabs):
        #charList.append(tab)
    #if end is True:
        #charList.append(lineEnd)
    #if returnList is True:
        #return charList
    #else:
        #text = ""
        #text = to_string(charList)
        #return text    
    
def multi_char(char, numChar, beginning = False, end = False, givenList = None, returnList = False):
    if givenList is None:
        charList = []
    else:
        charList = list(givenList)
    if beginning is True:
        if char == "=":
            charList.append(doubleDashLineStart)
        else:
            charList.append(lineStart)
    for i in range(numChar):
        charList.append(char)
    if end is True:
        if char == "=":
            charList.append(doubleDashLineEnd)
        else:
            charList.append(lineEnd)
    if returnList is True:
        return charList
    else:
        text = ""
        text = to_string(charList)
        return text    

def to_string(thingToBeStringified, retained = False):
    if isinstance(thingToBeStringified, Iterable):
        if retained is False:
            unjoinedStringifiedThing = list(map(str, thingToBeStringified))
            joinedStringifiedThing = "".join(unjoinedStringifiedThing)
            return joinedStringifiedThing
        else:
            stringifiedThing = str(thingToBeStringified)
            return stringifiedThing
    else:
        stringifiedThing = str(thingToBeStringified)
        return stringifiedThing

def make_list_all_strings(listToBeStringified):
    if type(listToBeStringified) != list:
        print("Error with 'make_list_all_strings(listToBeStringified)' in 'debugger_files.debugger_utils.py' on 'Line 68' :")
        print("'listToBeStringified' must be type 'list'")
        print("Was given:  '", listToBeStringified, "'  Which is type:  '", type(listToBeStringified), "'")
        print("Returned given 'listToBeStringified' unaltered")
        print("")
        return listToBeStringified
    stringifiedList = list(map(str, listToBeStringified))
    return stringifiedList

def to_list_of_chars(thingToBeCharified, retained = False):
    charifiableThing = to_string(thingToBeCharified, retained)
    charifiedThing = list(map(str, charifiableThing))
    return charifiedThing

def prepend(thingBeingPrependedTo, thingBeingPrepended, returnAsTypeOfThingBeingPrependedTo = True, returnAsTypeOfThingBeingPrepended = False, forceReturnAsType = None, retained = False):
    returnType = None
    if (forceReturnAsType is not None):
        if (type(forceReturnAsType) != str):
            print("Error with 'prepend()' in 'debugger_files.debugger_utils.py' on 'Line 93' :")
            print("'forceReturnAsType' must be type 'str'")
            print("Was given:   '", forceReturnAsType, "'   Which is type:   '", type(forceReturnAsType), "'")
            print("Completed prepend and returned using the defualt return setting 'returnAsTypeOfThingBeingPrependedTo = True'")
            print("")
            returnType = "default"
        elif (forceReturnAsType.lower() != "str") and (forceReturnAsType.lower() != "list"):
            print("Error with 'prepend()' in 'debugger_files.debugger_utils.py' on 'Line 93' :")
            print("'forceReturnAsType' must be equal to either 'str' or 'list'")
            print("Was given:   '", forceReturnAsType, "'")
            print("Completed prepend and returned using the defualt return setting 'returnAsTypeOfThingBeingPrependedTo = True'")
            print("")
            returnType = "default"
        elif forceReturnAsType.lower() == "str":
            returnType = "str"
        elif forceReturnAsType.lower() == "list":
            returnType = "list" 
        else:
            print("Unknown Error with 'prepend()' in 'debugger_files.debugger_utils.py' on 'Line 93' :")
            print("'forceReturnAsType' must be type 'str' and must be equal to either 'str' or 'list'")
            print("Was given:   '", forceReturnAsType, "'   Which is type:   '", type(forceReturnAsType), "'")
            print("Completed prepend and returned using the defualt return setting 'returnAsTypeOfThingBeingPrependedTo = True'")
            print("")
            returnType = "default"
    elif returnAsTypeOfThingBeingPrepended is True:
        if (returnAsTypeOfThingBeingPrependedTo is True) and ((returnAsTypeOfThingBeingPrependedTo is True)):
            print("Error with 'prepend()' in 'debugger_files.debugger_utils.py' on 'Line 93' :")
            print("Both 'returnAsTypeOfThingBeingPrependedTo' and 'returnAsTypeOfThingBeingPrepended' were set to '= True'")
            print("Completed prepend and overrode the defualt return setting 'returnAsTypeOfThingBeingPrependedTo = True'")
            print("Returned using the return setting 'returnAsTypeOfThingBeingPrepended = True'")
            print("")
            returnType = "inverse"
        else:
            returnType = "inverse"
    elif (returnAsTypeOfThingBeingPrependedTo is True):
        returnType = "default"
    elif ((returnAsTypeOfThingBeingPrependedTo is False) and (returnAsTypeOfThingBeingPrependedTo is False) and (forceReturnAsType is None)):
        print("Error with 'prepend()' in 'debugger_files.debugger_utils.py' on 'Line 93' :")
        print("None of the return settings were enabled. One must be used")
        print("Completed prepend and returned using the defualt return setting 'returnAsTypeOfThingBeingPrependedTo = True'")
        print("")
        returnType = "default"
    else:
        print("Unknown Error with 'prepend()' in 'debugger_files.debugger_utils.py' on 'Line 93' :")
        print("Could not determine return settings")
        print("Was given:   ' returnAsTypeOfThingBeingPrependedTo =", returnAsTypeOfThingBeingPrependedTo, "'   ' returnAsTypeOfThingBeingPrepended =", returnAsTypeOfThingBeingPrepended, "'   ' forceReturnAsType =", forceReturnAsType, "'")
        print("Completed prepend and returned using the defualt return setting 'returnAsTypeOfThingBeingPrependedTo = True'")
        print("")
        returnType = "default"
    if returnType == "default":
        if (type(thingBeingPrependedTo) == str):
            if (type(thingBeingPrepended) != list):
                prependedString = to_string([thingBeingPrepended, thingBeingPrependedTo], retained)
                return prependedString
            else:
                prependedList = list(thingBeingPrependedTo.insert(0, thingBeingPrepended))
                prependedString = to_string(prependedList, retained)
                return prependedString
        elif (type(thingBeingPrependedTo) == list):
            if (type(thingBeingPrepended) != list):
                prependedList = list(thingBeingPrependedTo.insert(0, thingBeingPrepended))
                return prependedList
            else:
                prependedList = list(thingBeingPrepended)
                for i in range (len(thingBeingPrependedTo)):    
                    prependedList.append(thingBeingPrependedTo[i])
                    i += 1
                return prependedList
        else:
            print("Warning from 'prepend()' in 'debugger_files.debugger_utils.py' on 'Line 93' :")
            print("'thingBeingPrependedTo' was not either type 'str' or 'list'")
            print("Was type:   '", type(thingBeingPrependedTo), "'")
            print("Completed prepend and returned using type 'list'")
            print("")                
            if (type(thingBeingPrepended) != list):
                prependedList = [thingBeingPrepended, thingBeingPrependedTo]
                return prependedList
            else:
                prependedList = list(thingBeingPrepended.append(thingBeingPrependedTo))
                return prependedList
    elif returnType == "inverse":
            
            
            
            prependedList = list(thingBeingPrependedTo.insert(0, thingBeingPrepended))
            return prependedList                
            
            
            prependedString = to_string([thingBeingPrepended, thingBeingPrependedTo], retained)
            return prependedString            




            
    elif (type(thingBeingPrependedTo) == str) and ((returnAsTypeOfThingBeingPrependedTo is True) or (type(thingBeingPrepended) == str)):
        if type(thingBeingPrepended) == str:
            prependedString = thingBeingPrepended + thingBeingPrependedTo
            return prependedString
        else:
            stringifiedThingBeingAppended = to_string(thingBeingPrepended, retained)
            prependedString = stringifiedThingBeingAppended + thingBeingPrependedTo
    elif type(thingBeingPrepended) == list:
        prependedList = list(thingBeingPrepended.append(thingBeingPrependedTo))
        return prependedList
    else:
        prependedList = list(thingBeingPrependedTo.insert(0, thingBeingPrepended))
        return prependedList

def left_align_text(givenText):
    formattedText = to_string(givenText)
    rightMargin = charLineLength - len(formattedText)
    charList = []
    charList.append(lineStart)
    charList.append(formattedText)
    text = multi_char(space, rightMargin, False, True, charList)
    return text

def center_text(givenText):
    formattedText = to_string(givenText)
    textLen = len(formattedText)
    totalMargins = charLineLength - textLen
    if (totalMargins % 2) != 0:
        leftMargin = (totalMargins + 1) // 2
        rightMargin = (totalMargins -1) // 2
        charList = multi_char(space, leftMargin, True, False, None, True)
        charList.append(formattedText)
        text = multi_char(space, rightMargin, False, True, charList)
        return text
    else:
        margin = totalMargins // 2
        charList = multi_char(space, margin, True, False, None, True)
        charList.append(formattedText)
        text = multi_char(space, margin, False, True, charList)
        return text
    
def standard_column(colOneText = None, colTwoText = None, colThreeText = None, colFourText = None):
    temp_colTextList = make_list_all_strings([colOneText, colTwoText, colThreeText, colFourText])
    
    colFormatting = [widthColOne - len(temp_colTextList[0]), widthColTwo - len(temp_colTextList[1]), widthColThree - len(temp_colTextList[2]), widthColFour - len(temp_colTextList[3]),]
    
    colTextList = []
    
    for i in range(4):
        if i == 0:      
            colTextList.append(to_string([lineStart, temp_colTextList[i], multi_char(space, colFormatting[i])]))
            i += 1
        elif (i > 0) and (i < 3):
            colTextList.append(to_string([columnLine, temp_colTextList[i], multi_char(space, colFormatting[i])]))
            i += 1
        elif i == 3:
            colTextList.append(to_string([columnLine, temp_colTextList[i], multi_char(space, colFormatting[i]), lineEnd]))
            i += 1
        else:
            print("Error: For Loop in debugger_files.debugger_utils.py on line 110")
    
    text = to_string(colTextList)
    return text

#def create_custom_chart(chartTitle, numofCol, colSizeList, colLabelList, colTextAlignmentList, ):
    
    
    