
#Exercise 1: Personal Information
'''
Write a program that displays the following information:

1. Your name
2. Your address, with city, province, and ZIP
3. Your phone number
4. Your school name
'''

name= input("please enter your name:\n")
address= int(input("please enter your address:\n"))
phone_number = int(input("please enter your phone number:\n"))
school= input("please enter your school:\n")

print("My name is", name,".")
print("I live in",address,".")
print("My number is",phone_number,".")
print("My school is",school,".")


#Exercise 2: Total purchase
'''
A customer in store is purchasing 5 items. Write a program
that asks the user for the price of each item, then displays
the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 7%.
'''
price1=float(input("Please enter your price1:\n"))
price2=float(input("Please enter your price2:\n"))
price3=float(input("Please enter your price3:\n"))
price4=float(input("Please enter your price4:\n"))
price5=float(input("Please enter your price5:\n"))
subtotal= price1+price2+price3+price4+price5
tax=subtotal*7/100
total=tax+subtotal
print(subtotal)
print(tax)
print(total)



#Exercise 3: Distance Traveled
'''
Assuming there are no accident delays, the distance that a car
travels down the interstate can be calculated with the following
formula:

Distance = Speed x Time

A car is travelling at 70 miles per hour.
Write a program that displays the following:
1. The distance the car will travel in 6 hours.
2. The distance the car will travel in 10 hours.
3. The distance the car will travel in 15 hours.
'''
def main():
    miles6h = 70*6
    print("The miles are calculated for 6 hours")
    print(miles6h)
    miles10h=70*10
    print("The miles are calculated for 10 hours")
    print(miles10h)
    miles15h=70*15
    print("The miles are calculated for 15 hours")
    print(miles15h)
    
    

main()
