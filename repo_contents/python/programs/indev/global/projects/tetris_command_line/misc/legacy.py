import time
import random

uiTop = []
uiTop.append(" ")
for i in range(10):
    uiTop.append("_")
uiTop.append(" ")

uiSides = "|"

uiBottom = []
uiBottom.append("|")
for i in range(10):
    uiBottom.append("_")
uiBottom.append("|")

playfield = []
for i in range (20):
    playfield.append([])
    for j in range(10):
        playfield[i].append(None)


def update_display():
    display = []
    for i in range(22):
        display.append([])
    display[0] = uiTop[0]
    for i in range(11):
        display[0] += uiTop[i + 1]
    #display[0] += "\n"
    for i in range(20):
        display[i + 1] = uiSides
        for j in range(10):
            if playfield[i][j] is None:
                display[i + 1] += " "
            else:
                display[i + 1] += playfield[i][j]
        display[i + 1] += uiSides
        #display[i] += "\n"
    display[21] = uiBottom[0]
    for i in range(11):
        display[21] += uiBottom[i + 1]
    #display[21] += "\n"
    return display

def is_inbounds(tetromino, orientation, yOffSet, xOffSet, debug = False):
    for i in range(len(tetromino[orientation])):
        if ((tetromino[orientation][i][0] + yOffSet) > (len(playfield) - 1)) or ((tetromino[orientation][i][0] + yOffSet) < 0) or ((tetromino[orientation][i][1] + xOffSet) > (len(playfield[0]) - 1)) or ((tetromino[orientation][i][1] + xOffSet) < 0):
            if debug is True:
                print("out of bounds")
                print((tetromino[orientation][i][0] + yOffSet), ">", (len(playfield) - 1))
                print((tetromino[orientation][i][0] + yOffSet) > (len(playfield) - 1))
                print("or")
                print((tetromino[orientation][i][1] + xOffSet), ">", (len(playfield[0]) - 1))
                print((tetromino[orientation][i][1] + xOffSet) > (len(playfield[0]) - 1))
            return False
    return True

def is_unoccupied(tetromino, orientation, yOffSet, xOffSet, debug = False):
    for i in range(len(tetromino[orientation])):
        if playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] == "X":
            if debug is True:
                print("occupied")
                print("playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] == 'X'")
                print("playfield[", tetromino, "[", orientation, "][", i, "][ 0 ] +", yOffSet, "][", tetromino, "[", orientation, "][", i, "][ 1 ] +", xOffSet, "==", playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet])
                print("tetromino[orientation][i][0] ==", tetromino[orientation][i][0], "yOffSet ==", yOffSet)
                print("tetromino[orientation][i][0] + yOffSet ==", tetromino[orientation][i][0] + yOffSet)
                print("tetromino[orientation][i][1] ==", tetromino[orientation][i][1], "xOffSet ==", xOffSet)
                print("tetromino[orientation][i][1] + xOffSet ==", tetromino[orientation][i][1] + xOffSet)
            return False
    return True

def place_tetromino(tetromino, orientation, yOffSet, xOffSet, debug = False, errorPrompt = False):
    count = 0
    for i in range(len(tetromino[orientation])):
        if playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] == " ":
            playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] = "#"
            count += 1
        else:
            if debug is True:
                print("Failed to place on i ==", i)
                print("playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] == ' '")
                print("playfield[", tetromino, "[", orientation, "][", i, "][ 0 ] +", yOffSet, "][", tetromino, "[", orientation, "][", i, "][ 1 ] +", xOffSet, "==", playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet])
                print("tetromino[orientation][i][0] ==", tetromino[orientation][i][0], "yOffSet ==", yOffSet)
                print("tetromino[orientation][i][0] + yOffSet ==", tetromino[orientation][i][0] + yOffSet)
                print("tetromino[orientation][i][1] ==", tetromino[orientation][i][1], "xOffSet ==", xOffSet)
                print("tetromino[orientation][i][1] + xOffSet ==", tetromino[orientation][i][1] + xOffSet)
    if count == 4:
        return True
    else:
        if debug is True:
            print("Expected to place 4, but only placed:", count)
        if errorPrompt is True:
            if error_input_prompt() is True:
                return True
            else:
                return False
        else:
            return True

def remove_tetromino(tetromino, orientation, yOffSet, xOffSet, debug = False, errorPrompt = False):
    count = 0
    for i in range(len(tetromino[orientation])):
        if playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] == "#":
            playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] = " "
            count += 1
        else:
            if debug is True:
                print("Failed to remove on i ==", i)
                print("playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet] == '#'")
                print("playfield[", tetromino, "[", orientation, "][", i, "][ 0 ] +", yOffSet, "][", tetromino, "[", orientation, "][", i, "][ 1 ] +", xOffSet, "==", playfield[tetromino[orientation][i][0] + yOffSet][tetromino[orientation][i][1] + xOffSet])
                print("tetromino[orientation][i][0] ==", tetromino[orientation][i][0], "yOffSet ==", yOffSet)
                print("tetromino[orientation][i][0] + yOffSet ==", tetromino[orientation][i][0] + yOffSet)
                print("tetromino[orientation][i][1] ==", tetromino[orientation][i][1], "xOffSet ==", xOffSet)
                print("tetromino[orientation][i][1] + xOffSet ==", tetromino[orientation][i][1] + xOffSet)        
    if count == 4:
        return True
    else:
        if debug is True:
            print("Expected to remove 4, but only removed:", count)
        if errorPrompt is True:
            if error_input_prompt() is True:
                return True
            else:
                return False
        else:
            return True

def update_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet, newOrientation, newYOffSet, newXOffSet):
    if is_inbounds(tetromino, newOrientation, newYOffSet, newXOffSet, debug = True) is False:
        player_action(tetromino, currentOrientation, currentYOffSet, currentXOffSet)
    elif is_unoccupied(tetromino, newOrientation, newYOffSet, newXOffSet, debug = True) is False:
        player_action(tetromino, currentOrientation, currentYOffSet, currentXOffSet)
    else:
        noErrorsOccurred = True
        if remove_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet, debug = True, errorPrompt = True) is False:
            noErrorsOccurred = False
        if place_tetromino(tetromino, newOrientation, newYOffSet, newXOffSet, debug = True, errorPrompt = True) is False:
            noErrorsOccurred = False
        return noErrorsOccurred

def move_tetromino(direction, tetromino, currentOrientation, currentYOffSet, currentXOffSet):
    newOrientation = currentOrientation
    newYOffSet = currentYOffSet
    newXOffSet = currentXOffSet + direction
    if update_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet, newOrientation, newYOffSet, newXOffSet) is False:
        return False
    else:
        return True

def rotate_tetromino(direction, tetromino, currentOrientation, currentYOffSet, currentXOffSet):
    #Probably will need to be fixed so it auto adjust if new location is out of bounds or occupied.
    if currentOrientation + direction > 3:
        newOrientation = 0
    elif currentOrientation + direction < 0:
        newOrientation = 3
    else:
        newOrientation = currentOrientation + direction
    newYOffSet = currentYOffSet
    newXOffSet = currentXOffSet
    if update_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet, newOrientation, newYOffSet, newXOffSet) is False:
        return False
    else:
        return True

def soft_drop_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet):
    newOrientation = currentOrientation
    newYOffSet = currentYOffSet + 1
    newXOffSet = currentXOffSet
    if update_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet, newOrientation, newYOffSet, newXOffSet) is False:
        return False
    else:
        return True

def hard_drop_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet):
    #TODO
    return

def hold_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet):
    #TODO
    return

def player_action(tetromino, currentOrientation, currentYOffSet, currentXOffSet):
    playerAction = input("Action:").lower()
    if len(playerAction) > 1:
        playerAction = playerAction[0]
    if playerAction.isalpha() is False:
        print("Invalid Action Entered! --- input was not a letter --- input:", playerAction)
        player_action(tetromino, currentOrientation, currentYOffSet, currentXOffSet)
    elif playerAction == "q":
        #rotate left (-1)
        if rotate_tetromino(-1, tetromino, currentOrientation, currentYOffSet, currentXOffSet) is False:
            return False
        else:
            return True
    elif playerAction == "w":
        #hold
        if hold_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet) is False:
            return False
        else:
            return True
    elif playerAction == "e":
        #rotate right (+1)
        if rotate_tetromino(1, tetromino, currentOrientation, currentYOffSet, currentXOffSet) is False:
            return False
        else:
            return True
    elif playerAction == "a":
        #move left (x-1)
        if move_tetromino(-1, tetromino, currentOrientation, currentYOffSet, currentXOffSet) is False:
            return False
        else:
            return True
    elif playerAction == "s":
        #soft drop (y-1)
        if soft_drop_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet) is False:
            return False
        else:
            return True
    elif playerAction == "d":
        #move right (x+1)
        if move_tetromino(1, tetromino, currentOrientation, currentYOffSet, currentXOffSet) is False:
            return False
        else:
            return True
    elif playerAction == " ":
        #hard drop (y-#)
        if hard_drop_tetromino(tetromino, currentOrientation, currentYOffSet, currentXOffSet) is False:
            return False
        else:
            return True
    elif playerAction == "pause":
        #TODO
        return
    elif playerAction == "settings":
        #TODO
        return
    elif playerAction == "options":
        #TODO
        return
    elif playerAction == "menu":
        #TODO
        return
    elif playerAction == "restart":
        #TODO
        return
    elif playerAction == "stop":
        return False
    elif playerAction == "quit":
        return False
    elif playerAction == "end":
        return False
    else:
        print("Invalid Action Entered! --- input had no assigned keybind --- input:", playerAction)
        player_action(tetromino, currentOrientation, currentYOffSet, currentXOffSet)
        
def error_input_prompt():
    continueGame = input("A potentially game breaking error has occurred! Attempt to continue the game? (y/n)").lower()
    if (continueGame == "y") or (continueGame == "yes"):
        return True
    elif (continueGame == "n") or (continueGame == "no"):
        return False
    else:
        print("Invalid Response Entered! --- input was not 'y' or 'n' --- input:", continueGame)
        print("Please enter either 'y' for yes or 'n' for no.")
        error_input_prompt()

#Game Functions:
#hard drop
#hold
#player actions options
#next tetromino
#**fix rotate**
#randomly generate tetrominos
#spawn tetrominos
#detect for top out
#tetromino drop speed
#convert playfield to 0's and 1's to see if a line is cleared by checking if the line equals 10
#709=
#main loop
#get next tetromino
#lock tetromino in place
#convert it from '#' to 'X'
#check for cleared lines
#convert cleared lines from 'X' to 'O' for a few frames as an animation
#remove cleared lines ('O's)
#adjust playfield (down) accordingly
#increase score accordingly
#add cleared lines to total lines cleared
#increase level accordingly
#increase tetromino drop speed accordingly
#update display


#UI:
#main menu
#settings/ options (includes how many lines you can see in your terminal)
#instructions/ help
#pause menu
#score
#hold
#next
#level
#lines






#lost = False
#while lost is False:
    
grid = []
for i in range(6):
    grid.append([])
    for j in range(10):
        grid[i].append("O")
    
def put_on_grid(thing, horOffSet = 0, vertOffSet = 0, char = "X", clear = False):
    for i in range(len(thing)):
        if ((thing[i][0] + vertOffSet) > (len(grid) - 1)) or ((thing[i][0] + vertOffSet) < 0) or ((thing[i][1] + horOffSet) > (len(grid[0]) - 1)) or ((thing[i][1] + horOffSet) < 0):
            print("out of bounds")
            print((thing[i][0] + vertOffSet), ">", (len(grid) - 1))
            print((thing[i][0] + vertOffSet) > (len(grid) - 1))
            print("or")
            print((thing[i][1] + horOffSet), ">", (len(grid[0]) - 1))
            print((thing[i][1] + horOffSet) > (len(grid[0]) - 1))
            return False
    if clear is True:
        for i in range(len(thing)):
            if grid[thing[i][0] + vertOffSet][thing[i][1] + horOffSet] != "N":
                grid[thing[i][0] + vertOffSet][thing[i][1] + horOffSet] = "O"
        return True
    for i in range(len(thing)):
        if grid[thing[i][0] + vertOffSet][thing[i][1] + horOffSet] == "X":
            return False
    for i in range(len(thing)):
        grid[thing[i][0] + vertOffSet][thing[i][1] + horOffSet] = char
    return True
        
def print_grid():
    for i in range(len(grid)):
        print(grid[i])

def move_on_grid(before):
    moveInput = input("Move:")
    if moveInput == "d":
        if put_on_grid(before[0], before[1] + 1, char = "N") is True:
            put_on_grid(before[0], horOffSet = before[1], clear = True)
        else:
            return False
    elif moveInput == "a":
        if put_on_grid(before[0], before[1] - 1, char = "N") is True:
            put_on_grid(before[0], horOffSet = before[1], clear = True)
        else:
            print("Could not move there")
            return False
    elif moveInput == "r":
        rotate(before, Io.index(before[0]) + 1)
    else:
        print("Invalid move inputed! Move inputed was:", moveInput)
    return True

#current[tetrimino, orientation, horizontal_offset, vertical_offset]

def rotate(before, rotation):
    if put_on_grid(Io[rotation], before[1], before[2], char = "N") is True:
        put_on_grid(before[0], horOffSet = before[1], vertOffSet = before[2], clear = True)
    else:
        return False
    return True

#put_on_grid(Iro, horOffSet = 3, vertOffSet = 0)

Iso = [[1, 0], [1, 1], [1, 2], [1, 3]]
#Iso_to_Iro = [[-1, 2], [0, 1], [1, 0], [2, -1]]
Iro = [[0, 2], [1, 2], [2, 2], [3, 2]]
Iio = [[2, 0], [2, 1], [2, 2], [2, 3]]
Ilo = [[0, 1], [1, 1], [2, 1], [3, 1]]
Io = [Iso, Iro, Iio, Ilo]

put_on_grid(Iro, horOffSet = 2, vertOffSet = 2)
put_on_grid(Iro, horOffSet = 4, vertOffSet = 2)
put_on_grid(Iso, horOffSet = 3, char = "C")
print_grid()
move_on_grid([Iso, 3, 0])
print("")
print_grid()
