#=======================================
#SRS str



#SRS roation shape of I
def get_srs_str_i():
    #Iso: I spawn/ standard orientation (first list block)
    #Iro: I right orientation (second list block)
    #Iio: I inverted orientation (third list block)
    #Ilo: I left orientation (forth list block)
    #Io: I orientations... (DNE)
    I = [
            [
                [None, None, None, None], 
                ["#", "#", "#", "#"], 
                [None, None, None, None], 
                [None, None, None, None]
            ],
            [
                [None, None, "#", None], 
                [None, None, "#", None], 
                [None, None, "#", None], 
                [None, None, "#", None]
            ],
            [
                [None, None, None, None], 
                [None, None, None, None], 
                ["#", "#", "#", "#"], 
                [None, None, None, None]
            ],
            [
                [None, "#", None, None], 
                [None, "#", None, None], 
                [None, "#", None, None], 
                [None, "#", None, None]
            ]
        ]
    return I

#---------------------------------------

def get_srs_str_o():
    O = [
            [
                [None, "#", "#", None],
                [None, "#", "#", None],
                [None, None, None, None]
            ],
            [
                [None, "#", "#", None],
                [None, "#", "#", None],
                [None, None, None, None]
            ],
            [
                [None, "#", "#", None],
                [None, "#", "#", None],
                [None, None, None, None]
            ],
            [
                [None, "#", "#", None],
                [None, "#", "#", None],
                [None, None, None, None]
            ]            
        ]
    return O

#---------------------------------------

def get_srs_str_t():
    T = [
            [
                [None, "#", None],
                ["#", "#", "#"],
                [None, None, None]
            ],
            [
                [None, "#", None],
                [None, "#", "#"],
                [None, "#", None]
            ],
            [
                [None, None, None],
                ["#", "#", "#"],
                [None, "#", None]
            ],
            [
                [None, "#", None],
                ["#", "#", None],
                [None, "#", None]
            ],            
        ]
    return T

#---------------------------------------

def get_srs_str_s():
    S = [
            [
                [None, "#", "#"],
                ["#", "#", None],
                [None, None, None]
            ],
            [
                [None, "#", None],
                [None, "#", "#"],
                [None, None, "#"]
            ],
            [
                [None, None, None],
                [None, "#", "#"],
                ["#", "#", None]
            ],
            [
                ["#", None, None],
                ["#", "#", None],
                [None, "#", None]
            ],            
        ]
    return S

#---------------------------------------

def get_srs_str_z():
    Z = [
            [
                ["#", "#", None],
                [None, "#", "#"],
                [None, None, None]
            ],
            [
                [None, None, "#"],
                [None, "#", "#"],
                [None, "#", None]
            ],
            [
                [None, None, None],
                ["#", "#", None],
                [None, "#", "#"]
            ],
            [
                [None, "#", None],
                ["#", "#", None],
                ["#", None, None]
            ],            
        ]
    return Z

#---------------------------------------

def get_srs_str_j():
    J = [
            [
                ["#", None, None],
                ["#", "#", "#"],
                [None, None, None]
            ],
            [
                [None, "#", "#"],
                [None, "#", None],
                [None, "#", None]
            ],
            [
                [None, None, None],
                ["#", "#", "#"],
                [None, None, "#"]
            ],
            [
                [None, "#", None],
                [None, "#", None],
                ["#", "#", None]
            ],            
        ]
    return J

#---------------------------------------

def get_srs_str_l():
    L = [
            [
                [None, None, "#"],
                ["#", "#", "#"],
                [None, None, None]
            ],
            [
                [None, "#", None],
                [None, "#", None],
                [None, "#", "#"]
            ],
            [
                [None, None, None],
                ["#", "#", "#"],
                ["#", None, None]
            ],
            [
                ["#", "#", None],
                [None, "#", None],
                [None, "#", None]
            ],            
        ]
    return L




#=======================================
#SRS int



def get_srs_int_i():
    I = [
            [
                [0, 0, 0, 0], 
                [1, 1, 1, 1], 
                [0, 0, 0, 0], 
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 1, 0], 
                [0, 0, 1, 0], 
                [0, 0, 1, 0], 
                [0, 0, 1, 0]
            ],
            [
                [0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [1, 1, 1, 1], 
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 0, 0], 
                [0, 1, 0, 0], 
                [0, 1, 0, 0], 
                [0, 1, 0, 0]
            ]
        ]
    return I

#---------------------------------------

def get_srs_int_o():
    O = [
            [
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ]            
        ]
    return O

#---------------------------------------

def get_srs_int_t():
    T = [
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0]
            ],            
        ]
    return T

#---------------------------------------

def get_srs_int_s():
    S = [
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [1, 1, 0]
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0]
            ],            
        ]
    return S

#---------------------------------------

def get_srs_int_z():
    Z = [
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1]
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0]
            ],            
        ]
    return Z

#---------------------------------------

def get_srs_int_j():
    J = [
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0]
            ],            
        ]
    return J

#---------------------------------------

def get_srs_int_l():
    L = [
            [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0]
            ],
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ],            
        ]
    return L



#=======================================