#Ingredient Adjuster

#A cookie recipe calls for the following ingredients:
# - 1.5 cups of sugar
# - 1 cup of butter
# - 2.75 cups of flour
#this recipe makes 48 cookies
#
#write a program that asks how many cookies they
#want to make, then display the number of cups
#needed for each ingredient to make the specified
#number of cookies

cookie = float(input("How many cookies do you want?\n"))
x = (cookie / 48)
sugar = float(1.5 * x)
butter = float(1 * x)
flour = float(2.75 * x)

print("Your ingredients are" ,sugar, "cups of sugar", butter, "cups of butter", flour, "cups of flour.")

                                
