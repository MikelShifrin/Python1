day=int(input("Please enter a date:\n"))
month=int(input("Please enter a month:\n"))
year= int(input("Please enter a year:\n"))

magic1 = day * month
magic2 = year % 100

if magic2 == magic1 :
    print("This is a magic date")
else:
    print("This is not a magic date")
*to Revise
