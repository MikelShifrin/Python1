#assignment 3
#ask user to enter a number between 1-7
# 1. Sunday
# 2. Monday
# 3. Tuesday
# 4. Wednesday
# 5. Thursday
# 6. Friday
# 7. Saturday

number = int(input("Please enter a number between 1-7:\n"))

if number == 1:
	print("Sunday")
elif number == 2:
	print("Monday")
elif number == 3:
	print("Tuesday")
elif number == 4:
	print("Wednesday")
elif number == 5:
	print("Thursday")
elif number == 6:
	print("Friday")
elif number == 7:
	print("Saturday")
else:
	print("Error")