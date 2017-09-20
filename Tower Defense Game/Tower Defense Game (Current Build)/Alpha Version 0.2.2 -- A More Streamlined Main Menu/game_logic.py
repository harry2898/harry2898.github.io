import math
import turtle
    
    
def logic():
    print("Game logic running")
    turtle.onscreenclick(get_cords_of_click)
    
def get_cords_of_click(x,y):
    print("Cursor Click Cords: " + "(", x, "," ,y,")")
    x_tile = int((x + 540) / 30 + 1)
    y_tile = int((y + 360) / 30 + 1)
    if x_tile < -8 or x_tile > 46 or y_tile < 1 or y_tile > 24:
        print("You clicked outside of the map!")
    elif -9 < x_tile < 1 and 0 < y_tile < 25:
        print("You clicked a UI!")
    elif 36 < x_tile < 47 and 0 < y_tile < 25:
        print("You clicked a UI!")
    elif 0 < x_tile < 15 and y_tile == 3:
        print("You clicked on the path!")
    elif x_tile == 14 and 3 < y_tile < 18:
        print("You clicked on the path!")
    elif 2 < x_tile < 14 and y_tile == 17:
        print("You clicked on the path!")
    elif x_tile == 3 and 17 < y_tile < 23:
        print("You clicked on the path!")
    elif 3 < x_tile < 20 and y_tile == 22:
        print("You clicked on the path!")
    elif x_tile == 19 and 22 > y_tile > 6:
        print("You clicked on the path!")
    elif 19 < x_tile < 25 and y_tile == 7:
        print("You clicked on the path!")
    elif x_tile == 24 and 7 < y_tile < 18:
        print("You clicked on the path!")
    elif 24 < x_tile < 30 and y_tile == 17:
        print("You clicked on the path!")
    elif x_tile == 29 and 17 > y_tile > 2:
        print("You clicked on the path!")
    elif 29 < x_tile < 35 and y_tile == 3:
        print("You clicked on the path!")
    elif x_tile == 34 and 3 < y_tile < 25:
        print("You clicked on the path!")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    else:    
        print("Tile Click Cords: " + "(", x_tile, "," ,y_tile,")")