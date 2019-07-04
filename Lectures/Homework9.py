#Assignment 9
#write a km to miles converter
#Miles = KM x 0.6214
#write it using void functions
#HINT:
#you will have 2 functions:
#main():
#km_to_miles(km):


def main ():
    kilometers = float(input("Please enter a value for kilometers\n"))
    km_to_miles(kilometers)
                      
def km_to_miles(km):
    miles = km*0.6214
    print("The kilometers are now converted to " , miles )

main()

#extra 4
#write a rectangle_area function
#area = length * width
#write it using void functions
#HINT:
#you will have 2 functions:
#main()
#rectangle_area(length, width)

def main () :
    length = float(input("Please enter a value for the length\n"))
    rectangle_area(length)

def rectangle_area(witdh):
    area = length*width
    print("The total area has now been calculated" , area)
