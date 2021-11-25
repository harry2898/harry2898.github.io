import os
import importlib

from debugython.ascii_table import *

class set_log_format:
    
    class default_format:
        def __init__(self):
            self.name = "default"
            from debugython.log_formats.default import format_config
            self.config = format_config()
            self.allSettings = self.config.get_all_settings()
            
        def get_all_settings(self):
            return self.allSettings    
            
        def print_all_settings(self):
            print(self.allSettings)
        
        
    class custom_format:
        def __init__(self, nameOfCustomFormat):
            if type(nameOfCustomFormat) != str:
                print("Error: Invalid variable 'type' given for 'nameOfCustomFormat'")
                print("Must be 'type' 'str', but was given:", nameOfCustomFormat, "whose 'type' is:", type(nameOfCustomFormat))
            else:
                self.name = nameOfCustomFormat
            self.config = self._import_format_class(self.name)
            self.allSettings = self.config.get_all_settings()
            
        def get_all_settings(self):
            return self.allSettings    
            
        def print_all_settings(self):
            print(self.allSettings)
            
        def _import_format_class(self, nameOfFormat):
            if self._import_exists(nameOfFormat) is True:
                formatFilePath = "debugython.log_formats." + nameOfFormat
                formatFile = importlib.import_module(formatFilePath)
                formatClass = formatFile.format_config()
                return formatClass
            else:
                print("Error: could not import format class as the format file does not exist")
                print("Ensure that the format file is in the 'log_formats' folder and the format name matches its file name (do not include the .py)")
                print("Was given --- 'nameOfFormat':", nameOfFormat)
                return False     
        
        def _import_exists(self, nameOfFormat):
            directoryPath = os.path.dirname(os.path.realpath("__file__"))
            relativeFormatFilePath = "../debugython/log_formats/" + nameOfFormat + ".py"
            formatFilePath = os.path.join(directoryPath, relativeFormatFilePath)
            pathExists = os.path.exists(formatFilePath)
            print("Check to see if the path of the to be imported format file exists resulted in:", pathExists)
            return pathExists        
    
    class get_current_format:
        def __init__(self):
            return
               
    
        
class custom_log_format:
    
    class create:
        def __init__(self, nameOfNewCustomFormat, baseTypeOfNewCustomFormat, nameOfCustomFormatToUseAsBase = None, saveAfterBaseIsCreated = False):
            if type(nameOfNewCustomFormat) != str:
                print("Error: Invalid variable 'type' given for 'nameOfNewCustomFormat'")
                print("Must be 'type' 'str', but was given:", nameOfNewCustomFormat, "whose 'type' is:", type(nameOfNewCustomFormat))
            else:
                self.name = nameOfNewCustomFormat
            if type(baseTypeOfNewCustomFormat) != str:
                print("Error: Invalid variable 'type' given for 'baseTypeOfNewCustomFormat'")
                print("Must be 'type' 'str', but was given:", baseTypeOfNewCustomFormat, "whose 'type' is:", type(baseTypeOfNewCustomFormat))
            if nameOfCustomFormatToUseAsBase is not None and type(nameOfNewCustomFormat) != str:
                print("Error: Invalid variable 'type' given for 'nameOfCustomFormatToUseAsBase'")
                print("Must be 'type' 'str', but was given:", nameOfCustomFormatToUseAsBase, "whose 'type' is:", type(nameOfCustomFormatToUseAsBase))
            if type(saveAfterBaseIsCreated) != bool:
                print("Error: Invalid variable 'type' given for 'saveAfterBaseIsCreated'")
                print("Must be 'type' 'bool', but was given:", saveAfterBaseIsCreated, "whose 'type' is:", type(saveAfterBaseIsCreated))                
            if nameOfCustomFormatToUseAsBase is None:
                self._set_paths()
            else:
                self._set_paths()
                self._set_custom_base_path()            
            if baseTypeOfNewCustomFormat.lower() == "default":
                self.baseType = baseTypeOfNewCustomFormat
                self.allSettings = self._import_format_class(self.baseType).get_all_settings()
                self.set_all_settings(self.allSettings)
            elif baseTypeOfNewCustomFormat.lower() == "blank":
                self.baseType = baseTypeOfNewCustomFormat
                self.allSettings = self._import_format_class(self.baseType).get_all_settings()
                numOfSettings = len(self.allSettings)
                for i in range(len(self.allSettings)):
                    self.allSettings[i] = None
                if ((numOfSettings != len(self.allSettings)) or (any(self.allSettings))):
                    print("Error: 'self.allSettings' created for 'blank' base' did not have the expected length or was not empty")
                    print("List Created:", self.allSettings)
                    print("Result of Length Test:", (numOfSettings != len(self.allSettings)))
                    print("Result of Is Empty Test:", (any(self.allSettings)))
                else:
                    self.set_all_settings(self.allSettings)
            elif baseTypeOfNewCustomFormat.lower() == "custom":
                self.baseType = baseTypeOfNewCustomFormat
                self.allSettings = self._import_format_class(nameOfCustomFormatToUseAsBase).get_all_settings()
                self.nameOfCustomBase = nameOfCustomFormatToUseAsBase
                #if self.allSettings is False:
                    #print("Error: Could not find the given 'nameOfCustomFormatToUseAsBase':", nameOfCustomFormatToUseAsBase)
                #else:                   
                self.set_all_settings(self.allSettings)
            else:
                print("Unknown Error: create_custom_format.create() failed to create custom format. Variables given:")
                print("'nameOfNewCustomFormat':", nameOfNewCustomFormat)
                print("'baseTypeOfNewCustomFormat':", baseTypeOfNewCustomFormat)
                print("'nameOfCustomFormatToUseAsBase':", nameOfCustomFormatToUseAsBase)
                return False
            if saveAfterBaseIsCreated is False:
                self.packageExists = False
                print("Successfully created 'custom_log_format' with 'self.name':", self.name, "and 'self.baseType':", self.baseType)
            elif saveAfterBaseIsCreated is True:
                print("Successfully created 'custom_log_format' with 'self.name':", self.name, "and 'self.baseType':", self.baseType)
                self.save
            else:
                print("Unknown Error: create_custom_format.create() --- Created custom format but failed saveAfterBaseIsCreated check. Variables given:")
                print("'nameOfNewCustomFormat':", nameOfNewCustomFormat)
                print("'baseTypeOfNewCustomFormat':", baseTypeOfNewCustomFormat)
                print("'nameOfCustomFormatToUseAsBase':", nameOfCustomFormatToUseAsBase)
                print("'saveAfterBaseIsCreated' :", saveAfterBaseIsCreated)
                return False
        
        def set_all_settings(self, listOfAllSettings):
            self.topBorder = listOfAllSettings[0]
            self.leftBorder = listOfAllSettings[1]
            self.rightBorder = listOfAllSettings[2]
            self.bottomBorder = listOfAllSettings[3]
            
            self.useCustomCornerBorders = listOfAllSettings[4]
            self.topLeftCornerBorder = listOfAllSettings[5]
            self.topRightCornerBorder = listOfAllSettings[6]
            self.bottomLeftCornerBorder = listOfAllSettings[7]
            self.bottomRightCornerBorder = listOfAllSettings[8]
            
            self.topMargin = listOfAllSettings[9]
            self.leftMargin = listOfAllSettings[10]
            self.rightMargin = listOfAllSettings[11]
            self.bottomMargin = listOfAllSettings[12]
            
            self.columnSeparator = listOfAllSettings[13]
            self.rowSeparator = listOfAllSettings[14]
            
            self.autoPageWidth = listOfAllSettings[15]
            self.minPageWidth = listOfAllSettings[16]
            self.maxPageWidth = listOfAllSettings[17]
            
            self.tabSize = listOfAllSettings[18]
            
            self.autoColumnWidth = listOfAllSettings[19]
            self.autoMakeColumnWidthsEqualSize = listOfAllSettings[20]
            self.minColumnWidth = listOfAllSettings[21]
            self.maxColumnWidth = listOfAllSettings[22]
            
            self.autoRowHeight = listOfAllSettings[23]
            self.minRowHeight = listOfAllSettings[24]
            self.maxRowHeight = listOfAllSettings[25]
            
            self.wrapText = listOfAllSettings[26]
            
            self.lineSeparatorOne = listOfAllSettings[27]
            self.lineSeparatorTwo = listOfAllSettings[28]
            self.lineSeparatorThree = listOfAllSettings[29]
            
            self.useCustomMarginsForLineSeparators = listOfAllSettings[30]
            self.customTopLineSeparatorMargin = listOfAllSettings[31]
            self.customLeftLineSeparatorMargin = listOfAllSettings[32]
            self.customRightLineSeparatorMargin = listOfAllSettings[33]
            self.customBottomLineSeparatorMargin = listOfAllSettings[34]
            
            self.topTextBoxBorder = listOfAllSettings[35]
            self.LeftTextBoxBorder = listOfAllSettings[36]
            self.RightTextBoxBorder = listOfAllSettings[37]
            self.BottomTextBoxBorder = listOfAllSettings[38]
            
            self.useCustomTextBoxCornerBorders = listOfAllSettings[39]
            self.topLeftTextBoxCornerBorder = listOfAllSettings[40]
            self.topRightTextBoxCornerBorder = listOfAllSettings[41]
            self.bottomLeftTextBoxCornerBorder = listOfAllSettings[42]
            self.bottomRightTextBoxCornerBorder = listOfAllSettings[43]     
            
            self.useCustomExternalMarginsForTextBoxes = listOfAllSettings[44]
            self.customExternalTopTextBoxMargin = listOfAllSettings[45]
            self.customExternalLeftTextBoxMargin = listOfAllSettings[46]
            self.customExternalRightTextBoxMargin = listOfAllSettings[47]
            self.customExternalBottomTextBoxMargin = listOfAllSettings[48]
            
            self.useCustomInternalMarginsForTextBoxes = listOfAllSettings[49]
            self.customInternalTopTextBoxMargin = listOfAllSettings[50]
            self.customInternalLeftTextBoxMargin = listOfAllSettings[51]
            self.customInternalRightTextBoxMargin = listOfAllSettings[52]
            self.customInternalBottomTextBoxMargin = listOfAllSettings[53]
            
            self.bulletListCharacterFollowingBulletPoint = listOfAllSettings[54]
            self.bulletListBulletPointOne = listOfAllSettings[55]
            self.bulletListBulletPointTwo = listOfAllSettings[56]
            self.bulletListBulletPointThree = listOfAllSettings[57]
            self.bulletListRepeatBulletPoints = listOfAllSettings[58]
            self.bulletListCustomRepeatingBulletPoint = listOfAllSettings[59]
            
            self.numListCharacterFollowingBulletPoint = listOfAllSettings[60]
            self.numListBulletPointTwo = listOfAllSettings[61]
            self.numListBulletPointThree = listOfAllSettings[62]
            self.useNumListCharacterFollowingBulletPointForNumBulletPoints = listOfAllSettings[63]
            self.useNumListCharacterFollowingBulletPointForLetterBulletPoints = listOfAllSettings[64]
            self.useNumListCharacterFollowingBulletPointForNonNumOrLetterBulletPoints = listOfAllSettings[65]
            self.numListRepeatAllBulletPoints = listOfAllSettings[66]
            self.numListRepeatBulletPointsTwoAndThree = listOfAllSettings[67]
            self.numListCustomRepeatingBulletPoint = listOfAllSettings[68]
            
            self.useTabSizeForListIndentSize = listOfAllSettings[69]
            self.customListIndentSize = listOfAllSettings[70]
            
            self.useCustomMarginsForLists = listOfAllSettings[71]
            self.customTopListsMargin = listOfAllSettings[72]
            self.customLeftListsMargin = listOfAllSettings[73]
            self.customRightListsMargin = listOfAllSettings[74]
            self.customBottomListsMargin = listOfAllSettings[75]
            
            self.allSettings = list([self.topBorder, self.leftBorder, self.rightBorder, self.bottomBorder, self.useCustomCornerBorders, self.topLeftCornerBorder, self.topRightCornerBorder, 
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
                                self.useNumListCharacterFollowingBulletPointForLetterBulletPoints, self.useNumListCharacterFollowingBulletPointForNonNumOrLetterBulletPoints, 
                                self.numListRepeatAllBulletPoints, self.numListRepeatBulletPointsTwoAndThree, self.numListCustomRepeatingBulletPoint, self.useTabSizeForListIndentSize, 
                                self.customListIndentSize, self.useCustomMarginsForLists, self.customTopListsMargin, self.customLeftListsMargin, self.customRightListsMargin, self.customBottomListsMargin])
            
            if self.allSettings == listOfAllSettings:
                print("Successfully set all settings")
            else:
                print("Error: 'set_all_settings(self, listOfAllSettings)' failed to properly set all settings")
                print("Was given 'listOfAllSettings':", listOfAllSettings)
                print("Created 'self.allSettings':", self.allSettings)
        
        def get_all_settings(self):
            return self.allSettings        
        
        def print_all_settings(self):
            print(self.allSettings)                    
        
        def package_format(self):
            if self.packageExists is True:
                self.package.clear()
            else:
                self.package = []
                self.packageExists = True
            with open(self._defaultFormatFilePath,   "r") as formatFileFormatting:
                lines = formatFileFormatting.readlines()
                count = 0
                for line in lines:
                    #Checks if line's first word is self
                    if line.lstrip().split(".", 1)[0] != "self":
                        self.package.append(line)
                    #Checks if there are more than one periods in the line
                    elif len(line.split(".")) > 2:
                        self.package.append(line)
                    else:
                        if type(self.allSettings[count]) == str:
                            self.package.append(str(line.split("=", 1)[0] + "= " + chr(34) + str(self.allSettings[count]) + chr(34) + "\n"))
                            count += 1
                        else:
                            self.package.append(str(line.split("=", 1)[0] + "= " + str(self.allSettings[count]) + "\n"))
                            count += 1
        
        def check_if_package_exists(self, printResult = True):
            if printResult is True:
                print("'check_if_package_exists' result:", self.packageExists)
                return self.packageExists
            else:
                return self.packageExists
        
        def get_package(self):
            if self.packageExists is True:
                return self.package
            else:
                print("Error: 'self.package' does not exist/ has not been created yet.")
                return False
        
        def print_package(self):
            if self.packageExists is True:
                print(self.package)
            else:
                print("Error: 'self.package' does not exist/ has not been created yet.")
                return False
        
        def save(self):
            self.package_format()
            with open(self._saveFilePath, "w") as formatFile:
                for line in self.package:
                    formatFile.write(line)
            self._check_if_saved_successfully()
            
            
        
        def save_as(self, newNameOfNewCustomFormat):
            self.name = newNameOfNewCustomFormat
            self._set_paths()
            self.package_format()
            with open(self._saveFilePath, "w") as formatFile:
                for line in self.package:
                    formatFile.write(line)
            self._check_if_saved_successfully()            
            
            
        def _check_if_saved_successfully(self):
            formatClass = self._import_format_class(self.name)
            allSettingsInSave = formatClass.get_all_settings()
            if allSettingsInSave == self.allSettings:
                print("Saved Successfully!")
                return True
            else:
                print("Save Failed!")
                print("Saved format did not have expected format settings")
                print("Saved settings should be    :", self.allSettings)
                print("Saved settings are currently:", allSettingsInSave)
                return False        
        
        def _set_paths(self):
            self._directoryPath = os.path.dirname(os.path.realpath("__file__"))
            #print("Directory Path set as:", self._directoryPath)
            
            relativeSaveFilePath = "../debugython/log_formats/" + self.name + ".py"
            self._saveFilePath = os.path.join(self._directoryPath, relativeSaveFilePath)
            #print("Save File Path set as:", self._saveFilePath)
            
            relativeDefaultFormatFilePath = "../debugython/log_formats/default.py"
            self._defaultFormatFilePath = os.path.join(self._directoryPath, relativeDefaultFormatFilePath)
            #print("Default Format File Path set as:", self._defaultFormatFilePath)
                
        def _set_custom_base_path(self):
            relativeCustomBaseFilePath = "../debugython/log_formats/" + self.nameOfCustomBase + ".py"
            self._customBaseFilePath = os.path.join(self._directoryPath, relativeCustomBaseFilePath)
            #print("Custom Base File Path set as:", self._saveFilePath)            
        
        def _import_format_class(self, nameOfFormat):
            if self._import_exists(nameOfFormat) is True:
                formatFilePath = "debugython.log_formats." + nameOfFormat
                formatFile = importlib.import_module(formatFilePath)
                formatClass = formatFile.format_config()
                return formatClass
            else:
                print("Error: could not import format class as the format file does not exist")
                print("Ensure that the format file is in the 'log_formats' folder and the format name matches its file name (do not include the .py)")
                print("Was given --- 'nameOfFormat':", nameOfFormat)
                return False
        
        def _import_exists(self, nameOfFormat):
            relativeFormatFilePath = "../debugython/log_formats/" + nameOfFormat + ".py"
            formatFilePath = os.path.join(self._directoryPath, relativeFormatFilePath)
            pathExists = os.path.exists(formatFilePath)
            print("Check to see if the path of the to be imported format file exists resulted in:", pathExists)
            return pathExists
        
    class modify:
        def __init__(self, nameOfExistingCustomPackage):
            return
    
    
    class save_custom_format:
        def __init__ (self, packageOfCustomFormat):
            return
        
        
        
    class save_custom_format_as:
        def __init__ (self, packageOfCustomFormat, newNameOfCustomPackage):
            return
    
    
    class delete_custom_format:
        def __init__(self, nameOfCustomFormatToDelete, areYouSure = "false", haveYouDoubleCheckedEverything = False, youUnderstandThisIsIrreversible = False):
            quadCheck = input("To permanently delete the given custom format named:", nameOfCustomFormatToDelete, "type 'DELETE' without quotes and press 'enter'.")
            if ((areYouSure == "true") and (haveYouDoubleCheckedEverything is True) and (youUnderstandThisIsIrreversible is True) and (quadCheck == "DELETE")):
                print("Deleting the custom format named:", nameOfCustomFormatToDelete)
                #TODO
            else:
                print("Error: At least delete check is wrong. Did not delete the custom format named:", nameOfCustomFormatToDelete)
                print("Given 'areYouSure':", areYouSure)
                print("Given 'haveYouDoubleCheckedEverything':", haveYouDoubleCheckedEverything)
                print("Given 'youUnderstandThisIsIrreversible':", youUnderstandThisIsIrreversible)
                print("Given terminal input:", quadCheck)
                return False

        
logFormat = set_log_format()
logFormat.default_format()