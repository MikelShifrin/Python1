#Nested loops

number = int(input("Please enter a number:\n"))
for i in range(0,number+1,1):
    for x in range(0,i,1):
        print("*",end="")
    print()

#*#*if i put 2, it does'nt work
