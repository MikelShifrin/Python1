#Lists and Tuples

#List of strings
'''
names = ['Eric','Mikel','Patrick', 'Fenghua', 'Haochen']

print(names)
print(names[0])
'''

#List of integers
'''
numbers = [100, 63, 96, 43]
'''

#List of mixed data types
'''
info = ['hello', 1, 4.9]
'''

#Other ways of creating lists
'''
a = list(range(10))
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = list(range(1, 10, 2))
print(b)
# [1, 3, 5, 7, 9]

c = [1] * 5
print(c)
# [1, 1, 1, 1, 1] 
'''

#Iterating over a List with for Loop
'''
names = ['Eric','Mikel','Patrick', 'Fenghua', 'Haochen']
for i in names:
    print(i)
'''

#Indexing
'''
i = 0
while i < len(names):
    print(names[i])
    i += 1

print(names[-1])
# Haochen
print(names[-2])
#Fenghua

print(names[5])
'''

#List mutability
'''
names = ['Eric','Mikel','Patrick', 'Fenghua', 'Haochen']
names[0] = 'Bob'
'''

#List Concatenating
'''
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = list1 + list2
print(list3)
'''

#List Slicing
'''
list3 = [1, 2, 3, 'a', 'b', 'c']
print(list3[:])    # [1, 2, 3, 'a', 'b', 'c']
print(list3[2:])   # [3, 'a', 'b', 'c']
print(list3[:5])   # [1, 2, 3, 'a', 'b']
print(list3[1:6:2])# [2, 'a', 'c']
print(list3[-3:])  # ['a', 'b', 'c']
list3 = list3[2:5] # [3, 'a', 'b']
print(list3)
'''

#Search Lists with the in Operator
'''
names = ['Eric','Mikel','Patrick', 'Fenghua', 'Haochen']
search = 'Edward'

if search in names:
    print('found ya!')
else:
    print('not there :(')
'''

#List methods and Built-in Functions

#append(item)         - adds item to end of list
#index(item)          - returns index of item
#insert(index, item)  - inserts item at specified index
#sort()               - sorts list in order
#remove(item)         - removes 1st occurence of item from list           
#reverse()            - reverses list 

names = ['Eric','Mikel','Patrick', 'Fenghua', 'Haochen']
names.append('Edward')
print(names)

print(names.index('Fenghua'))

names.insert(1 ,'Bob')
print(names)

names.sort()
print(names)















