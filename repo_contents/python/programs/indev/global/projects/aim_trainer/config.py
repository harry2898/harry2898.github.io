        #Aim Trainer Config
        
#=======================================
        #Config Imports:

#---------------------------------------
#Large number of colors --- Each color is equal to a list containing its RGB value --> COLOR = [R, G, B] --- Ex: BLUE = [0, 0, 255]:
from color_constants_rgb_lists import *

#=======================================
        #Developer Config Settings:
        
#---------------------------------------
#Use color_constants_rgb_lists.py instead of turtle's built color names:
DEVELOPER_USE_COLOR_CONSTANTS = True

#=======================================
        #Window Config Settings:

#---------------------------------------
#Window Dimensions:
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

#---------------------------------------
#Window Background Color:
WINDOW_BG_COLOR = "white"

#---------------------------------------
#Window Title:
WINDOW_TITLE = "Aim Trainer"

#=======================================
        #Targets Config Settings:

#---------------------------------------
#Target Color:
TARGET_COLOR = "red"

#---------------------------------------
#Target Shape:
TARGET_SHAPE = "circle"

#---------------------------------------
#Target's size is fixed --- (if equal to False: the target's size will be variable):
TARGET_SIZE_IS_FIXED = True

#---------------------------------------
#Target Size:

#If TARGET_SHAPE = "circle":
        #If TARGET_SIZE_IS_FIXED = True:
                #Target Diameter:
TARGET_DIAMETER = 100

#-------------------

        #If TARGET_SIZE_IS_FIXED = False:
                #Target Diameter Range:
TARGET_DIAMETER_MIN, TARGET_DIAMETER_MAX = 50, 100

#-------------------

#If TARGET_SHAPE = "rectangle":
        #If TARGET_SIZE_IS_FIXED = True:
                #Target Dimensions:
TARGET_WIDTH, TARGET_HEIGHT = 100, 100

#-------------------

        #If TARGET_SIZE_IS_FIXED = False:
                #Target Dimensions Range:
TARGET_WIDTH_MIN, TARGET_WIDTH_MAX = 50, 100
TARGET_HEIGHT_MIN, TARGET_HEIGHT_MAX = 50, 100

#---------------------------------------
#Number of target(s) active at a time --- (must be equal to or less than 5):
TARGET_NUMBER_ACTIVE_AT_ONCE = 1

#---------------------------------------
#Amount of time before a target disappears --- (if equal to 0: the target will not disappear until clicked):
TARGET_LIFESPAN = 0

#---------------------------------------
#Target's speed is fixed --- (if equal to False: the target's speed will be variable):
TARGET_MOVEMENT_SPEED_IS_FIXED = True

#---------------------------------------
#If TARGET_MOVEMENT_SPEED_IS_FIXED = True:
        #Speed that a target moves --- (if equal to 0: the target will not move --- must be equal to or less than ???):
TARGET_MOVEMENT_SPEED = 0

#---------------------------------------
#If TARGET_MOVEMENT_SPEED_IS_FIXED = False:
        #Speed range that a target moves --- (must be greater than 0 --- must be equal to or less than ???):
TARGET_MOVEMENT_SPEED_MIN, TARGET_MOVEMENT_SPEED_MAX = 100, 200

#=======================================