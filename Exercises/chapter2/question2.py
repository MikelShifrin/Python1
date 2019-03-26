#author: Mikel Shifrin
#program that calculatess company's annual profit of 23%

#ask for projected amount of total sales
total = float(input("Please enter the company's projected amount"
                    +" of total sales:\n"))

#calculates the total annual profit
profit = total * 23 / 100

#display the result
print("The profit that will be made is",profit,"$", end = "", sep = " ")


