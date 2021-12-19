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
    #Pieces (Polyominoes) --- Misc:
        # https://tetris.fandom.com/wiki/Piece


#Super Rotation System (SRS):
    #Uses SRS sized Rotation State Grids (RSGs) (RSG Sizes: [Tetrominoe = (x, y)], [I = (4, 4)], [O = (4, 3), [T, S, Z, J, and L = (3, 3)])
    #All RSGs contain the true respective position of each mino for the given Rotation State (RS) with respect to each of the other RSs
        #(looping through a tetromino's RSs (in order) would result in an animation of the tetromino rotating around the center point of its RGS)
    #All RSGs contain both minos and empty cells
#Minimum Grid System (MGS)
    #Uses smallest possible RSGs
    #RSGs do not contain the true respective position of each mino for the given Rotation State (RS) with respect to each of the other RSs
        #(looping through a tetromino's RSs (in order) would result in an animation of the tetromino rotating around its own center point)
    #RSGs only contain minos (no empty cells)
#Small Grid System (SGS):
    #



#Acronym List:
    #SRS: Super Rotation System - Official Tetris System
    #MGS: Minimum Grid System - *?* similar to old Tetris System
    #SGS: Small Grid System - Hybrid between SRS and MGS
    #RSG(s): Rotation State Grid(s) - Stores a tetromino's RS, including its orientation and respective position data which is required to rotate the tetromino correctly) 
        #*(a RSG can only contain one RS)*
    #RS(s): Rotation State(s) - The orientation of a tetromino when rotated


#Coord System:
    #Everything (applies to/ is used by/ is true of everything that uses coords)
        #coord positions: (x, y)
        #position of (0, 0): bottom left corner
    #RSGs:
        #bottom row: y = 1
        #left column: x = 1
    #playfield:
        #bottom row: y = 1
        #top row: y = 20 --- (technically there are 20 additional rows above the visible playfield, therefore, --- top row: y = 40)
        #left column: x = 1
        #right column: x = 10
        #dimensions: (10, 20) --- (technically due to the 20 additional rows above the visible playfield --- dimensions: (10, 40))
        
        
        


Cut/ Paste:

#=======================================
#Uses a hybrid of the SRS and SGS systems 
#Uses coords to denote the location of each block that makes up the tetromino



#playfield spawn coords of I
def get_i_spawn():
    #Is: spawn coords of each block that makes up I
    Is = [[0, 3], [0, 4], [0, 5], [0, 6]]
    return Is

#---------------------------------------

#SRS rotation coords of I
def get_i_rotations():
    #Iso: SRS - list containing the SPAWN/ STANDARD rotation orientation coords of each block that forms the I tetromino
    #Iro: SRS - list containing the RIGHT rotation orientation coords of each block that forms the I tetromino
    #Iio: SRS - list containing the INVERTED rotation orientation coords of each block that forms the I tetromino
    #Ilo: SRS - list containing the LEFT rotation orientation coords of each block that forms the I tetromino
    #Io: SRS - list containing ALL four rotation orientation lists of I (in the order: [s, r, i, l])
    Iso = [[1, 0], [1, 1], [1, 2], [1, 3]]
    #Iso_to_Iro = [[-1, 2], [0, 1], [1, 0], [2, -1]]
    Iro = [[0, 2], [1, 2], [2, 2], [3, 2]]
    Iio = [[2, 0], [2, 1], [2, 2], [2, 3]]
    Ilo = [[0, 1], [1, 1], [2, 1], [3, 1]]
    Io = [Iso, Iro, Iio, Ilo]
    return Io



    print("NOT INT ERROR - Function", functionName, "--- At least one of the given arguments is not an int!")
    if (type(argumentNames) != list) and (type(argumentValues) != list):
        print("For argument", argumentNames, "was given:", argumentValues, "  with type:", type(argumentValues), "  Is type int:", is_int(argumentValues))
    elif (type(argumentNames) == list) and (type(argumentValues) == list) and (len(argumentNames) == len(argumentValues)):
        #print("Argument Name\t\t\tArgument Value\t\tArgument Type\tIs Type Int")
        for i in range(len(argumentNames)):
            print("For argument", argumentNames[i], "was given:", argumentValues[i], "  with type:", type(argumentValues[i]), "  Is type int:", is_int(argumentValues[i]))
    elif len(argumentNames) != len(argumentValues):
        dev_error(functionName, argumentNames, argumentValues, causeOfError = "argumentNames and argumentValues have different lengths", valuesThatCausedError = [len(argumentNames), len(argumentValues)], generatedErrorFunctionErrorReport = "not_int_error")
    else:
        dev_error(functionName, argumentNames, argumentValues, causeOfError = "unknown", generatedErrorFunctionErrorReport = "not_int_error")
    return False
    
    
    
    
    
    print("DEV ERROR - Function Name:", functionName)
    print("Argument Names:", argumentNames)
    print("Argument Values:", argumentValues)
    if generatedErrorFunctionErrorReport is not None:
        print("Function Name:", generatedErrorFunctionErrorReport)
    if causeOfError is not None:
        print("Cause of Error:", causeOfError)
    if valuesThatCausedError is not None:
        print("Values That Caused Error:", valuesThatCausedError)
    print_this(printThis, iterateThroughPrintThis)
    print("End of Dev Error Report")
    return False
    
    
    
    
    
        print("UNKNOWN ERROR - Function Name:", functionName)
    print("Argument Names:", argumentNames)
    print("Argument Values:", argumentValues)
    print_this(printThis, iterateThroughPrintThis)
    return False
    
    
    
    
        print("ERROR - Function Name:", functionName)
    print("Argument Names:", argumentNames)
    print("Argument Values:", argumentValues)
    if causeOfError is not None:
        print("Cause of Error:", argumentValues)
    print_this(printThis, iterateThroughPrintThis)  
    return False
    
    
    

def create_playfield(twentyOrForty):
    if type(twentyOrForty) != int:
        #Not Int Error
        return
    elif (twentyOrForty != 20) or (twentyOrForty != 40):
        #Given value is invalid
        return
    elif (twentyOrForty == 20) or (twentyOrForty == 40):
        playfield = []
        for i in range(twentyOrForty + uiVerticalSize):
            playfield.append([])
            for j in range(10 + uiHorizontalSize):
                playfield[i].append(logicEmptyCells)
            
    else:
        #Unknown Error
        return
        
        
        
        
def coord_pair_tester():
    coordGrid = create_coord_grid()
    correctCounter = 0
    incorrectCounter = 0
    #errorCounter = 0
    for i in range(10000):
        loopNum = i + 1
        x = random.randint(1, 10)
        y = random.randint(1, 20)
        gridCoordPair = [x, y]
        listCoordPair = translate_coord_pair(gridCoordPair)
        #try:
            #if (coordGrid[listCoordPair[1]][listCoordPair[0]][0] == gridCoordPair):
                #correctCounter += 1
            #else:
                #incorrectCounter += 1
        #except TypeError:
            #errorCounter += 1
        #print(coordGrid[listCoordPair[1]][listCoordPair[0]][1], gridCoordPair)
        if (coordGrid[listCoordPair[1]][listCoordPair[0]][1] == gridCoordPair):
            correctCounter += 1
        else:
            incorrectCounter += 1
        correctPercentage = correctCounter / loopNum
        incorrectPercentage = incorrectCounter / loopNum
        #errorPercentage = errorCounter / loopNum
        #print("Loop #:", loopNum, "\t\tCorrect %:", correctPercentage, "\t\tIncorrect %:", incorrectPercentage, "\t\tError %:", errorPercentage)
        if i % 1000 == 0:
            print("Loop #:", loopNum, "\t\tCorrect %:", correctPercentage, "\t\tIncorrect %:", incorrectPercentage, "\t\tC#:", correctCounter, "\t\tI#:", incorrectCounter)




coord_pair_tester()

#coordGrid = create_coord_grid()
#for i in range(len(coordGrid)):
    #print(coordGrid[i])
#print(coordGrid[0][0])
#print(coordGrid[1][1][0])
#print(coordGrid[7][7])
#print(coordGrid[10][3])
#print(coordGrid[14][9])
#print(coordGrid[17][6])