

def translate_coord_pair(coordPair, xChange = None, yChange = None, universalChange = None, xyChange = [None, None], troubleshoot = False):
    newCoordPair = list(coordPair)
    if len(newCoordPair) != 2:
        print("ERROR - Translate Coordinate Pair Function:'newCoordPair' arguement out of bounds. Should have length 2 but has length:", len(newCoordPair))
        print("        The list used for the 'newCoordPair' argumet must have a length of 2.")
        return newCoordPair
    elif (xChange is None) and (yChange is None) and (universalChange is None) and (not any(xyChange)):
        print("ERROR - Translate Coordinate Pair Function: No arguments to translate the 'newCoordPair' argument recieved.")
        print("        Enter a value for one of the optional arguments to translate the 'newCoordPair' armument as desired.")
        return newCoordPair
    elif ((xChange is not None) or (yChange is not None)) and (universalChange is None) and (not any(xyChange)):
        if (xChange is not None) and (yChange is not None):
            newCoordPair[0] += xChange
            newCoordPair[1] += yChange
            if troubleshoot is True:
                print("'xChange and 'yChange' used. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair
        elif (xChange is not None) and (yChange is None):
            newCoordPair[0] += xChange
            if troubleshoot is True:
                print("'xChange used. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair
        elif (xChange is None) and (yChange is not None):
            newCoordPair[1] += yChange
            if troubleshoot is True:
                print("'yChange used. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair
        else:
            print("ERROR - Translate Coordinate Pair Function: Unkown error with 'xChange' and/ or 'yChange' argument(s) occurred. Respectively the arguements recieved are:", xChange, "and", yChange)
    elif (xChange is None) and (yChange is None) and (universalChange is not None) and (not any(xyChange)):
        newCoordPair[0] += universalChange
        newCoordPair[1] += universalChange
        if troubleshoot is True:
            print("'universalChange' used. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
        return newCoordPair
    elif (xChange is None) and (yChange is None) and (universalChange is None) and (any(xyChange)):
        if (xyChange[0] is not None) and (xyChange[1] is not None):
            newCoordPair[0] += xyChange[0]
            newCoordPair[1] += xyChange[1]
            if troubleshoot is True:
                print("'xyChange' used with neither x or y being 'None'. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair
        elif (xyChange[0] is not None) and (xyChange[1] is None):
            newCoordPair[0] += xyChange[0]
            if troubleshoot is True:
                print("'xyChange' used with y being 'None'. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair
        elif (xyChange[0] is None) and (xyChange[1] is not None):
            newCoordPair[1] += xyChange[1]
            if troubleshoot is True:
                print("'xyChange' used with x being 'None'. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair
        else:
            print("ERROR - Translate Coordinate Pair Function: Unkown error with 'xyChange' argument occurred. 'xyChange' argument recieved:", xyChange)
            return newCoordPair
    elif ((xChange is not None) or (yChange is not None)) or (universalChange is not None) or (any(xyChange)):
        converted_xyChange = [xChange, yChange]
        converted_universalChange = [universalChange,universalChange]
        if (converted_xyChange == xyChange) and (any(xyChange)):
            if (xyChange[0] is not None) and (xyChange[1] is not None):
                newCoordPair[0] += xyChange[0]
                newCoordPair[1] += xyChange[1]
                if troubleshoot is True:
                    print("Multiple arguements recieved: At least 'xChange' and 'yChange' equal 'xyChange'. 'xyChange' used with neither x or y being 'None'. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
                return newCoordPair
            elif (xyChange[0] is not None) and (xyChange[1] is None):
                newCoordPair[0] += xyChange[0]
                if troubleshoot is True:
                    print("Multiple arguements recieved: At least 'xChange' and 'yChange' equal 'xyChange'. 'xyChange' used with y being 'None'. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
                return newCoordPair
            elif (xyChange[0] is None) and (xyChange[1] is not None):
                newCoordPair[1] += xyChange[1]
                if troubleshoot is True:
                    print("Multiple arguements recieved: At least 'xChange' and 'yChange' equal 'xyChange'. 'xyChange' used with x being 'None'. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
                return newCoordPair
            else:
                print("ERROR - Translate Coordinate Pair Function: Unkown error with 'xChange', 'yChange', or 'xyChange' argument(s) occurred. Respectively the arguments recieved are:", xChange, ",", yChange, ", and", xyChange)
                return newCoordPair
        elif (converted_universalChange == xyChange) and (any(xyChange)):
            newCoordPair[0] += universalChange
            newCoordPair[1] += universalChange
            if troubleshoot is True:
                print("Multiple arguements recieved: At least 'universalChange' equals 'xyChange'. 'universalChange' used. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair 
        elif (xChange == universalChange) and (yChange == universalChange):
            newCoordPair[0] += universalChange
            newCoordPair[1] += universalChange
            if troubleshoot is True:
                print("Multiple arguements recieved: At least 'xChange' and 'yChange' equal 'universalChange'. 'universalChange' used. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
            return newCoordPair
        elif (xChange is not None) and (yChange is not None) and (universalChange is not None) and (any(xyChange)):
            if (converted_xyChange == converted_universalChange) and (converted_xyChange == xyChange):
                newCoordPair[0] += universalChange
                newCoordPair[1] += universalChange
                if troubleshoot is True:
                    print("Multiple arguements recieved: 'xChange', 'yChange', 'universalChange', and 'xyChange' are all equal. 'universalChange' used. Arguments recieved: 'newCoordPair' =", coordPair, "'xChange' =", xChange, "'yChange' =", yChange, "'universalChange' =", universalChange, "'xyChange' =", xyChange, ". Returned:", newCoordPair)
                return newCoordPair
            else:
                print("ERROR - Translate Coordinate Pair Function: Multiple optional arguments recieved which do not all equal each other. In the order of'xChange', 'yChange', 'universalChange', and 'xyChange' the arguments recieved are:", xChange, ",", yChange, ",", universalChange, ", and", xyChange)
                return newCoordPair
        else:
            print("ERROR - Translate Coordinate Pair Function: Unkown error. In the order of'xChange', 'yChange', 'universalChange', and 'xyChange' the arguments recieved are:", xChange, ",", yChange, ",", universalChange, ", and", xyChange)
            return newCoordPair
    else:
        print("ERROR - Translate Coordinate Pair Function: Unkown error. In the order of'xChange', 'yChange', 'universalChange', and 'xyChange' the arguments recieved are:", xChange, ",", yChange, ",", universalChange, ", and", xyChange)
        return newCoordPair