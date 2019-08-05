
Price_1 = float(input("enter the first price:\n"))
Price_2 = float(input("enter the second price:\n"))
Price_3 = float(input("enter the third price:\n"))

subtotal = ( Price_1 + Price_2 + Price_3 )
taxe = ( subtotal * 0.15 )
total = ( subtotal + taxe )

print("The total cost is:" , total, "$.")
