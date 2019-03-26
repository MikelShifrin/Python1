#author: Mikel Shifrin
#program that converts numbers 1-10 to roman numerals

#ask user to input a number between 1 to 10
number = int(input('Please enter an integer between 1 to 10:\n'))

#print out the coresponding roman numeral
if number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')
else:
    print('That is an invalid number')
