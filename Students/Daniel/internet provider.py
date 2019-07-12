#Package A: 9.95$/month 10 hours +2.00$/hour
#Package B: 12.95$/month 20 hours +1.00$/hour
#Package C: 19.95$/month unlimited

def main():
    package = input("Please enter your package(A, B or C):\n")
    hours = int(input("Please enter the number of hours you use:\n"))
    total = 0
    package_a = 9.95
    package_b = 12.95
    package_c = 19.95
        
    if hours > 10:
        total = hours - 10
        extra = total * 2
        package_a = 9.95 + extra
        
    elif hours > 20:
        total = hours - 20
        extra = total
        package_b = 12.95 + extra
        #print("You need to pay", grand_total,"$")

    if package == "A":
        print("You need to pay", package_a,"$")
        if package_b < package_a:
            print("Package B would've been cheaper")
        if package_c < package_a:
            print("Package C would've been cheaper")


    if package == "B":
        print("You need to pay", package_b,"$")
        if package_a < package_b:
            print("Package A would've been cheaper")
        if package_c < package_b:
            print("Package C would've been cheaper")

    if package == "C":
        print("You need to pay", package_c,"$")
        if package_a < package_c:
            print("Package A would've been cheaper")
        if package_b < package_c:
            print("Package B would've been cheaper")




        







main()
