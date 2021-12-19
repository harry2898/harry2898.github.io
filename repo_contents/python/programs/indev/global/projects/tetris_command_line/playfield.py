from config import *

import random

def get_playfield():
    playfield = add_ui_to_playfield(create_playfield_grid())
    

def create_playfield_grid():
    playfield = []
    for i in range(playfieldHeight):
        playfield.append([])
        for j in range(playfieldWidth):
            playfield[i].append(logicEmptyCells)
    return playfield

def add_ui_to_playfield(playfieldGrid):
    return
    
def get_ui_boarder_coords():
    uiBoarderCoords = []
    for i in range(totalPlayfieldHeight):
        uiBoarderCoords.append([])
        for j in range(totalPlayfieldWidth):
            if i < uiTopBoarderSize:
                uiBoarderCoords[i].append(uiTopBoarder)
            elif i > totalPlayfieldHeight - uiBottomBoarderSize - 1:
                uiBoarderCoords[i].append(uiBottomBoarder)
            elif j < uiLeftBoarderSize:
                uiBoarderCoords[i].append(uiLeftBoarder)
            elif j > totalPlayfieldWidth - uiRightBoarderSize - 1:
                uiBoarderCoords[i].append(uiRightBoarder)
            else:
                uiBoarderCoords[i].append("-")
    flip = 0
    if flip == 1:
        for i in range(len(uiBoarderCoords)):
            print(uiBoarderCoords[i])
    else:
        print(stringify(uiBoarderCoords))
        
def translate_coord_pair(coordPair):
    coordGrid = create_coord_grid()
    coordPair[0] -= 1
    coordPair[1] = 20 - coordPair[1]
    return coordPair
    #x - 1
    #20 - y
    
def create_coord_grid():
    coordGrid = []
    for i in range(playfieldHeight):
        coordGrid.append([])
        for j in range(playfieldWidth):
            x = j + 1
            y = playfieldHeight - i          
            #coordGrid[i].append([x, y])
            coordGrid[i].append([[x, y], [j, i]])
    return coordGrid

def stringify(givenList):
    stringified = ""
    for i in range(len(givenList)):
        if i > 0:
            stringified = "".join(stringified + "\n")
        for j in range(len(givenList[i])):
            stringified = "".join(stringified + str(givenList[i][j]))
    return stringified


get_ui_boarder_coords()