#====================================================================

#Default Launcher Config

#====================================================================

#    Table of Contents:

#    1a: Imports
#    1b: Misc

#    2a: Window Constants
#    2b: Window Settings

#    3a: UI Elements Constants
#    3b: UI Elements Settings

#====================================================================

#  1a: Imports:

#Imports a large number of defined color constant values
from pysics_utils.color_constants import *

#--------------------------------------------------------------------

#  1b: Misc:

#Description of Misc Config
#Misc Config

#====================================================================

#  2a: Window Constants:

#Window Dimensions
WIN_WIDTH, WIN_HEIGHT = 640, 480
WIN_DIM = [WIN_WIDTH, WIN_HEIGHT]

#FPS Cap (max FPS)
FPS_CAP = 60

#--------------------------------------------------------------------

#  2b: Window Settings:

#Text that will appear on the title bar at the top of the window
title_caption = "Pysics Simulator Launcher"

#Default Background Color
winBgColor = WHITE

#====================================================================

#  3a: UI Elements Constants:

#UI Elements Scalar Value
UI_SCALE_FACTOR = 5


#Extra Small Square Side Length and Circle Diameter
XS_SQ_SIDE_LEN, XS_CIR_DIAMETER = 25

#Small Square Side Length (dimensions)
SM_SQ_SIDE_LEN, SM_CIR_DIAMETER = 50

#Medium Square Side Length (dimensions)
MED_SQ_SIDE_LEN, MED_CIR_DIAMETER = 75

#Large Square Side Length (dimensions)
LG_SQ_SIDE_LEN, LG_CIR_DIAMETER = 100

#Extra Large Square Side Length (dimensions)
XL_SQ_SIDE_LEN, XL_CIR_DIAMETER = 125

#2XL Square Side Length (dimensions)
XXL_SQ_SIDE_LEN, XXL_CIR_DIAMETER = 150

#3XL Square Side Length (dimensions)
XXXL_SQ_SIDE_LEN, XXXL_CIR_DIAMETER = 175

#4XL Square Side Length (dimensions)
XXXXL_SQ_SIDE_LEN, XXXXL_CIR_DIAMETER = 200

#  3b: UI Elements Calculated Values (essential constants):

XS = 