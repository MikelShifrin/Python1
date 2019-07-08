#assignement 2
#write a program that calculates the total cost
#ask the user to input 3 prices
#calculate the subtotal
#add 15% tax
#calculate total


price1 = float(input("enter price 1:"))
price2 = float(input("enter price 2:"))
price3 = float(input("enter price 3:"))

total = ( price1 + price2 + price3 ) * 1.15

print("Your total is ", total)
