#====================================================================

#Default Launcher Config

#====================================================================

#    Table of Contents:

#    1: Imports

#    2: Window

#    3: UI Elements

#====================================================================

#  1: Imports:

#Imports a large number of defined color constant values
from pysics_utils.color_constants import *

#====================================================================

#  2: Window:

#Window Dimensions
WIN_WIDTH, WIN_HEIGHT = 640, 480
WIN_DIM = [WIN_WIDTH, WIN_HEIGHT]

#FPS Cap (max FPS)
WIN_FPS_CAP = 60

#Text that will appear on the title bar at the top of the window
win_title_caption = "Pysics Simulator Launcher"

#Default Background Color
win_bg_color = WHITE

#====================================================================

#  3: UI Elements Constants:

#UI Elements Scale Factor
UI_SCALE_FACTOR = 5

btn_unpressed_color = LIGHTBLUE1
btn_hovered_color = LIGHTSKYBLUE
btn_pressed_color = DEEPSKYBLUE1