#assignment3
#ask user to enter a number between 1-7 
#1.Sunday
#2.Monday
#3.Tuesday
#4.Wednesday
#5.Thursday
#6.Friday
#7.Saturday
number = int(input("please enter a number between 1 to 7:\n"))
if number == 7:
    print('Saturday')
elif number == 6:
    print('Friday')
elif number == 5:
    print('Thursday')
elif number == 4:
    print('Wednesday')
elif number == 3:
    print('Tuesday')
elif number == 2:
    print ('Monday')
elif number == 1:
    print ('Sunday')
else:
    print('ERROR')











#assignment4
#ask user to enter a number between 1-10
#1.I
#2.II
#3.III
#4.IV
#5.V
#6.VI
#7.VII
#8.VIII
#9.IX
#10.X
number= int(input("please enter a number between 1 to 10:\n"))
if number == 10:
    print("X")
elif number == 9:
    print("IX")
elif number == 8:
    print("VIII")
elif number == 7:
    print("VII")
elif number == 6:
    print("VI")
elif number == 5:
    print("V")
elif number == 4:
    print("IV")
elif number == 3:
    print("III")
elif number == 2:
    print("II")
elif number == 1:
    print ("I")
else:
    print("NUMBER EXCEEDING LIMIT ")
