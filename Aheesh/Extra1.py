length1=float(input("enter length of rectangle1\n"))
width1=float(input("enter width of rectangle1\n"))
area1=length1*width1
print(area1)

length2=float(input("enter length of rectangle2\n"))
width2=float(input("enter width of rectangle2\n"))
area2=length2*width2
print(area2)

if area1 > area2:
    print("area of rectangle1 is bigger than area of rectangle2")
elif area1 < area2 :
    print("area of rectangle2 is bigger than area of rectangle1")
if area1 == area2 :
    print ("area of rectangle1 and area of rectangle2 are equal")
