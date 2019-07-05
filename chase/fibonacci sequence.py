def main():
    print(fibonacci_sequence(1,1,int(input("please enter a position of fibonacci sequence:"))-2))
def fibonacci_sequence(number1,number2,position):
    if(position<=0):
        return number2
    return fibonacci_sequence(number2,number1+number2,position-1)
main()
