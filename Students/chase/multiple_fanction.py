def main():
    print(multiple(int(input("please enter the first number of the multiple:")),int(input("please enter the second number of the multiple:"))))
def multiple(number1,number2):
    if(number1==0):
        return 0
    return multiple(number1-1,number2)+number2
main()
