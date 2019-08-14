#Dictionaries

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
'''
age = {'Chase':11, 'Mikel':23, 'Daniel':10, 'Aheesh':12}
print(len(age))
'''
#Mixing Data Types in a Dictionary
'''
age = {'Chase':11, 'Mikel':'person', 'Daniel':10.5, 'Aheesh':True}
'''
#Creating an Empty Dictionary
'''
age = {}
age['Chase'] = 11
age['Mikel'] = 23
print(age)
'''
#Using the for Loop to iterate over a Dictionary
'''
age = {'Chase':11, 'Mikel':'person', 'Daniel':10.5, 'Aheesh':True}
for key in age:
    print(key)
    print(age[key])
'''
#Some Dictionary Methods
age = {'Chase':11, 'Mikel':'person', 'Daniel':10.5, 'Aheesh':True}
#clear
#get
#items
#keys
#pop
#popitem
#values
'''
print(age)
age.clear()
print(age)
'''
'''
print(age.get('Chase'))
print(age.get('Bob'))
print(age['Bob'])
'''
'''
print(age.items())
'''
'''
print(age.keys())
'''
'''
print(age.pop('Mikel'))
print(age)
'''
'''
deletes randoms key, value pair 
print(age.popitem())
print(age)
values
'''










