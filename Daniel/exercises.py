#exercice 1

#calories calculator. create 2 functions main, calories.
#It should calculate the amount of calories from 
#the grams of carbs, fat and protein.
#calories from fat = fat gram x 9
#calories from carbs = carbs gram x 4
#calories from protein = protein gram x 4

#example:
#if item has 1 gram of fat, 2 grams of protein and 
#3 grams of carbs
#1 x 9 + 2 x 4 + 3 x 4 = 29 calories total

#you will ask the user to enter fat, carbs and protein in main
#and calculate the total calories and print the answer 
#in calories function.

def main():
    fat = int(input("Please enter a number of grams of fat:\n"))
    carbs = int(input("Please enter a number of grams of carbs:\n"))
    protein = int(input("Please enter a number of grams of protein:\n"))
    calories(fat, carbs, protein)

def calories(fat, carbs, protein):
    total = fat * 9 + carbs * 4 + protein * 4
    print("The grams of fat, carbs and protein equal to ",total, "calories")

main()



#exercice 2

#feet to inches
#1 foot = 12 inches
#you will create a feet_to_inches function
#it will take a number of feet and convert it to inches
#you will ask the user to input the number of feet in 
#main() and print the number of inches in feet_to_inches(feet)
#HINT: 
#main()
#feet_to_inches(feet)

def main():
    feet = int(input("Please enter a number of feet:\n"))
    feet_to_inches(feet)

def feet_to_inches(feet):
    total = feet * 12
    print("The number of feet equal to",total,"inches")

main()


#exercice 3

#maximum of 2 numbers
#write a function that accepts 2 floats it should print which number is bigger
#you should ask the user to input the 2 numbers in main() and max(num1, num2)
#should print the answer
#HINT:
#main()
#max(num1, num2)

#Example: if both numbers are 1 and 2
#then answer is 2 is bigger than 1 

def main():
    num1 = int(input("Please enter a number:\n"))
    num2 = int(input("Please enter another number:\n"))
    max(num1, num2)

def max(num1, num2):
    if num1 > num2:
        print(num1,"is bigger than",num2)
    elif num2 > num1:
        print(num2,"is bigger than",num1)
    elif num1 == num2:
        print("the numbers are equal")

main()
