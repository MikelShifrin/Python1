#Sets

#Creating a Set
'''
cards = set()

cards = set('jack')

cards = set(['jack', 'king', 'queen'])

cards = set(('jack', 'king', 'queen', 'jack'))

print(cards)
'''
#Getting the Number of Elements in a Set
'''
cards = set(('jack', 'king', 'queen', 'jack'))
print(len(cards))
'''
#Adding and Removing Elements in a Set
'''
cards = set()
cards.add('jack')
cards.add('queen')
cards.update(['king', 'ace'])
print(cards)

cards.remove('jack')
#discard doesn't give exception if element doesn't exist 
cards.discard('3')
'''
#Using the for Loop to Iterate over a Set
'''
cards = set(('jack', 'king', 'queen', 'jack', 'ace'))
for i in cards:
    print(i)
'''
#Using the in and not in Operators to test for a Value in a Set
'''
cards = set(('jack', 'king', 'queen', 'jack', 'ace'))
if 'king' not in cards:
    print('I have the king')
else:
    print('You have him')
'''
#Finding the Union of Sets
'''
set1 = set(['jack', 'king', 'queen', 'jack', 'ace'])
set2 = set(['one', 'two', 'three'])
set3 = set1.union(set2)
print(set3)
set3 = set1 | set2
print(set3)
'''
#Finding the Intersection of Sets
'''
set1 = set(['jack', 'king', 'queen', 'jack', 'ace'])
set2 = set(['one', 'two', 'three', 'queen'])
set3 = set1.intersection(set2)
print(set3)
set3 = set1 & set2
print(set3)
'''
#Finding the Difference of Sets
'''
set1 = set(['jack', 'king', 'queen', 'jack', 'ace'])
set2 = set(['one', 'two', 'three', 'queen'])
set3 = set1.difference(set2)
print(set3)
set3 = set1 - set2
print(set3)
'''
#Finding the Symmetric Difference of Sets
'''
set1 = set(['jack', 'king', 'queen', 'jack', 'ace'])
set2 = set(['one', 'two', 'three', 'queen'])
set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1 ^ set2
print(set3)
'''
#Finding Subsets and Supersets
'''
set1 = set(['jack', 'king', 'queen', 'jack', 'ace'])
set2 = set(['ace', 'queen'])
result1 = set1.issubset(set2)
result1 = set1 <= set2          #same as previous line
result2 = set1.issuperset(set2)
result2 = set1 >= set2          #same as previous line
print(result1)
print(result2)
'''


