from error_utils import *
from checker_utils import *

def get_spawn_pos_i():
    iSpawnPos = [
                    [4, 20], [5, 20], [6, 20], [7, 20]
                ]
    return iSpawnPos

def get_spawn_pos_o():
    oSpawnPos = [
                    [5, 20], [6, 20], 
                    [5, 19], [6, 19]
                ]
    return oSpawnPos

def get_spawn_pos_t():
    tSpawnPos = [
                             [5, 20],
                    [4, 19], [5, 19], [6, 19]
                ]
    return tSpawnPos

def get_spawn_pos_s():
    sSpawnPos = [
                             [5, 20], [6, 20],
                    [4, 19], [5, 19]
                ]
    return sSpawnPos

def get_spawn_pos_z():
    zSpawnPos = [
                    [4, 20], [5, 20],
                             [5, 19], [6, 19]
                ]
    return zSpawnPos

def get_spawn_pos_j():
    jSpawnPos = [
                    [4, 20],
                    [4, 19], [5, 19], [6, 19]
                ]
    return jSpawnPos

def get_spawn_pos_l():
    lSpawnPos = [
                                      [6, 20],
                    [4, 19], [5, 19], [6, 19]
                ]
    return lSpawnPos

def left(currentXPos, exactAmount = 0):
    if is_int([currentXPos, exactAmount]) is False:
        not_int_error("left", ["currentXPos", "exactAmount"], [currentXPos, exactAmount])
        return False
    elif (exactAmount == 0) and ((currentXPos - 1) > 0):
        newXPos = currentXPos - 1
        return newXPos
    elif ((currentXPos - exactAmount) > 0) and (exactAmount > 0):
        newXPos = currentXPos - exactAmount
        return newXPos
    elif (currentXPos - exactAmount) < 11:
        newXPos = currentXPos - exactAmount
        return newXPos
    else:
        unknown_error("left", ["currentXPos", "exactAmount"], [currentXPos, exactAmount])
        
def right(currentXPos, exactAmount = 0):
    if is_int([currentXPos, exactAmount]) is False:
        not_int_error("right", ["currentXPos", "exactAmount"], [currentXPos, exactAmount])
        return False
    elif exactAmount < 0:
        newXPos = left(currentXPos, abs(exactAmount))    
    elif (currentXPos + 1) < 11:
        newXPos = currentXPos + 1
        return newXPos
        return newXPos
    elif (currentXPos + exactAmount) < 11:
        newXPos = currentXPos + exactAmount
        return newXPos
    else:
        unknown_error("right", ["currentXPos", "exactAmount"], [currentXPos, exactAmount])

def down(currentYPos, exactAmount = 0):
    #TODO
    return