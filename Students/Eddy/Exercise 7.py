#Assignment 6
#Sum of numbers
#Ask user to enter positive integers and print out the sum
#To stop counting ask user to input -1

print("Calculor\nThis calculator will continuously calculate the sum of the entered numbers.\nEnter -1 to stop it")
num = int(input('Enter as much as POSITIVE numbers as you want:\n'))
total = 0

while num != -1:
    total += num
    num = int(input("Enter as much as POSITIVE numbers as you want(enter -1 to stop):\n"))
    

print('Total sum = ', total)

