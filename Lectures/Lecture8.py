#Functions writing your own modules
'''
import Lecture8Module as car

print(car.interior_color())
'''

#Files
#read access              'r'
#write access             'w'
#write access with append 'a'

#open(String filename, String access type)
'''
outputfile = open('C:/Users/mikis/Desktop/random1.txt', 'a')
for i in range(10):
    outputfile.write("Hello my name is mikel\n")
outputfile.close()
'''
'''
inputfile = open('C:/Users/mikis/Desktop/random1.txt', 'r')
#file_contents = inputfile.read()
#print(file_contents)

file_contents = inputfile.readline()

while file_contents != '':
    print(file_contents)
    file_contents = inputfile.readline()

inputfile.close()
'''

#Assignment 12
#create 2 files on Desktop:
#input.txt
#output.txt
#inside input.txt write the following lines:
#apple
#orange
#banana
#cucumber
#Your program will add an s to each line
#and write it to output.txt
#Hint: name = 'hello\n'
#      name.rstrip('\n')

