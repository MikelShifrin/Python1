#Calculating a running total
number = int(input('Please enter a positive integer:'))
total = 0
for value in range(number+1):
    total = total + value
print(total)

#Sentinel Loop
number = 0
total = 0
while number != -1:
    total += number
    number = float(input("Please enter a positive number (-1 to stop):"))
print(total)

#Nested Loops

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ":", minutes, ":", seconds)

#Assignment 6
#Sum of numbers
#Ask user to enter positive integers and print out the sum
#To stop counting ask user to input -1

#Assignment 7
#Calculating the factorial of a number
#Ask user to input a positive integer
#calculate and print out the factorial of that number
#Reminder: 7! = 7x6x5x4x3x2x1

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
