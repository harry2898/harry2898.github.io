def is_int(variableToCheck):
    if type(variableToCheck) != list:
        isInt = type(variableToCheck) == int
        return isInt
    else:
        for i in range(len(variableToCheck)):
            if type(variableToCheck[i]) != int:
                return False
        return True

def is_str(variableToCheck):
    #TODO
    return

def is_bool(variableToCheck):
    #TODO
    return

def is_list(variableToCheck):
    #TODO
    return

def is_iterable(variableToCheck, notString = True):
    if (notString is True) and (type(variableToCheck) == str):
        return False
    try:
        iterableChecker = iter(variableToCheck)
    except TypeError:
        return False
    return True

def all_none(listOfVariables):
    #TODO
    return

def is_valid_move(tetromino, xChange = None, yChange = None, xyCoordPairChange = None):
    #TODO
    return

def is_inbounds():
    #TODO
    return