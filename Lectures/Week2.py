import turtle

turtle.setup(1000, 640)     #size of graphics screen (width, height) in pxs
turtle.showturtle()         #shows pointer
turtle.hideturtle()         #hides pointer
turtle.pencolor('red')      #selects the pen color
turtle.forward(200)         #draws forward in pxs
turtle.left(90)             #turns pointer left in degrees based on current position
turtle.right(90)            #turns pointer right in degrees based on current position
turtle.setheading(0)        #turns pointer counter clockwise in degrees from initial pos
turtle.penup()              #doesn't write but can move around
turtle.pendown()            #starts writing       
turtle.circle(50)           #draws a circle with radius in pxs
turtle.dot()                #draws a dot
turtle.pensize(10)          #thickness of pen
turtle.bgcolor('blue')      #sets background color

turtle.reset()
turtle.clear()
turtle.clearscreen()

turtle.goto(10, 10)         #moves to position (0,0) and draws a line
turtle.pos()                #returns current cartesian position on shell
turtle.xcor()               #returns the x from the current cartesian position
turtle.ycor()               #returns the y from the current cartesian position
turtle.speed(1)             #controls animation speed number between 1-10 (slowest to fastest) or 0 with no animation
turtle.write('hello world') #writes text at current position of cursor

turtle.fillcolor('pink')    #decide on shape fill color  
turtle.begin_fill()         #starts fill before drawing shape
turtle.circle(100)
turtle.end_fill()           #ends fill after drawing shape
turtle.done()               #keeps graphics window open
