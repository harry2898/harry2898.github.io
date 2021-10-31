from physics_debug_config import *

def blank_line():
    text = multi_char(space, charLineLength, True, True)
    return text

def dash_line():
    text = multi_char(dash, charLineLength, True, True)
    return text

def double_dash_line():
    text = multi_char(doubleDash, charLineLength, True, True)
    return text

def multi_tab(numTabs, beginning = False, end = False, givenList = None, returnList = False):
    if givenList is None:
        charList = []
    else:
        charList = list(givenList)
    
    if beginning is True:
        charList.append(lineStart)
    for i in range(numTabs):
        charList.append(tab)
    if end is True:
        charList.append(lineEnd)
    if returnList is True:
        return charList
    else:
        text = ""
        text = join_text(charList)
        return text    
    
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
        text = join_text(charList)
        return text    

def join_text(givenList):
    givenList = list(map(str, givenList))
    joinedText = "".join(givenList)
    return joinedText

def convert_to_string(givenText, convertList = False):
    if convertList is True:
        convertedList = list(map(str, givenText))
        return convertedList
    else: 
        convertedText = str(givenText)
        return convertedText

def left_align_text(givenText):
    formattedText = join_text(givenText)
    rightMargin = charLineLength - len(formattedText)
    charList = []
    charList.append(lineStart)
    charList.append(formattedText)
    text = multi_char(space, rightMargin, False, True, charList)
    return text

def center_text(givenText):
    formattedText = join_text(givenText)
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
    temp_colTextList = convert_to_string([colOneText, colTwoText, colThreeText, colFourText], True)
    
    colFormatting = [widthColOne - len(temp_colTextList[0]), widthColTwo - len(temp_colTextList[1]), widthColThree - len(temp_colTextList[2]), widthColFour - len(temp_colTextList[3]),]
    
    colTextList = []
    
    for i in range(4):
        print(i)
        if i == 0:      
            colTextList.append(join_text([lineStart, temp_colTextList[i], multi_char(space, colFormatting[i])]))
            i += 1
        elif (i > 0) and (i < 3):
            colTextList.append(join_text([columnLine, temp_colTextList[i], multi_char(space, colFormatting[i])]))
            i += 1
        elif i == 3:
            colTextList.append(join_text([columnLine, temp_colTextList[i], multi_char(space, colFormatting[i]), lineEnd]))
            i += 1
        else:
            print("Error: For Loop in physics_debug_utils.py on line 110")
    
    text = join_text(colTextList)
    return text

#def create_custom_chart(chartTitle, numofCol, colSizeList, colLabelList, colTextAlignmentList, ):
    
    
    