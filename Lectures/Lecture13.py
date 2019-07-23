#Basic String Operations

#Iterating over a String with the for loop
'''
name = "Mikel"
for i in name:
    print(i)
'''
#Indexing
'''
name = 'Chase Zhang'
print(name[0])
print(name[-1])
'''
#IndexError Exceptions
'''
name = 'Chase Zhang'
print(name[11])
'''
#The len Function
'''
name = 'Mikel'
print(len(name))
'''
#String Concatenation
'''
fname = 'Mikel'
lname = 'Shifrin'
age = 23
name = fname + ' ' + lname + str(age)
print(name)
'''
#Strings are immutable

#String Slicing
#Just like lists
'''
name = 'Mikel Shifrin'
print(name[:])             #Mikel Shifrin
print(name[2:])            #kel Shifrin
print(name[:5])            #Mikel
print(name[6:9])           #Shi
print(name[0:len(name)])   #Mikel Shifrin
name = name[-7:]    
print(name)                #Shifrin 
'''
#Testing Strings with in and not in
'''
fname = 'Chase'
name = 'Chase Zhang'
if fname in name:
    print('True')
else:
    print('False')
'''
#String Methods

#Some String Testing Methods
'''
isalnum()
isalpha()
isadigit()
islower()
isspace()
isupper()
'''

#Modification Methods
'''
lower()
lstrip()
lstrip(char)
rstrip()
rstrip(char)
strip()
strip(char)
upper()
'''

#Searching and Replacing
'''
endswith(substring)
find(substring)
replace(old, new)
startswith(substring)
'''

#The Repetiotion Operator
'''
name = 'Mikel'
repeat = name * 5
print(repeat)
# MikelMikelMikelMikelMikel
'''

#Splitting a String
split()
split(char)












