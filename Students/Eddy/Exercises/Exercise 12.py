#Assignment 10
#Calorie calculator
#calories from carbs = carb grams x 4
#calories from fat = fat grams x 9
#calories from protein = protein x 4
#total calories
#HINT:
#main():
#fat(grams):
#carbs(grams):
#protein(grams):
#total(fat, carbs, protein):



def main():
    print('Calorie Calculator')
    
    fats = float(input('Enter the amount of fat you want to calculate:\n'))
    cal1 = fat(fats)
    carbss = float(input('Enter the amount of carbs you want to calculate:\n'))
    cal2 = carbs(carbss)
    proteins = float(input('Enter the amount of carbs you want to calculate:\n'))
    cal3 = protein(proteins)
    total1 = total(cal1, cal2, cal3)
    print('Your total of calories is', total1)

def fat(g):
    cal1 = g * 9
    return cal1

def carbs(g):
    cal2 = g * 4
    return cal2

def protein(g):
    cal3 = g * 4
    return cal3

def total(fat, carbs, protein):
    total1 = (fat + carbs + protein)
    return total1
   

main()

