#the 3 ways of printing in python
print('hello')
print("hello")
print("""hello""")

#String variables and literals
name = 'Mikel'
print(name)
print('Mikel')

#variables
#variable naming rules:
#1. needs to start with a uppercase letter, lowercase letter or underscore
#2. everything after can be a number, letter or underscore
age = 9
print(age)
age = 'hello'
print(age)

#The print function
name = 'Mikel'
age = 9
print("My name is:", name, "and I am", age, "years old.")
#escape characters
# \\     prints \
# \t     tab space
# \n     new line
# \'     prints '
# \"     prints "

print("I like", "Python")
print("I like", "Python", sep=" ", end="\n")
print("I like", "Python", sep="+", end="&&&&")
print("today")

#keyboard input
name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))

#performing calculations
# +    addition
# -    substraction 
# *    multiplication
# /    division
# //   integer division 
# %    remainder
# **   Exponent

#Average grade program
grade1 = float(input("enter grade 1:"))
grade2 = float(input("enter grade 2:"))
grade3 = float(input("enter grade 3:"))

average = ( grade1 + grade2 + grade3 ) / 3

print("Your average is", average)

#assignment 1
#write a program that shows the following:
#   1. your name
#   2. your age
#   3. your favorite color
#   4. your favorite animal
#
#Hello my name is Mikel.
#I am 22 years old.
#My favorite color is black.
#My favorite animal is the Jaguar.

#assignment 2
#write a program that calculates the total cost
#ask the user to input 3 prices
#calculate the subtotal
#add 15% tax
#calculate total
































