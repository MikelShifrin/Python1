#Assignment 7
#Calculating the factorial of a number
#Ask user to input a positive integer
#calculate and print out the factorial of that number
#Reminder: 7! = 7x6x5x4x3x2x1


num = int(input("Please enter a positive number.\n"))

while num <0:
    num = int(input("Please enter a POSITIVE number. (idiot)\n"))


total = 1
for num1 in range(1 , num + 1):
    total = total * num1

print(total)
