'''
from turtle import *

speed(10)
left(135)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(400)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
hideturtle()
'''
from turtle import *

speed(0)
left(90)
penup()
goto(200,-200)
pendown()
for count in range(0,400,4):
    forward(count)
    left(90)
    forward(count)
    left(90)
    forward(count)
    left(90)
    forward(count)
    left(90)
