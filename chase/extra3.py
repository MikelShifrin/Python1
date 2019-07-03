def main():
    number_of_item=float(input("how many number of item do you want buy"))
    if(number_of_item<10):
        print(number_of_item*99)
    elif(number_of_item>=10 and number_of_item<=19):
        print(number_of_item*99*0.9)
    elif(number_of_item>=20 and number_of_item<=49):
        print(number_of_item*99*0.8)
    elif(number_of_item>=50 and number_of_item<=99):
        print(number_of_item*99*0.7)
    else:
        print(number_of_item*99*0.6)
main()
