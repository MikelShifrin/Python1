#author: Mikel

#ask user for input
answer = input("Please enter a number between 1 and 7:")

#display the day of the week based on the input
if answer == '1':
    print('Sunday')
elif answer == '2':
    print('Monday')
elif answer == '3':
    print('Tuesday')
elif answer == '4':
    print('Wednesday')
elif answer == '5':
    print('Thursday')
elif answer == '6':
    print('Friday')
elif answer == '7':
    print('Saturday')
else:
    print('error')
