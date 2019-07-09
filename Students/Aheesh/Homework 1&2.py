#Homework1

#Write a program that asks and shows
#the following from the user


# 1. Your name
# 2. Your age
# 3. Your favorite color
# 4. Your favorite animal
#
#Hello my name is Michael.
#I am 22 years old.
#My favorite color is black.
#My favorite animal is the Jaguar.



name= input("please enter your name:\n")
age= int(input("please enter your age:\n"))
color= input("please enter your color:\n")
animal= input("please enter your animal:\n")

print('Hello',"My name is",name,".")
print("I am",age,"years old.")
print("My favorite color is",color,".")
print("My favorite animal is the",animal,".")

#Homework2
#Write a program that calculates the total cost.
#Ask the user to input 3 prices
#Calculate the Subtotal
#Add 15% Tax
#Calculate Total

price1= int(input("please enter your price1:\n"))
price2= int(input("please enter your price2:\n"))
price3= int(input("please enter your price3:\n"))

subtotal = price1 + price2 + price3
tax = subtotal * 15/100
total = tax + subtotal

print(subtotal)
print(tax)
print(total)
    
