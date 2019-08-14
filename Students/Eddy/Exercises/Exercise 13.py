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

while True:
    def main():
        grade1 = float(input('Please enter 5 grades:\n'))
        grade2 = float(input('\n'))
        grade3 = float(input('\n'))
        grade4 = float(input('\n'))
        grade5 = float(input('\n'))
        average = avg(grade1, grade2, grade3, grade4, grade5)
        print('Your average is:', average)
        let = letter(average)
        if let == 'A':
            print('S, Fantastic!')
    
        elif let == 'B':
            print('A, Great Job!')
    
        elif let == 'C':
            print('B, Good Work!')
    
        elif let == 'D':
            print('C, OK')
    
        elif let == 'E':
            print('D, Study More (Play less Fortnite)')
    
        elif let == 'F':
            print('F, You Failed!')
    
        elif let == 'G':
            print('F-, Complete Failure! DISASTER')

        elif let == 'H':
            print('I think sombody forgot their brain at home...')

        input('\n----------------------Press Eneter to Restart the Program----------------------')
        
    
    def avg(grade1, grade2, grade3, grade4, grade5):
        average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
        return average

    def letter(grade):
        if grade == 100:
            return 'A'
        
        elif grade < 100 and grade > 90:
            return 'B'
        
        elif grade < 90 and grade > 80:
            return 'C'
        
        elif grade < 80 and grade > 70:
            return 'D'
        
        elif grade < 70 and grade > 60:
            return 'E'
        
        elif grade < 60 and grade > 0:
            return 'F'

        elif grade == 0:
            return 'G'
            
        else:
            return 'H'
               
    
    main()
