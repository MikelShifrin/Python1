import errorhandling
def main():
    number=errorhandling.number_error_handling(input("Please enter a positive integer:"))
    while number<=0:    
        number=errorhandling.number_error_handling(input("Please enter a positive integer:"))
    print_1_to_n(number)
def print_1_to_n(n):
    return print_1_to_n(n-1)
main()
