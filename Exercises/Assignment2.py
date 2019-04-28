#assignment 2
#write a program that calculates the total cost
#ask the user to input 3 prices
#calculate the subtotal
#add 15% tax
#calculate total

item1 = float(input("Please enter your 1st item's price:\n"))
item2 = float(input("Please enter your 2nd item's price:\n"))
item3 = float(input("Please enter your 3rd item's price:\n"))

subtotal = item1 + item2 + item3
tax = subtotal * 15/100
total = subtotal + tax

print("\nYOUR BILL")
print("______________________________")
print("subtotal:",subtotal)
print("tax:     ",tax)
print("______________________________")
print("total:   ",total)
