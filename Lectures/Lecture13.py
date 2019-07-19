#Dictionaries and Sets

#Dictionaries
#Creating a Dictionary
'''
age = {'Chase':11, 'Mikel':23, 'Daniel':10, 'Aheesh':12}
print(age['Mikel'])
'''
#Using the in and not in Operators to Test for a in a Dictionary
'''
age = {'Chase':11, 'Mikel':23, 'Daniel':10, 'Aheesh':12}
if 'Daniel' in age:
    print(age['Daniel'])

else:
    print('not in dictionary')
'''
#Adding Elements to an Existing Dictioary
'''
age = {'Chase':11, 'Mikel':23, 'Daniel':10, 'Aheesh':12}
age['Chase'] = 12
age['Peter'] = 14
print(age)
'''
#Deleting Elements
'''
age = {'Chase':11, 'Mikel':23, 'Daniel':10, 'Aheesh':12}
del age['Mikel']
print(age)
'''
#Size of Dictionary

age = {'Chase':11, 'Mikel':23, 'Daniel':10, 'Aheesh':12}
print(len(age))

#Mixing Data Types in a Dictionary
'''
age = {'Chase':11, 'Mikel':'person', 'Daniel':10.5, 'Aheesh':True}
'''
