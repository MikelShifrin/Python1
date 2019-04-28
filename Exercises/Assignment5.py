#Assignment 5
#Ask user to input a positive integer
#calculate and print the running total
#ex: input = 5
#total = 1+2+3+4+5
#output = total

number = 0

while number < 1:
	number = int(input("Please enter a positive integer:\n"))

total = 0	
for count in range(nuber + 1):
	total += count

print("Total =" , total)