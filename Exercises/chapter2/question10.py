#author: Mikel Shifrin
#program that shows the ingredients to make cookies

#ask for number of cookies
quantity = int(input("Please enter the number of cookies you want to make: "))

#adjust recipe
ratio = quantity / 48
sugar = ratio * 1.5
butter = ratio * 1
flour = ratio * 2.75

#display results
print("\nA cookie recipe calls for the following ingredients",
      "\n", sugar, "cups of sugar\n", butter, "cup of butter\n",
      flour, "cups of flour", sep = " ", end = "")
