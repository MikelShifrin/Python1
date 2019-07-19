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
info = ['hello', 1, 4.9, True]
'''

#Other ways of creating lists
'''
a = list(range(10))
print(a)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = list(range(1, 10, 2))
print(b)
# [1, 3, 5, 7, 9]

c = [1, 2] * 5
print(c)
# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2] 
'''

#Iterating over a List with for Loop
'''
names = ['Eric','Mikel','Patrick', 'Fenghua', 'Haochen']
for i in names:
    print(i, end = ' ')

for i in range(len(names)):
    print(names[i])
'''

#Indexing
'''
names = ['Eric','Mikel','Patrick', 'Fenghua', 'Haochen']
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
print(names)
names[0] = 'Bob'
print(names)
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
'''
names.append('Edward')
print(names)
'''
'''
print(names.index('Fenghua'))
'''
'''
names.insert(1 ,'Bob')
print(names)
'''
'''
names.sort()
print(names)
'''
'''
print(names)
names.remove('Mikel')
print(names)
'''
'''
print(names)
names.reverse()
print(names)
'''
'''
print(names)
del names[0]
print(names[0])
'''
'''
numbers = [5, 4, 20, 2, 30]
print(numbers)
print(max(numbers))
print(min(numbers))
'''
#Shallow copying vs. deep copying of lists
'''
list1 = [1, 2, 3, 4, 5]
list2 = list1
del list1[0]
print(list2)
'''
'''
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    list2.append(i)
'''

#Using a list as a parameter in a function
'''
list1 = [1, 2, 3, 4, 5]
list2 = []
for item in list1:
    list2.append(item)



def average(numbers):
    total = 0
    for i in numbers:
        total += i
    size = len(numbers)
    average = total / size
    print(average)
    
average(list1)
'''
#2 dimentional list
'''
list1 = [[1,10], [20,2], ['hello', 1]]
list1[0][0]
'''

   
#Tuples
'''
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[0])
'''
# built-in functions: len, min, max




