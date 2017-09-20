import turtle
import math

def test_map():
    turtle.tracer(0,0)
    turtle.bgcolor("black")
    print("Set background color to black.")
    tmd = turtle.Turtle()
    tmd.pencolor("brown")
    tmd.penup()
    tmd.setpos(-540,360)
    tmd.pendown()
    tmd.fillcolor("brown")
    tmd.begin_fill()
    for i in range(2):
        tmd.forward(1080)
        tmd.right(90)
        tmd.forward(720)
        tmd.right(90)
    tmd.end_fill()
    print("Game map drawn.")
    tmd.pencolor("black")
    for i in range(12):
        tmd.forward(1080)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
        tmd.forward(1080)
        tmd.left(90)
        tmd.forward(30)
        tmd.left(90)
    tmd.left(90)
    for i in range(18):
        tmd.forward(720)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
        tmd.forward(720)
        tmd.left(90)
        tmd.forward(30)
        tmd.left(90)    
    tmd.penup()
    tmd.setpos(-540,-270)
    tmd.pendown()
    tmd.left(270)
    tmd.pencolor("gray")
    tmd.fillcolor("gray")
    tmd.begin_fill()  
    for i in range(2):
        tmd.forward(420)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
    tmd.end_fill()
    tmd.forward(390)
    tmd.left(90)
    tmd.begin_fill()  
    for i in range(2):
        tmd.forward(420)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
    tmd.end_fill()
    tmd.forward(390)
    tmd.left(90)
    tmd.begin_fill()  
    for i in range(2):
        tmd.forward(330)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
    tmd.end_fill()
    tmd.forward(330)
    tmd.right(90)
    tmd.begin_fill()  
    for i in range(2):
        tmd.forward(150)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
    tmd.end_fill()
    tmd.forward(180)
    tmd.right(90)
    tmd.begin_fill()  
    for i in range(2):
        tmd.forward(510)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
    tmd.end_fill()
    tmd.forward(510)
    tmd.right(90)
    tmd.begin_fill()      
    for i in range(2):
        tmd.forward(480)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
    tmd.end_fill()
    tmd.forward(450)
    tmd.left(90)
    tmd.begin_fill()      
    for i in range(2):
        tmd.forward(150)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)    
    tmd.end_fill()
    tmd.forward(120)
    tmd.left(90)
    tmd.begin_fill()      
    for i in range(2):
        tmd.forward(300)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)    
    tmd.end_fill()
    tmd.forward(300)
    tmd.right(90)
    tmd.begin_fill()      
    for i in range(2):
        tmd.forward(180)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)    
    tmd.end_fill()
    tmd.forward(180)
    tmd.right(90)
    tmd.begin_fill()  
    for i in range(2):
        tmd.forward(450)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)
    tmd.end_fill()
    tmd.forward(420)
    tmd.left(90)
    tmd.begin_fill()      
    for i in range(2):
        tmd.forward(150)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)    
    tmd.end_fill()
    tmd.forward(120)
    tmd.left(90)
    tmd.begin_fill()      
    for i in range(2):
        tmd.forward(630)
        tmd.right(90)
        tmd.forward(30)
        tmd.right(90)    
    tmd.end_fill()    
    tmd.penup()
    tmd.setpos(0,360)
    tmd.pendown()
    tmd.pencolor("red")
    tmd.write("Tower", False, "center", ("Arial", 100, "normal"))
    print("Created 'Tower' text on map.")
    tmd.penup()
    tmd.setpos(0,-510)
    tmd.pendown()    
    tmd.write("Defense", False, "center", ("Arial", 100, "normal"))
    print("Created 'Defense' text on map.")    
    turtle.update