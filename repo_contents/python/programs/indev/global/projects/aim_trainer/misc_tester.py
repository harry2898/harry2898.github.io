import turtle
import time
import random

from config import *
from utils import *

from color_constants_rgb_lists import *

screenWidth = 640
screenHeight = 480
screenDim = [screenWidth, screenHeight]

screenTopLeftCorner = [screenWidth / -2, screenHeight / 2]
screenTopRightCorner = [screenWidth / 2, screenHeight / 2]
screenBottomRightCorner = [screenWidth / 2, screenHeight / -2]
screenBottomLeftCorner = [screenWidth / -2, screenHeight / -2]

windowWidth = screenWidth + 100
windowHeight = screenHeight + 100
winDim = [windowWidth, windowHeight]

WIN = turtle.Screen()
WIN.colormode(255)
WIN.bgcolor(WHITE)
WIN.setup(windowWidth, windowHeight)

screenBoarder = turtle.Turtle()
screenBoarder.color("green")
screenBoarder.speed(0)
screenBoarder.penup()
screenBoarder.goto(screenTopLeftCorner[0], screenTopLeftCorner[1])
screenBoarder.pendown()
print(screenBoarder.pos())
for i in range(2):
    screenBoarder.forward(screenWidth)
    print(screenBoarder.pos())
    screenBoarder.right(90)
    screenBoarder.forward(screenHeight)
    screenBoarder.right(90)
    print(screenBoarder.pos())


l = 200
w = 40

s = 5
f = 2

x = 0 - (l / 2)
y = 0 + (l / 2)

t = turtle.Turtle()

t.penup()
#t.goto(x, y)
#t.pendown()

t.shape("circle")
#t.width(w)
t.color(BLUE)
t.goto(0, 0)
t.stamp()



yw = 1

y = turtle.Turtle()
y.penup()
#y.goto(int(turtle.window_width() / 4), 0)
#y.shape("circle")
y.shape("square")
y.width(yw)
y.resizemode("user")
y.shapesize(s, s, 0)
y.color(RED1)


off = 5
_x = 400
_y = 400
y.goto(int(_x / -2 - off), 0)

#c = 0
#while True:
    #for i in range(2):
        #for i in range(int(l / w)):
            #t.forward(int(l / w) + int((w/ 2) + c))
            #t.stamp()
        #t.right(90)
        #c += 1
        
#y.goto(int(turtle.window_width() / - 2) + int(w / 3), 0)
y.stamp
o = w
print(turtle.window_width(), turtle.window_height())
print("\t\t\twidth|\t\tshapesize\t|\t\t\tpos\t\t\t|scaleFactor")
num = 2
for i in range(num):
    if i == 0:
        print("Loop #:" + str(i) + ":\t" + str(round(y.width(), 2)) + "\t|\t(" + str(round(y.shapesize()[0], 2)) + ", " + str(round(y.shapesize()[1], 2)) + ", " + str(round(y.shapesize()[2], 2)) + ")\t|\t(" + str(round(y.pos()[0], 2)) + ", " + str(round(y.pos()[0], 2)) + ")\t|\t" + str(round(s, 2)))        
    else:
        print("Loop #:" + str(i) + ":\t" + str(round(y.width(), 2)) + "\t|\t(" + str(round(y.shapesize()[0], 2)) + ", " + str(round(y.shapesize()[1], 2)) + ", " + str(round(y.shapesize()[2], 2)) + ")\t|\t(" + str(round(y.pos()[0], 2)) + ", " + str(round(y.pos()[0], 2)) + ")\t|\t" + str(round(s, 2)))
    #y.forward(int(y.width() * s * f))
    s = s * f
    y.shapesize(s, s, 0)
    t.stamp()
    if i == num - 1:
        print("Loop #:" + str(i + 1) + ":\t" + str(round(y.width(), 2)) + "\t|\t(" + str(round(y.shapesize()[0], 2)) + ", " + str(round(y.shapesize()[1], 2)) + ", " + str(round(y.shapesize()[2], 2)) + ")\t|\t(" + str(round(y.pos()[0], 2)) + ", " + str(round(y.pos()[0], 2)) + ")\t|\t" + str(round(s, 2)))
    time.sleep(.2)

n = turtle.Turtle()
n.penup()
n.goto(int(_x / 2 + off), 0)
#y.shape("circle")
n.shape("square")
n.width(yw)
n.resizemode("user")
n.shapesize(s, s, 0)
n.color(ORANGE)

#s = 1

#y = turtle.Turtle()
#y.penup()
#y.goto(int(turtle.window_width() / 4), 0)
#y.shape("circle")
#y.resizemode("user")
#y.shapesize(s, s, 0)
#y.color(RED1)

#t.goto(int(turtle.window_width() / - 4), 0)
#for i in range(20):
    ##print(t.width())
    #print(y.shapesize())
    #t.stamp()
    #y.stamp()
    #w = w * 2
    #s = s * 1.25
    #t.width(w)
    #y.shapesize(s, s, 0)
    #time.sleep(.25)
    
b = turtle.Turtle()
b.penup()
b.goto(turtle.window_width() / - 2, turtle.window_height() / 2)
b.pendown()
b.speed(0)
for i in range(2):
    b.forward(turtle.window_width())
    b.right(90)
    b.forward(turtle.window_height())
    b.right(90)
    
def bt(pnx, pny):
    b.penup()
    #b.goto(_x / - 2, _y / 2)
    b.goto(_x * pnx, _y * pny)
    b.pendown()
    b.speed(0)
    for i in range(2):
        b.forward(_x)
        b.right(90)
        b.forward(_y)
        b.right(90)
bt(-1, .5)
bt(0, .5)

lt = turtle.Turtle()
lt.penup()
lt.hideturtle()
while True:
    for i in range(2):
        lt.forward(100)
        lt.right(90)