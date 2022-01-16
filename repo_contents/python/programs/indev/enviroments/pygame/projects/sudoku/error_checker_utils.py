def is_valid_num(givenValue, debugMode = False, debuggerTool = None):
    if is_inbounds(givenValue, debugMode, debuggerTool) is True:
        return True
    else:
        if _do_debug is True:
            debuggerTool.set_error_info("invalid_num_error", givenValue, errorCheckerFunctionNameToAddToPath = "is_valid_num(givenValue)")
            return False
        else:
            return False

def are_valid_nums(givenListOfValues, debugMode = False, debuggerTool = None):
    if are_inbounds(givenListOfValues, debugMode, debuggerTool) is True:
        return True
    else:
        if _do_debug is True:
            debuggerTool.set_error_info("invalid_num_error", givenListOfValues, errorCheckerFunctionNameToAddToPath = "are_valid_nums(givenListOfValues)")
            return False
        else:
            return False

def is_int(givenValue, debugMode = False, debuggerTool = None):
    if type(givenValue) == int:
        return True
    else:
        if _do_debug is True:
            debuggerTool.set_error_info("type_error", givenValue, errorCheckerFunctionNameToAddToPath = "is_int(givenValue)")
            return False
        else:
            return False

def are_ints(givenListOfValues, debugMode = False, debuggerTool = None):
    if is_list(givenListOfValues, debugMode, debuggerTool) is True:
        for i in givenListOfValues:
            if is_int(i, debugMode, debuggerTool) is not True:
                if _do_debug is True:
                    debuggerTool.set_error_info("type_error", givenListOfValues, errorCheckerFunctionNameToAddToPath = "are_ints(givenListOfValues)")
                    return False
                else:
                    return False
        return True
    else:
        if _do_debug is True:
            debuggerTool.set_error_info("type_error", givenListOfValues, errorCheckerFunctionNameToAddToPath = "are_ints(givenListOfValues)")
            return False
        else:
            return False

def is_list(given, debugMode = False, debuggerTool = None):
    if type(given) == list:
        return True
    else:
        if _do_debug is True:
            debuggerTool.set_error_info("type_error", given, errorCheckerFunctionNameToAddToPath = "is_list(given)")
            return False
        else:
            return False

def is_inbounds(givenValue, debugMode = False, debuggerTool = None):
    if is_int(givenValue, debugMode, debuggerTool) is True:
        if (givenValue > 0) and (givenValue < 10):
            return True
        else:
            if _do_debug is True:
                debuggerTool.set_error_info("out_of_bounds_error", givenValue, errorCheckerFunctionNameToAddToPath = "is_inbounds(givenValue)")
                return False
            else:
                return False
    else:
        if _do_debug is True:
            debuggerTool.set_error_info("out_of_bounds_error", givenValue, errorCheckerFunctionNameToAddToPath = "is_inbounds(givenValue)")
            return False
        else:
            return False        

def are_inbounds(givenListOfValues, debugMode = False, debuggerTool = None):
    if is_list(givenListOfValues, debugMode, debuggerTool) is True:
        for i in givenListOfValues:
            if is_inbounds(i, debugMode, debuggerTool) is not True:
                if _do_debug is True:
                    debuggerTool.set_error_info("out_of_bounds_error", givenListOfValues, errorCheckerFunctionNameToAddToPath = "are_inbounds(givenListOfValues)")
                    return False
                else:
                    return False
        return True
    else:
        if _do_debug is True:
            debuggerTool.set_error_info("out_of_bounds_error", givenListOfValues, errorCheckerFunctionNameToAddToPath = "are_inbounds(givenListOfValues)")
            return False
        else:
            return False        

def _do_debug(debugMode, debuggerTool):
    if (debugMode is True) and (type(debuggerTool) == object):
        try:
            debuggerTool.is_debugger()
        except AttributeError:
            return False
        return True
    else:
        return False