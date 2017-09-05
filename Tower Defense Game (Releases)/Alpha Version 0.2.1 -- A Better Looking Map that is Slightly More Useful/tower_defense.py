import math
import turtle
import sys
import os
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

def reset_button():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def start_button(x, y):
    print("Clearing Screen!")
    turtle.resetscreen()
    turtle.clearscreen()
    game_window()
    
def exit_button(x, y):
    button_drawer(75, -80, 330, 45, "Are you sure?", 22)
    print("Created 'Are you sure?' text box.")
    button_drawer(75, -155, 150, 45, "Yes", 22)
    print("Created 'Yes' button.")
    button_drawer(255, -155, 150, 45, "No", 22)
    print("Created 'No' button.")
    if 75 < x < 225 and -155 > y > -200:
        print("Closed Game")
        quit()
    elif 255 < x < 405 and -155 > y > -200:
        print("Game Reset")
        reset_button()
    elif 210 < x < 540 and -180 > y > -330:
        print("Game Reset")
        reset_button()
    elif -405 < x < -75 and 60 > y > -30:
        turtle.onscreenclick(start_button)
        turtle.mainloop()

def main_buttons(x, y):
    print("Cursor Click Cords: " + "(", x, "," ,y,")")
    if -405 < x < -75 and 60 > y > -30:
        turtle.onscreenclick(start_button)
        turtle.mainloop()
    elif 75 < x < 405 and 60 > y > -30:
        turtle.onscreenclick(exit_button)
        turtle.mainloop()
    elif 210 < x < 540 and -180 > y > -330:
        print("Game Reset")
        reset_button()

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
    smwd.penup()
    smwd.setpos(240, -29.5)
    smwd.pendown()
    smwd.pencolor("yellow")
    smwd.write("*Press twice, sorry!", False, "center", ("Arial", 10, "normal"))
    print("Created '*Press twice, sorry!' exit button disclaimer.")
    smwd.penup()
    smwd.setpos(-240, -29.5)
    smwd.pendown()
    smwd.write("*Press twice, sorry!", False, "center", ("Arial", 10, "normal"))
    print("Created '*Press twice, sorry!' start button disclaimer.")    
    smwd.pencolor("red")
    turtle.onscreenclick(main_buttons)
    turtle.mainloop()
    turtle.update
    
def game_window():
    maps.test_map()
    print("Map Drawn!")
    game_logic.logic()
    
start_menu_window()