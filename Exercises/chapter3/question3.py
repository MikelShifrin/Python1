#author: Mikel Shifrin
#age classifier program

#ask user to enter their age
age = int(input('Please enter your age in years:\n'))

#print their age classification
if age <= 1:
    print('You are an infant')
elif age > 1 and age < 13:
    print('You are a child')
elif age >= 13 and age < 20:
    print('You are a teenager')
elif age >= 20:
    print('You are an adult')
else:
    print('error')
