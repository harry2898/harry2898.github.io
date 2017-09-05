import math
import turtle
import maps
import game_logic

def button_drawer(x, y, width, height, text, font_size):
    turtle.tracer(0,0)    
    bdd = turtle.Turtle()
    bdd.penup()
    bdd.setpos(x, y)
    bdd.pendown()
    bdd.pencolor("blue")
    bdd.fillcolor("blue")
    bdd.begin_fill()
    for i in range(2):
        bdd.forward(width)
        bdd.right(90)
        bdd.forward(height)
        bdd.right(90)
    bdd.end_fill()
    bdd.penup()
    bdd.pencolor("yellow")
    bdd.setpos((x + width / 2), (y - height + 5))
    bdd.pendown()
    bdd.write(text, False, "center", ("Arial", font_size, "normal"))
    turtle.update

def main_buttons(x, y):
    print("Cursor Click Cords: " + "(", x, "," ,y,")")
    if -405 < x < -75 and 60 > y > -30:
        print("Clearing Screen!")
        turtle.resetscreen()
        turtle.clearscreen()
        game_window()
    elif 75 < x < 405 and 60 > y > -30:
        print("Closed Game")
        quit()
    elif 210 < x < 540 and -180 > y > -330:
        print("Game Reset")
        turtle.resetscreen()
        turtle.clearscreen()
        start_menu_window()

def start_menu_window():
    turtle.tracer(0,0)
    turtle.bgcolor("black")
    turtle.setup(1080, 720)
    print("Created start menu window.")
    button_drawer(-405, 60, 330, 90, "Start", 45)
    print("Created 'Start' button.")
    button_drawer(75, 60, 330, 90, "Exit", 45)
    print("Created 'Exit' button.")
    button_drawer(210, -270, 330, 90, "Reset", 45)
    print("Created 'Reset' button.")
    smwd = turtle.Turtle()
    smwd.setpos(0, 120)
    smwd.pencolor("red")
    smwd.write("Tower Defense", False, "center", ("Arial", 100, "normal"))
    print("Created 'Tower Defense' text.")
    turtle.onscreenclick(main_buttons)
    turtle.mainloop()
    turtle.update
    
def game_window():
    maps.test_map()
    print("Map Drawn!")
    game_logic.logic()
    
start_menu_window()