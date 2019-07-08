#extra 4
#write a rectangle_area function
#area = length * width
#write it using void functions
#HINT:
#you will have 2 functions:
#main()
#rectangle_area(length, width)

def main ():
    l = float(input("Please enter a value in meters for the length\n"))
    w = float(input("Please enter a value in meters for the width\n"))
    rectangle_area(l, w)

def rectangle_area(length, width):
    area = length*width
    print("The total area has now been calculated in sqr.mtrs" , area)

main()
