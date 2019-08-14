#Assignment 9
#write a km to miles converter
#Miles = KM x 0.6214
#write it using void functions
#HINT:
#you will have 2 functions:
#main():
#km_to_miles(km):

def main():
    km = float(input("Enter a number (km) and it'll be converted in to miles\n"))
    km_to_miles(km)

def km_to_miles(km):
    miles = km * 0.6214
    print(miles)
    
main()
