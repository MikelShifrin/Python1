import turtle as i

i.setup(700,700)
i.hideturtle()
i.penup()
i.goto(-25,25)
i.pendown()

total = 50

while True:
    
    i.speed(50)
    i.forward(total)
    i.right(90)
    i.forward(total)
    i.right(90)
    i.forward(total)
    i.right(90)
    i.forward(total)
    i.penup()
    i.forward(10)
    i.left(90)
    i.forward(10)
    i.right(180)
    i.pendown()
    total = total + 20
