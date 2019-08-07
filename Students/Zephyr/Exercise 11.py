def main():
    print('Grade Average calculator')
    gr1 = float(input('enter first grade:\n'))
    gr2 = float(input('enter second grade:\n'))
    gr3 = float(input('enter third grade:\n'))
    gr4 = float(input('enter fourth grade:\n'))
    gr5 = float(input('enter fifth grade:\n'))
    average_grade(gr1, gr2, gr3, gr4, gr5)

def average_grade(g1, g2, g3, g4, g5):
    average = ( g1 + g2 + g3 + g4 + g5 ) / 5
    print('Your average is:',average)
    
    if average > 90 and average <= 100:
        print("Your note is: A")
        
    elif average > 80 and average <= 90:
        print("Your note is: B")

    elif average > 70 and average <= 80:
        print("Your note is: C")

    elif average > 60 and average <= 70:
        print("Your note is: D")

    else:
        print("Your note is: F")

main()
