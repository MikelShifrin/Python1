cal_type = input("Enter: + (addition) or * (multiplication) or / (division) or - (substraction)\n")

if  cal_type == '+':
    num1 = float(input("Enter the first number\n"))
    num2 = float(input("Enter the second number\n"))
    num3 = (num1 + num2)
    print("The total is:", num3,)

elif cal_type == '*':
    num1 = float(input("Enter the first number\n"))
    num2 = float(input("Enter the second number\n"))
    num3 = (num1 * num2)
    print("The total is:", num3,)

elif cal_type == '/':
    num1 = float(input("Enter the first number\n"))
    num2 = float(input("Enter the second number\n"))
    num3 = (num1 / num2)
    print("The total is:", num3,)

elif cal_type == '-':
    num1 = float(input("Enter the first number\n"))
    num2 = float(input("Enter the second number\n"))
    num3 = (num1 - num2)
    print("The total is:", num3,)

else:
    while cal_type != '+' and cal_type != '*' and cal_type != '/' and cal_type != '-':
        cal_type = input("Enter: + (addition) or * (multiplication) or / (division) or - (substraction)\n")
    if  cal_type == '+':
        num1 = float(input("Enter the first number\n"))
        num2 = float(input("Enter the second number\n"))
        num3 = (num1 + num2)
        print("The total is:", num3,)

    elif cal_type == '*':
        num1 = float(input("Enter the first number\n"))
        num2 = float(input("Enter the second number\n"))
        num3 = (num1 * num2)
        print("The total is:", num3,)
    
    elif cal_type == '/':
        num1 = float(input("Enter the first number\n"))
        num2 = float(input("Enter the second number\n"))
        num3 = (num1 / num2)
        print("The total is:", num3,)

    elif cal_type == '-':
        num1 = float(input("Enter the first number\n"))
        num2 = float(input("Enter the second number\n"))
        num3 = (num1 - num2)
        print("The total is:", num3,)
