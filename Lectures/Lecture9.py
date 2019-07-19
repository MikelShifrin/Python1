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
'''
inputfile = open('C:/Users/mikis/Desktop/random1.txt', 'r')
for line in inputfile:
    print(line)

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

#Assignment 13
#
#Personal Web Page Generator
#
#Write a program that asks the user for their name, then asks the user to enter
#a sentence that describes themself.
#Ex:
#Enter your name: Mikel Shifrin
#Describe yourself: Just a boring programming teacher.
#
#Once the user has entered the input, the program should create an HTML file
#(example: site.html), containing the input, for a simple Web page.
#Example with sample input
'''
<html>
    <head>
    </head>
    <body>
        <center>
            <h1>Mikel Shifrin</h1>
        </center>
        <hr />
        Just a boring programming teacher.
        <hr />
    </body>
</html>
'''


