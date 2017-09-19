import turtle
import time

turtle.colormode(255)

line1 = turtle.Turtle()
line1.penup()
line1.setpos(-127, 0)
line1.pendown()
line1.pensize(20)

line2 = turtle.Turtle()
line2.penup()
line2.setpos(0, 127)
line2.pendown()
line2.right(90)
line2.pensize(20)

line3 = turtle.Turtle()
line3.penup()
line3.setpos(88.5, 88.5)
line3.pendown()
line3.right(135)
line3.pensize(20)

line4 = turtle.Turtle()
line4.penup()
line4.setpos(-88.5, 88.5)
line4.pendown()
line4.right(45)
line4.pensize(20)

x = 1
for i in range(1):
    for i in range(255):
        c1 = i 
        c2 = 0
        c3 = 255 - i
        
        line1.pencolor(c1, c2, c3)
        line1.forward(1)
        print("Line 1: " + str(c1) + ", " + str(c2) + ", " + str(c3))
        
        line2.pencolor(c3, c1, c2)
        line2.forward(1)
        print("Line 2: " + str(c1) + ", " + str(c2) + ", " + str(c3))
        
        line3.pencolor(c1, c2, c3)
        line3.forward(1)
        print("Line 3: " + str(c1) + ", " + str(c2) + ", " + str(c3))
        
        line4.pencolor(c1, c2, c3)
        line4.forward(1)
        print("Line 4: " + str(c1) + ", " + str(c2) + ", " + str(c3))
    
    line1.right(180)
    line2.right(180)
    line3.right(180)
    line4.right(180)
        
    for i in range(255):
        c1 = 255 - i
        c2 = i
        c3 = 0
     
        line1.pencolor(c1, c2, c3)
        line1.forward(1)
        print("Line 1: " + str(c1) + ", " + str(c2) + ", " + str(c3))
        
        line2.pencolor(c3, c1, c2)
        line2.forward(1)
        print("Line 2: " + str(c1) + ", " + str(c2) + ", " + str(c3))
        
        line3.pencolor(c3, c1, c2)
        line3.forward(1)
        print("Line 3: " + str(c1) + ", " + str(c2) + ", " + str(c3))
        
        line4.pencolor(c3, c1, c2)
        line4.forward(1)
        print("Line 4: " + str(c1) + ", " + str(c2) + ", " + str(c3))
     
turtle.mainloop()



#time.sleep(.002614)