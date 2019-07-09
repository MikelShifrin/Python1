def main():
    print(method(int(input("please enter the first number of the method:")),int(input("please enter the second number of the method:"))))
    
def method(number1,number2):
    if(number1==0):
        return 1
    return method(number1-1,number2)*number2
main()
