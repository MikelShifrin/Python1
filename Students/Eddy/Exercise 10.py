#Assignment 1
#
#Draw the olympic logo with color using Turtle
#for a reference of the olympic logo use the following link:
#https://github.com/MikelShifrin/Python1/blob/master/Images/Olympic%20Logo.png

import turtle

turtle.setup(10000, 10000)
turtle.hideturtle()
turtle.pencolor('blue')
turtle.pensize(15)
turtle.circle(100)
turtle.penup()
turtle.right(90)
turtle.forward(15)  
turtle.pendown()
turtle.pencolor('yellow')
turtle.circle(100)
turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(215)
turtle.setheading(180)  
turtle.pendown()
turtle.pencolor('black')
turtle.circle(100)
#turtle.penup()

turtle.right(-90)
turtle.forward(-15)  
turtle.pendown()
turtle.pencolor('green')
turtle.circle(100)
turtle.penup()



'''
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
turtle.circle(50)
'''
