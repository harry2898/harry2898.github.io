#This file contains a format for Debugython

#Imports a class containing a variable for each ASCII printable character and useable control code (within ASCII 7 bit/ 128 code character set)
#Each variable is named the character name (sometimes abbreviated) and is equal to its respective ASCII decimal code 
#Such as: 'period = chr(46)' with char(34) equal to '.'
from debugython.ascii_table import *

#A class containing all of the format's settings
class format_config:
    def __init__(self):
        #Creates an oject named 'char' who contains the ASCII variables
        #For example: 'char.period would equal '.' and 'str(char.H + char.i + char.period) would equal 'Hi.'
        char = ascii_chars()

        self.topBorder = "="
        self.leftBorder = "||"
        self.rightBorder = "||"
        self.bottomBorder = "="

        self.useCustomCornerBorders = True
        self.topLeftCornerBorder = "|="
        self.topRightCornerBorder = "=|"
        self.bottomLeftCornerBorder = "|="
        self.bottomRightCornerBorder = "=|"

        self.topMargin = 1
        self.leftMargin = 2
        self.rightMargin = 2
        self.bottomMargin = 1

        self.columnSeparator = "|"
        self.rowSeparator = "-"

        self.autoPageWidth = True
        self.minPageWidth = None
        self.maxPageWidth = None

        self.tabSize = 4

        self.autoColumnWidth = True
        self.autoMakeColumnWidthsEqualSize = True
        self.minColumnWidth = None
        self.maxColumnWidth = None

        self.autoRowHeight = True
        self.minRowHeight = None
        self.maxRowHeight = None

        self.wrapText = True

        self.lineSeparatorOne = "-"
        self.lineSeparatorTwo = "+"
        self.lineSeparatorThree = "#"

        self.useCustomMarginsForLineSeparators = True
        self.customTopLineSeparatorMargin = 0
        self.customLeftLineSeparatorMargin = 5
        self.customRightLineSeparatorMargin = 5
        self.customBottomLineSeparatorMargin = 0

        self.topTextBoxBorder = "_"
        self.LeftTextBoxBorder = "|"
        self.RightTextBoxBorder = "|"
        self.BottomTextBoxBorder = "_"

        self.useCustomTextBoxCornerBorders = True
        self.topLeftTextBoxCornerBorder = [' _', '|_|']
        self.topRightTextBoxCornerBorder = ['_ ', '|_|']
        self.bottomLeftTextBoxCornerBorder = ['|_', '|_|']
        self.bottomRightTextBoxCornerBorder = ['_|', '|_|']

        self.useCustomExternalMarginsForTextBoxes = True
        self.customExternalTopTextBoxMargin = 0
        self.customExternalLeftTextBoxMargin = 5
        self.customExternalRightTextBoxMargin = 5
        self.customExternalBottomTextBoxMargin = 0

        self.useCustomInternalMarginsForTextBoxes = True
        self.customInternalTopTextBoxMargin = 1
        self.customInternalLeftTextBoxMargin = 2
        self.customInternalRightTextBoxMargin = 2
        self.customInternalBottomTextBoxMargin = 1

        self.bulletListCharacterFollowingBulletPoint = ")"
        self.bulletListBulletPointOne = "*"
        self.bulletListBulletPointTwo = "-"
        self.bulletListBulletPointThree = ">>"
        self.bulletListRepeatBulletPoints = True
        self.bulletListCustomRepeatingBulletPoint = None

        self.numListCharacterFollowingBulletPoint = ":"
        self.numListBulletPointTwo = "lowercase_letters"
        self.numListBulletPointThree = ">"
        self.useNumListCharacterFollowingBulletPointForNumBulletPoints = True
        self.useNumListCharacterFollowingBulletPointForLetterBulletPoints = True
        self.useNumListCharacterFollowingBulletPointForNonNumOrLetterBulletPoints = True
        self.numListRepeatAllBulletPoints = False
        self.numListRepeatBulletPointsTwoAndThree = True
        self.numListCustomRepeatingBulletPoint = None

        self.useTabSizeForListIndentSize = True
        self.customListIndentSize = None

        self.useCustomMarginsForLists = False
        self.customTopListsMargin = None
        self.customLeftListsMargin = None
        self.customRightListsMargin = None
        self.customBottomListsMargin = None

        #A list containing all of the format's settings
        self.allSettings = [self.topBorder, self.leftBorder, self.rightBorder, self.bottomBorder, self.useCustomCornerBorders, self.topLeftCornerBorder, self.topRightCornerBorder, 
                            self.bottomLeftCornerBorder, self.bottomRightCornerBorder, self.topMargin, self.leftMargin, self.rightMargin, self.bottomMargin, self.columnSeparator, self.rowSeparator, 
                            self.autoPageWidth, self.minPageWidth, self.maxPageWidth, self.tabSize, self.autoColumnWidth, self.autoMakeColumnWidthsEqualSize, self.minColumnWidth, self.maxColumnWidth, 
                            self.autoRowHeight, self.minRowHeight, self.maxRowHeight, self.wrapText, self.lineSeparatorOne, self.lineSeparatorTwo, self.lineSeparatorThree, 
                            self.useCustomMarginsForLineSeparators, self.customTopLineSeparatorMargin, self.customLeftLineSeparatorMargin, self.customRightLineSeparatorMargin, 
                            self.customBottomLineSeparatorMargin, self.topTextBoxBorder, self.LeftTextBoxBorder, self.RightTextBoxBorder, self.BottomTextBoxBorder, self.useCustomTextBoxCornerBorders, 
                            self.topLeftTextBoxCornerBorder, self.topRightTextBoxCornerBorder, self.bottomLeftTextBoxCornerBorder, self.bottomRightTextBoxCornerBorder, 
                            self.useCustomExternalMarginsForTextBoxes, self.customExternalTopTextBoxMargin, self.customExternalLeftTextBoxMargin, self.customExternalRightTextBoxMargin, 
                            self.customExternalBottomTextBoxMargin, self.useCustomInternalMarginsForTextBoxes, self.customInternalTopTextBoxMargin, self.customInternalLeftTextBoxMargin, 
                            self.customInternalRightTextBoxMargin, self.customInternalBottomTextBoxMargin, self.bulletListCharacterFollowingBulletPoint, self.bulletListBulletPointOne, 
                            self.bulletListBulletPointTwo, self.bulletListBulletPointThree, self.bulletListRepeatBulletPoints, self.bulletListCustomRepeatingBulletPoint, 
                            self.numListCharacterFollowingBulletPoint, self.numListBulletPointTwo, self.numListBulletPointThree, self.useNumListCharacterFollowingBulletPointForNumBulletPoints, 
                            self.useNumListCharacterFollowingBulletPointForLetterBulletPoints, self.useNumListCharacterFollowingBulletPointForNonNumOrLetterBulletPoints, self.numListRepeatAllBulletPoints, 
                            self.numListRepeatBulletPointsTwoAndThree, self.numListCustomRepeatingBulletPoint, self.useTabSizeForListIndentSize, self.customListIndentSize, self.useCustomMarginsForLists, 
                            self.customTopListsMargin, self.customLeftListsMargin, self.customRightListsMargin, self.customBottomListsMargin]

    #A function which returns the list containing all of the format's settings
    def get_all_settings(self):
        return self.allSettings

    #A function which prints the list containing all of the format's settings
    def print_all_settings(self):
        print(self.allSettings)