def main():
    width1=float(input("please enter the width of first rectangle"))
    lenth1=float(input("please enter the lenth of first rectangle"))
    area1=area(width1,lenth1)
    width2=float(input("please enter the width of first rectangle"))
    lenth2=float(input("please enter the lenth of first rectangle"))
    area2=area(width2,lenth2)
    print(area1)
    print(area2)
    if(area1>area2):
        print("rectangle1 is bigger")
    elif(area1<area2):
        print("rectangle2 is bigger")
    else:
        print("rectangle1 is same with rectangle2")
def area(width, lenth):
    area=width*lenth
    return area
main()
