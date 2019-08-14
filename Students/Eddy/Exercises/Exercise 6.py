#Assignment 5
#Ask user to input a positive integer
#calculate and print the running total
#ex: input = 5
#total = 1+2+3+4+5
#output = total

num = int(input("Please enter a positive number:\n"))

while num < 0:
    num = int(input("Enter a POSITIVE number!\n"))

total = 0
for num1 in range(0, num+1):
    total = total + num1
print(total)

    



