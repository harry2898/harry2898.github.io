from mgs import *
from tetrominos import *

class tetris:
    def __init__(self, rotationSystem = None):
#Temporary, until Rotation System is worked out
#-------------------------------------------------------------------------------
        #Setting Rotation System
        #Setting Tetrominos RSGs
        if (rotationSystem is None):
            print("Nothing was given for rotationSystem")
            default_rotation_system()
        elif type(rotationSystem) != str:
            #general_error(...)
            print("Error: Given rotationSystem is not of type str")
            default_rotation_system()
        elif rotationSystem == "srs":
            print("Error: Could not load SRS")
            print("Neither SRS or SGS have been implemented yet")
            default_rotation_system()
            return
        elif rotationSystem == "mgs":
            print("Loading MGS")
            I = get_mgs_i()
            O = get_mgs_o()
            T = get_mgs_t()
            S = get_mgs_s()
            Z = get_mgs_z()
            J = get_mgs_j()
            L = get_mgs_l()
        elif rotationSystem == "sgs":
            print("Error: Could not load SGS")
            print("Neither SRS or SGS have been implemented yet")
            default_rotation_system()
            return
        else:
            #unknown_error(...)
            print("Unknown Error: Could not determine the given rotationSystem")
            default_rotation_system()
        
        def default_rotation_system(self):
            #Default is MGS
            print("Defaulting to MGS")
            print("Loading MGS")
            I = get_mgs_i()
            O = get_mgs_o()
            T = get_mgs_t()
            S = get_mgs_s()
            Z = get_mgs_z()
            J = get_mgs_j()
            L = get_mgs_l()        
#-------------------------------------------------------------------------------
        #Setting Tetrominos Spawn Position
        Isp = get_spawn_pos_i()
        Osp = get_spawn_pos_o()
        Tsp = get_spawn_pos_t()
        Ssp = get_spawn_pos_s()
        Zsp = get_spawn_pos_z()
        Jsp = get_spawn_pos_j()
        Lsp = get_spawn_pos_l()
        
        