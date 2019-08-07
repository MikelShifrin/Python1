def main():
    print('CALORIE CALCULATOR')
    Fat = int(input('How much fat have you eaten totay(in grams)?\n'))
    carb = int(input('How many carbs have you eaten today(in grams)?\n'))
    prot = int(input('How much protein have you eaten today(in grams)?\n'))
    a = fat(Fat)
    b = carbs(carb)
    c = protein(prot)
    total(a, b, c)
    
def fat(grams):
    cal_fat = grams * 9
    return cal_fat

def carbs(grams):
    cal_carb = grams * 4
    return cal_carb

def protein(grams):
    cal_prot = grams * 4
    return cal_prot
    
def total(fat, carbs, protein):
    Total = fat + carbs + protein
    print("You have acquired", fat,'calories from fat,',carbs,"calories from carbs ,",protein,"calories from protein for a total of",Total,"calories.")
    
main()
