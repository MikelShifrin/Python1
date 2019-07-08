#Nested loops

number = int(input("Please enter a number:\n"))
for i in range(0,number+1):
    for x in range(0,i):
        print("*",end="")
    print()
