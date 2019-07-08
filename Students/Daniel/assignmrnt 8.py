#Assignment 8
#Using nested loops recreate the following pattern
#*******   (7)
#******    (6)
#*****     (5)
#****      (4)
#***       (3)
#**        (2)
#*         (1)
#Hint: for i in range(10,0,-1)

number = int(input("Please enter a number:\n"))
for i in range(number,0,-1):
    for x in range(i,0,-1):
        print("*", end="")
    print("")
