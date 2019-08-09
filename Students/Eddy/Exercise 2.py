    
#assignment 2
#write a program that calculates the total cost
#ask the user to input 3 prices
#calculate the subtotal
#add 15% tax
#calculate total

pri1 = float(input("Please input 3 prices:\n"))
pri2 = float(input("\n"))
pri3 = float(input("\n"))
sub = pri1 + pri2 + pri3
tax = sub/100*15
total = sub + tax

print("Your subtotal is",sub, "dollars")
print("The 15% tax is",tax, "dollars")
print("Your total is", total, "dollars")


