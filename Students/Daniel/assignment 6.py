#Assignment 6
#Sum of numbers
#Ask user to enter positive integers and print out the sum
#To stop counting ask user to input -1

number = 0
total = 0
while number != -1:
    total += number
    number = float(input("Please enter positive integers(enter -1 to stop):\n"))
print(total)
