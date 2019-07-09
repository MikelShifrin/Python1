#Assignment 11
#Test Average and Letter Grade
#ask for 5 grades
#calculate and display the average
#display letter grade
#90 -100  A
#80 - 89  B
#70 - 79  C
#60 - 69  D
#Below 60 F

def main():
    grade1 = float(input("Please enter your score for grade 1:\n"))
    grade2 = float(input("Please enter your score for grade 2:\n"))
    grade3 = float(input("Please enter your score for grade 3:\n"))
    grade4 = float(input("Please enter your score for grade 4:\n"))
    grade5 = float(input("Please enter your score for grade 5:\n"))

    average(grade)
    letter_grade(grade)
    
def average(grade):
    average = grade1 + grade2 + grade3 + grade4 + grade5
    return average

def letter_grade(grade):
    if average < 100 and averege > 90:
        print("A")
    elif average < 89 and average > 80:
        print("B")
    elif average < 79 and average > 70:
        print("C")
    elif average < 69 and average > 60:
        print("D")
    else:
        print("F")

main()
