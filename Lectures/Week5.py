#Repetition Loops

#The while loop
'''
number = 0

while number < 10:
    print(number)
    number = number + 1
print('outside of while loop')
'''
#Infinite While loop
'''
number = 0

while True:
    print(number)
    number = number + 1
print('outside of while loop')
'''
#The for loop using list
'''
for age in [1, 2, 20, 'stuff']:
    print(age)
'''
#The for loop using range(one)
'''
for count in range(10):
    print(count)
'''
#The for loop using range(one, two)
'''
for count in range(1, 10):
    print(count)
'''
#The for loop using range(start, end, step)
'''
for count in range(1, 10, 2):
    print(count)
'''
#Letting user control loop
'''
count = int(input('How many times do you want to loop?'))
for number in range(count):
    print(number)
'''
#Input validation loops
'''
number = int(input('Please enter a number between 1-7:\n'))
while number < 1 or number > 7:
    number = int(input('Please enter a number between 1-7:\n'))
'''
#Assignment 5
#Ask user to input a positive integer
#calculate and print the running total
#ex: input = 5
#total = 1+2+3+4+5
#output = total
