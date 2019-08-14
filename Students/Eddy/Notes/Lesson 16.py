#Files part 2

#Binary Files and Serializing Objects
import pickle

#Writing objects to File
'''
cards = ['jack', 'queen', 'king', 'ace']

outputfile = open('C:/Users/mikis/Desktop/cards.dat', 'wb')

pickle.dump(cards, outputfile)
outputfile.close()
'''
#Reading objects from File
'''
inputfile = open('C:/Users/mikis/Desktop/cards.dat', 'rb')

a = pickle.load(inputfile)
print(a)
'''
