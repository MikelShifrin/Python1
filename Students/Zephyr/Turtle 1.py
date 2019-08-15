import turtle

i = 1

while i != 0:

    turtle.setup(750, 750)
    turtle.penup()
    turtle.goto(-175,0)
    turtle.pendown()
    turtle.speed(10)
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor('blue')
    turtle.circle(75)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.circle(75)
    turtle.penup()
    turtle.goto(175,0)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.circle(75)
    turtle.penup()
    turtle.goto(87.5,-75)
    turtle.pendown()
    turtle.pencolor('green')
    turtle.circle(75)
    turtle.penup()
    turtle.goto(-87.5,-75)
    turtle.pendown()
    turtle.pencolor('yellow')
    turtle.circle(75)

