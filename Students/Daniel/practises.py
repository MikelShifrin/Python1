#Nested loops
'''
number = int(input("Please enter a number:\n"))
for i in range(0,number+1):
    for x in range(0,i):
        print("*",end="")
    print()
'''
#Input and if statement

house = input("Please enter your favorite house(1 = Griffindor, 2 = Slytherin, 3 = Hufflepuff and 4 = Ravenclaw):\n")

if house == 1:
    print("Welcome to Griffindor, new wizard!")
elif house == 2:
    print("Welcome to Slytherin, new wizard!")
elif house == 3:
    print("Welcome to Hufflepuff, new wizard!")
else:
     print("Welcome to Ravenclaw, new wizard!")
