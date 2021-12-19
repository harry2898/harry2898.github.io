#=======================================
#Uses Minimum Grid System (MGS) for RSGs (smallest possible grid that fits the oriented piece)
#The size of each grid can vary (both across and within each tetromino)
#Uses coords to denote where each block should be ()


#I: MGS - list of all rotation orientation coord lists of I
def get_mgs_i():
    I = [
            [
                [1, 1], [2, 1], [3, 1], [4, 1]
            ],
            [
                [1, 4],
                [1, 3],
                [1, 2],
                [1, 1]
            ],
            [
                [1, 1], [2, 1], [3, 1], [4, 1]
            ],
            [
                [1, 4],
                [1, 3],
                [1, 2],
                [1, 1]
            ]
            
        ]
    return I

#---------------------------------------

#O: MGS - list of all rotation orientation coord lists of O
def get_mgs_o():
    O = [
            [
                [1, 2], [2, 2],
                [1, 1], [2, 1]
            ],
            [
                [1, 2], [2, 2],
                [1, 1], [2, 1]
            ],
            [
                [1, 2], [2, 2],
                [1, 1], [2, 1]
            ],
            [
                [1, 2], [2, 2],
                [1, 1], [2, 1]
            ]
        ]
    return O

#---------------------------------------

#T: MGS - list of all rotation orientation coord lists of T
def get_mgs_t():
    T = [
            [
                        [2, 2],
                [1, 1], [2, 1], [3, 1]
            ],
            [
                [1, 3],
                [1, 2], [2, 2],
                [1, 1]
            ],
            [
                [1, 2], [2, 2], [3, 2],
                        [2, 1]
            ],
            [
                        [2, 3],
                [1, 2], [2, 2],
                        [2, 1]
            ]
        ]
    return T

#---------------------------------------

#S: MGS - list of all rotation orientation coord lists of S
def get_mgs_s():
    S = [
            [
                        [2, 2], [3, 2],
                [1, 1], [2, 1]
            ],
            [
                [1, 3],
                [1, 2], [2, 2],
                        [2, 1]
            ],
            [
                        [2, 2], [3, 2],
                [1, 1], [2, 1]
            ],
            [
                [1, 3],
                [1, 2], [2, 2],
                        [2, 1]
            ]
        ]
    return S

#---------------------------------------

#Z: MGS - list of all rotation orientation coord lists of Z
def get_mgs_z():
    Z = [
            [
                [1, 2], [2, 2],
                        [2, 1], [3, 1]
            ],
            [
                        [2, 3],
                [1, 2], [2, 2],
                [1, 1]
            ],
            [
                [1, 2], [2, 2],
                        [2, 1], [3, 1]
            ],
            [
                        [2, 3],
                [1, 2], [2, 2],
                [1, 1]
            ]
        ]
    return Z

#---------------------------------------

#J: MGS - list of all rotation orientation coord lists of J
def get_mgs_j():
    J = [
            [
                [1, 2],
                [1, 1], [2, 1], [3, 1]
            ],
            [
                [1, 3], [2, 3],
                [1, 2],
                [1, 1]
            ],
            [
                [1, 2], [2, 2], [3, 2],
                                [3, 1]
            ],
            [
                        [2, 3],
                        [2, 2],
                [1, 1], [2, 1]
            ]
        ]
    return J

#---------------------------------------

#L: MGS - list of all rotation orientation coord lists of L
def get_mgs_l():
    L = [
            [
                                [3, 2],
                [1, 1], [2, 1], [3, 1]
            ],
            [
                [1, 3],
                [1, 2],
                [1, 1], [2, 1]
            ],
            [
                [1, 2], [2, 2], [3, 2],
                [1, 1]
            ],
            [
                [1, 3], [2, 3],
                        [2, 2],
                        [2, 1]
            ]
        ]
    return L



#=======================================