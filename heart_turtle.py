import math
import turtle

#set up the screen 
Window = turtle.Screen()
Window.bgcolor("black")

#set up the turtle
pen = turtle.Turtle()
pen.speed(0) 
pen.color("red")

#functiuon to define the heart shape
def heart(t):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x, y
#draw the heart patern 
pen.penup()
for i in range(10): 
    pen.goto(0, 0)
    pen.pendown()
    for t in range (0, 100, 2):
        x,y = heart(t/ 10)
        pen.goto(x * i,y * i)
    pen.penup()

pen.hideturtle()
turtle.done()
