#Introduction to Functions

#Rules for naming functions:
#1. cannot be a key word
#2. cannot contain spaces
#3. first character can be _ or English alphabet
#4. the rest can be _ or English alphabet or any arabic number

#Void Functions
'''   
def message():
    print('hello')
    print('my friend')
    for count in range(10):
        print(count)

message()
message()
message()
'''
#The main function
'''
def main():
    names()
    
def names():
    full_name = input("Please enter your full name:\n")
    print("Welcome to my program", full_name)
    
main()
'''
#Local variables
#variables created inside functions only exist
#inside those functions
'''
def main():
    person = 'Mikel'
    name()
    print(person)
    
def name():
    person = 'Patrick'
    print(person)
    
main()
'''
#Passing arguments to functions
'''
def main():
    reply = input('Please enter your favorite planet:\n')
    planet(reply) #reply is an argument
    planet('Earth')
    planet('Saturn')
    planet('Jupiter')
    a = 'Mars'
    planet(a)

#answer is a parameter
def planet(answer):
    print(answer)
    
main()
'''
#Passing multiple arguments
'''
def main():
    nb1 = float(input('enter a number:\n'))
    nb2 = float(input('enter a number:\n'))
    sum(nb1, nb2) #nb1 and nb2 are arguments
    
def sum(num1, num2): #num1 and num2 are parameters
    result = num1 + num2
    print(result)

main()
'''
#Keyword arguments
'''
def main():
    nb1 = float(input('enter a number:\n'))
    nb2 = float(input('enter a number:\n'))
    sum(num2=nb1, num1=nb2) #nb1 and nb2 are arguments
    
def sum(num1, num2): #num1 and num2 are parameters
    result = num1 + num2
    print(result)

main()
'''
#Global variables
#Only use globals as constants (if absolutely neccessary) 
#Contants are in all uppercases by conversion
#this example is bad practice do not reproduce
'''
PERSON = 'Mikel'

def main():
    name()
    print(PERSON)
    
def name():
    global PERSON
    PERSON = 'Patrick'
    print(PERSON)
          
main()
'''
#Assignment 9
#write a km to miles converter
#Miles = KM x 0.6214
#write it using void functions
#HINT:
#you will have 2 functions:
#main():
#km_to_miles(km):



















