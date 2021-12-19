def error_change_win_bg_color(error, color, winColormode = None):
    if error == "rgb_value_out_of_bounds":
        print("Error: Could not change window's background color")
        print("At least one of the given RGB values was out of bounds (less than 0 or greater than 255)")
        print("Was given: color =", color)
        return False
    elif error == "unknown_error":
        print("Unknown Error: Could not change window's background color")
        print("Was given: color =", color, " --- len(color) =", len(color))    
    elif error == "rgb_value_list_invalid_length":
        print("Error: Could not change window's background color")
        print("The given color must have a lenth of 3")
        print("Was given: color =", color, " --- len(color) =", len(color))
        return False
    elif error == "str_color_invalid":
        print("Error: Could not change window's background color")
        print("The given color is not a valid color")
        print("Was given: color =", color)
        return False
    elif error == "given_color_invalid_type":
        if winColormode == "rgb":
            correctColorType = "list"
        else:
            correctColorType = "str"        
        print("Error: Could not change window's background color")
        print("The given color must must be type", correctColorType)
        print("Was given: color =", color, " --- type(color) =", type(color))
        return False
    else:
        print("Unknown Error: Could not determine change_win_bg_color error")
        print("Was given: error =", error, "  color =", color, "  winColormode =", winColormode)
        print("type(color) =", type(color))
        return False    