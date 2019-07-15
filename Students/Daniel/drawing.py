import turtle


turtle.setup(1000, 640)     #size of graphics screen (widht, height) in pixels
turtle.showturtle()         #shows pointer
turtle.hideturtle()         #hides pointer
turtle.pencolor("red")      #selects the pen color
turtle.forward(200)         #draws forward in pixels
turtle.left(90)             #turns pointer left in degrees based on current position
turtle.right(90)            #turns pointer right in degrees based on current position
turtle.setheading(0)        #turns pointer counter clockwise in degrees from initial
turtle.penup()              #doesn't write but can move around
turtle.pendown()            #starts writing
turtle.circle(50)           #draws a circle
turtle.dot()                #draws a dot
turtle.pensize(1)           #thickness of pen
turtle.bgcolor("blue")      #sets background color
turtle.reset                #completely resets your turtle
turtle.clear                #clears everything but keeps your bakscreen, penup, pendown, etc
turtle.clearscreen
turtle.goto(10, 10)         #moves to position (0, 0) and draws a line
turtle.pos()                #returns current cartesian position on shell
turtle.xcor()               #returns the x from the current cartesian position
turtle.ycor()               #returns the y from the current cartesian position
turtle.speed(1)             #controls animations speed number netween 1-10 (slowest to fastest) or 0 with animation
turtle.write("Hello world") #writes text at current position of cursor
turtle.fillcolor("green")   #decide on shape fill color
turtle.begin_fill()         #starts fillbefore drawing shape
turtle.circle(100)
turtle.end_fill()           #ebds fill after drawing shape

turtle.done()               #keeps graphics window open
