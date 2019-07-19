#Assignment 10
#Calorie calculator
#calories from carbs = carb grams x 4
#calories from fat = fat grams x 9
#calories from protein = protein x 4
#total calories
#HINT:
#main():
#carbs(grams):
#protein(grams):
#total(fat, carbs, protein):

def main():
    grams_carbs = int(input("Please enter a number of grams of carbs:\n"))
    grams_fat = int(input("Please enter a number of grams of fat:\n"))
    grams_protein = int(input("Please enter a number of grams of protein:\n"))
    
    calories_carbs = carbs(grams_carbs)
    calories_fat = fat(grams_fat)
    calories_protein = protein(grams_protein)
    calories_total = total(calories_carbs, calories_fat, calories_protein)
    
    print("You have",calories_carbs,"calories in the carbs")
    print("You have",calories_fat,"calories in the fat")
    print("You have",calories_protein,"calories in the protein")
    print("The total calories equal to",calories_total)
    
def carbs(grams):
    total_carbs = grams * 4
    return total_carbs

def fat(grams):
    total_fat = grams * 9
    return total_fat

def protein(grams):
    total_protein = grams * 4
    return total_protein

def total(carbs, fat, protein):
    total = carbs + fat + protein
    return total

main()
