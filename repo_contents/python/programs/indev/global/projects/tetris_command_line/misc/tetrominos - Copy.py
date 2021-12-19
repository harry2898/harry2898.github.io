#Helpful Links:
    #Tetris Wiki:
        # https://tetris.fandom.com/wiki/Tetris_Wiki
    #Tetris Guideline (rules) --- Tetris Wiki:
        # https://tetris.fandom.com/wiki/Tetris_Guideline
    #Super Rotation System (SRS) --- Tetris Wiki:
        # https://tetris.fandom.com/wiki/SRS
    #Tetrominos --- Tetris Wiki:
        # https://tetris.fandom.com/wiki/Tetromino
    #Official Tetris Game:
        # https://tetris.com/play-tetris
    #Unofficial Tetris Game --- Jstris:
        # https://jstris.jezevec10.com/


#Super Rotation System (SRS):
    #Uses SRS sized Rotation State Grids (RSGs) (RSG Sizes: [Tetrominoe = (x, y)], [I = (4, 4)], [O = (4, 3), [T, S, Z, J, and L = (3, 3)])
    #All RSGs contain the true respective position of each mino for the given Rotation State (RS) with respect to each of the other RSs
        #(looping through a tetrominoe's RSs (in order) would result in an animation of the tetrominoe rotating around the center point of its RGS)
    #All RSGs contain both minos and empty cells
#Minimum Grid System (MGS)
    #Uses smallest possible RSGs
    #RSGs do not contain the true respective position of each mino for the given Rotation State (RS) with respect to each of the other RSs
        #(looping through a tetrominoe's RSs (in order) would result in an animation of the tetrominoe rotating around its own center point)
    #RSGs only contain minos (no empty cells)
#Small Grid System (SGS):
    #



#Acronym List:
    #SRS: Super Rotation System
    #MGS: Minimum Grid System
    #SGS: Small Grid System
    #RSG(s): Rotation State Grid(s)
    #RS(s): Rotation State(s)


#Notes:
    #coord positions: (x, y)
    #playfield:
        #coord positions: (x, y)
        #bottom row: y = 1
        #top row: y = 20 --- (technically there are 20 additional rows above the visible playfield, therefore, --- top row: y = 40)
        #left column: x = 1
        #right column: x = 10
        #dimensions: (10, 20) --- (technically due to the 20 additional rows above the visible playfield --- dimensions: (10, 40))



#=======================================
#Uses a hybrid of the SRS and SGS systems 
#Uses coords to denote the location of each block that makes up the tetrominoe



#playfield spawn coords of I
def get_i_spawn():
    #Is: spawn coords of each block that makes up I
    Is = [[0, 3], [0, 4], [0, 5], [0, 6]]
    return Is

#---------------------------------------

#SRS rotation coords of I
def get_i_rotations():
    #Iso: SRS - list containing the SPAWN/ STANDARD rotation orientation coords of each block that forms the I tetrominoe
    #Iro: SRS - list containing the RIGHT rotation orientation coords of each block that forms the I tetrominoe
    #Iio: SRS - list containing the INVERTED rotation orientation coords of each block that forms the I tetrominoe
    #Ilo: SRS - list containing the LEFT rotation orientation coords of each block that forms the I tetrominoe
    #Io: SRS - list containing ALL four rotation orientation lists of I (in the order: [s, r, i, l])
    Iso = [[1, 0], [1, 1], [1, 2], [1, 3]]
    #Iso_to_Iro = [[-1, 2], [0, 1], [1, 0], [2, -1]]
    Iro = [[0, 2], [1, 2], [2, 2], [3, 2]]
    Iio = [[2, 0], [2, 1], [2, 2], [2, 3]]
    Ilo = [[0, 1], [1, 1], [2, 1], [3, 1]]
    Io = [Iso, Iro, Iio, Ilo]
    return Io




#=======================================
#Uses Minimal Grid (MIN) for orientations (smallest possible grid that fits the oriented piece)
#The size of each grid can vary (both across and within each tetrominoe)
#Uses coords to denote where each block should be ()


#I: MIN - list of all rotation orientation coord lists of I
def _get_i():
    I = [
        
        [
        [0, 0], [0, 1], [0, 2], [0, 3]
        ],
        
        [
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 0]
        ],
        
        [
        [0, 0], [0, 1], [0, 2], [0, 3]
        ],
        
        [
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 0]
        ]
        
        ]
    return I

#---------------------------------------

#I: MIN - list of all rotation orientation coord lists of O
def _get_o():
    O = [
        
        [
        [0, 0], [0, 1],
        [1, 0], [1, 1]
        ],
        
        [
        [0, 0], [0, 1],
        [1, 0], [1, 1]
        ],
        
        [
        [0, 0], [0, 1],
        [1, 0], [1, 1]
        ],
        
        [
        [0, 0], [0, 1],
        [1, 0], [1, 1]
        ]
        
        ]
    return O

#---------------------------------------

#I: MIN - list of all rotation orientation coord lists of T
def _get_t():
    T = [
        
        [
                [0, 1],
        [1, 0], [1, 1], [1, 2]
        ],
        
        [
        [0, 0],
        [1, 0], [1, 1],
        [2, 1]
        ],
        
        [
        [0, 0], [0, 1], [0, 2],
                [1, 1]
        ],
        
        [
                [0, 1],
        [1, 0], [1, 1],
                [2, 1]
        ]
        
        ]
    return T

#---------------------------------------

#I: MIN - list of all rotation orientation coord lists of S
def _get_s():
    S = [
        
        [
                [0, 1], [0, 2],
        [1, 0], [1, 1]
        ],
        
        [
        [0, 0],
        [1, 0], [1, 1],
                [2, 1]
        ],
        
        [
                [0, 1], [0, 2],
        [1, 0], [1, 1]
        ],
    
        [
        [0, 0],
        [1, 0], [1, 1],
                [2, 1]
        ]
        
        ]
    return S

#---------------------------------------

#I: MIN - list of all rotation orientation coord lists of Z
def _get_z():
    Z = [
        
        [
        [0, 0], [0, 1],
                [1, 1], [1, 2]
        ],
        
        [
                [0, 1],
        [1, 0], [1, 1],
        [2, 0]
        ],
        
        [
        [0, 0], [0, 1],
                [1, 1], [1, 2]
        ],
    
        [
                [0, 1],
        [1, 0], [1, 1],
        [2, 0]
        ]
        
        ]
    return Z

#---------------------------------------

#I: MIN - list of all rotation orientation coord lists of J
def _get_j():
    J = [
        
        [
        [0, 0],
        [1, 0], [1, 1], [1, 2]
        ],
        
        [
        [0, 0], [0, 1],
        [1, 0],
        [2, 0]
        ],
        
        [
        [0, 0], [0, 1], [0, 2],
                        [1, 2]
        ],
    
        [
                [0, 1],
                [1, 1],
        [2, 0], [2, 1]
        ]
        
        ]
    return J

#---------------------------------------

#I: MIN - list of all rotation orientation coord lists of L
def _get_l():
    L = [
        
        [
                        [0, 2],
        [1, 0], [1, 1], [1, 2]
        ],
        
        [
        [0, 0],
        [1, 0],
        [2, 0], [2, 1]
        ],
        
        [
        [0, 0], [0, 1], [0, 2],
        [1, 0]
        ],
    
        [
        [0, 0], [0, 1],
                [1, 1],
                [2, 1]
        ]
        
        ]
    return L



#=======================================

#SRS roation shape of I
def __get_i():
    #Iso: I spawn/ standard orientation
    #Iro: I right orientation
    #Iio: I inverted orientation
    #Ilo: I left orientation
    #Io: I orientations
    Iso = [
        [None, None, None, None], 
        ["#", "#", "#", "#"], 
        [None, None, None, None], 
        [None, None, None, None]
        ]
    Ir = [
        [None, None, "#", None], 
        [None, None, "#", None], 
        [None, None, "#", None], 
        [None, None, "#", None]
        ]
    Ii = [
        [None, None, None, None], 
        [None, None, None, None], 
        ["#", "#", "#", "#"], 
        [None, None, None, None]
        ]
    Il = [
        [None, "#", None, None], 
        [None, "#", None, None], 
        [None, "#", None, None], 
        [None, "#", None, None]
        ]
    Is
    
    O = [
        [None, "#", "#", None], 
        [None, "#", "#", None], 
        [None, None, None, None]
        ]
    
    T = [
        [None, "#", None], 
        ["#", "#", "#"], 
        [None, None, None]
        ]
    
    S = [
        [None, "#", "#"], 
        ["#", "#", None], 
        [None, None, None]
        ]
    
    Z = [
        ["#", "#", None], 
        [None, "#", "#"], 
        [None, None, None]
        ]
    
    J = [
        ["#", None, None], 
        ["#", "#", "#"], 
        [None, None, None]
        ]
    
    L = [
        [None, None, "#"], 
        ["#", "#", "#"], 
        [None, None, None]
        ]