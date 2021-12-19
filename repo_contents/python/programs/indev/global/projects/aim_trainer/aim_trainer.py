import turtle
import time
import random

from config import *
from utils import *
from error_utils import *

class aim_trainer:
    def __init__(self):
        WINDOW = window()
        WIN = WINDOW.win
        
        TGT = target()
        #num of targets

    

class window:    
    def __init__(self):
        self.win = turtle.Screen()
        self._create_win_config_variables()
        self._set_win_colormode()
        self._set_win_config()
    
    def _create_win_config_variables(self):
        self.win_width, self.win_height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.win_dimensions = [self.win_width, self.win_height]
        
        self.win_bg_color = WINDOW_BG_COLOR
        
        self.win_title = WINDOW_TITLE
    
    def _set_win_config(self):
        self.win.setup(self.win_width, self.win_height)
        self.win.bgcolor(self.win_bg_color)
        self.win.title(self.win_title)
    
    def _set_win_colormode(self):
        if DEVELOPER_USE_COLOR_CONSTANTS is True:
            self.win.colormode(255)
            self.win_colormode = "rgb"    
    
    def _get_win_colormode(self):
        if DEVELOPER_USE_COLOR_CONSTANTS is True:
            return self.win_colormode
    
        else:
            self.win_colormode = "turtle_default"
    
    def get_win_width(self):
        return self.win_width
    
    def get_win_height(self):
        return self.win_height
    
    def get_win_dimensions(self):
        return self.win_dimensions
    
    def change_win_bg_color(self, color):
        if (type(color) == list) and (self.win_colormode == "rgb"):
            if len(color) == 3:
                for i in range(color):
                    if (color[i] < 0) or (color[i] > 255):
                        return error_change_win_bg_color("rgb_value_out_of_bounds", color, winColormode = None)
                try:
                    self.win.bgcolor(color)
                except turtle.TurtleGraphicsError:
                    return error_change_win_bg_color("unknown_error", color, winColormode = None)
                self.win_bg_color = color
            else:
                return error_change_win_bg_color("rgb_value_list_invalid_length", color, winColormode = None)
        elif type(color) == str:
            try:
                self.win.bgcolor(color)
            except turtle.TurtleGraphicsError:
                return error_change_win_bg_color("str_color_invalid", color, winColormode = None)
            self.win_bg_color = color
        else:
            try:
                self.win.bgcolor(color)
            except turtle.TurtleGraphicsError:
                return error_change_win_bg_color("given_color_invalid_type", color, self.win_colormode)
            print("Warning: Successfully changed the window's background color, but the given color was originally deemed invalid")
            print("Was given: color =", color)
            self.win_bg_color = color
    
    def get_win_bg_color(self):
        return self.win_bg_color



class target:
    def __init__(self):
        self.tgt = turtle.Turtle()
        self._create_tgt_config_variables()
    
    def _create_tgt_config_variables(self):
        self.tgt_color = TARGET_COLOR
        
        self.tgt_shape = TARGET_SHAPE
        
        self._determine_tgt_size()
        
        self.tgt_lifespan = TARGET_LIFESPAN
        
        self._determine_tgt_movespeed()
        
    def _set_win_config(self):
        self.tgt.color(self.tgt_color)
        
        self.tgt.shape(self.tgt_shape)
        
        self._set_tgt_size()
        
    
    def _determine_tgt_size(self):
        self.tgt_size_is_fixed = TARGET_SIZE_IS_FIXED
        if (self.tgt_shape == "circle") and (self.tgt_size_is_fixed is True):
            self.tgt_diameter = TARGET_DIAMETER
            self.tgt_radius = self.tgt_diameter / 2
        elif (self.tgt_shape == "circle") and (self.tgt_size_is_fixed is False):
            self.tgt_diameter_min, self.tgt_diameter_max = TARGET_DIAMETER_MIN, TARGET_DIAMETER_MAX
            self.tgt_diameter_range = [self.tgt_diameter_min, self.tgt_diameter_max]
            
            self.tgt_radius_min, self.tgt_radius_max = self.tgt_diameter_min / 2, self.tgt_diameter_max / 2
            self.tgt_radius_range = [self.tgt_radius_min, self.tgt_radius_max]
        elif (self.tgt_shape == "rectangle") and (self.tgt_size_is_fixed is True):
            self.tgt_width, self.tgt_height = TARGET_WIDTH, TARGET_HEIGHT
            self.tgt_dimensions = [self.tgt_width, self.tgt_height]
        elif (self.tgt_shape == "rectangle") and (self.tgt_size_is_fixed is False):
            self.tgt_width_min, self.tgt_width_max = TARGET_WIDTH, TARGET_HEIGHT
            self.tgt_height_min, self.tgt_height_max = TARGET_HEIGHT_MIN, TARGET_HEIGHT_MAX
            
            self.tgt_width_range = [self.tgt_width_min, self.tgt_width_max]
            self.tgt_height_range = [self.tgt_height_min, self.tgt_height_max]
            
            self.tgt_axis_mins = [self.tgt_width_min, self.tgt_height_min]
            self.tgt_axis_maxes = [self.tgt_width_max, self.tgt_height_max]
            
            self.tgt_dimensions_range_axes = [self.tgt_width_range, self.tgt_height_range]    #[0][0] = TARGET_WIDTH_MIN, [0][1] = TARGET_WIDTH_MAX, [1][0] = TARGET_HEIGHT_MIN, [1][1] = TARGET_HEIGHT_MAX
            self.tgt_dimensions_range_bounds = [self.tgt_axis_mins, self.tgt_axis_maxes]      #[0][0] = TARGET_WIDTH_MIN, [0][1] = TARGET_HEIGHT_MIN, [1][0] = TARGET_WIDTH_MAX, [1][1] = TARGET_HEIGHT_MAX
    
    def _set_tgt_size(self):
        if (self.tgt_shape == "circle") and (self.tgt_size_is_fixed is True):
            self.tgt.width = self.tgt_diameter
        elif (self.tgt_shape == "circle") and (self.tgt_size_is_fixed is False):
            self.tgt.width = (self.tgt_radius_min + self.tgt_radius_max) / 2
        elif (self.tgt_shape == "rectangle") and (self.tgt_size_is_fixed is True):
            self.tgt.shapesize()
            
            

    def _determine_tgt_movespeed(self):
        self.tgt_movespeed_is_fixed = TARGET_MOVEMENT_SPEED_IS_FIXED
        if self.tgt_movespeed_is_fixed is True:
            self.tgt_movespeed = TARGET_MOVEMENT_SPEED
        else:
            self.tgt_movespeed_min, self.tgt_movespeed_max = TARGET_MOVEMENT_SPEED_MIN, TARGET_MOVEMENT_SPEED_MAX
            self.tgt_movespeed_range = [self.tgt_movespeed_min, self.tgt_movespeed_max]


'''
color
shape
fixed size
size
number at a time
lifespan
fixed speed
speed
'''