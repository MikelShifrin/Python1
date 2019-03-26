#author: Mikel Shifrin
#program asks for price of 5 items then calculates total with 7% sales tax

#welcome message
print("Welcome to my receipt calculator:\n")

#get price of 5 items
item_1 = float(input("Please enter price of item 1: "))
item_2 = float(input("Please enter price of item 2: "))
item_3 = float(input("Please enter price of item 3: "))
item_4 = float(input("Please enter price of item 4: "))
item_5 = float(input("Please enter price of item 5: "))

#perform all calculations
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = subtotal * 7 / 100
total = subtotal + sales_tax

#display result
print("\nsubtotal: ", subtotal,"\nsales tax: ",sales_tax,
      "\n__________", "\ntotal", total, end = "", sep = " ")
