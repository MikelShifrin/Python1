#assignement 5
#ask user to input a positive integer
#calculate and print the running total
#ex: input = 5
#total = 1+2+3+4+5
#output = total

number = int(input("Please enter a positive integer number:\n"))
total = 0
for count in range(number+1):
    total = total + count
print(total)
