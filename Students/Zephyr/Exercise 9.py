def main():
    kiloM = float(input('please enter a number of kilometers to convert it in to miles\n'))
    km_to_miles(kiloM)

def km_to_miles(km):
    miles = km * 0.6214
    print(km,'Km is equal to',miles, 'Miles.')

main()
