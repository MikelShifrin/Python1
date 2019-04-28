#Assignment 7
#Calculating the factorial of a number
#Ask user to input a positive integer
#calculate and print out the factorial of that number
#Reminder: 7! = 7x6x5x4x3x2x1

number = 0

while number < 1:
	number = int(input("Please enter a positive integer:\n"))

total = 1
for count in range(1, number + 1):
	total *= count

print("Total", total)