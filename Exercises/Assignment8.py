#Assignment 8
#Using nested loops recreate the following pattern
#*******   (7)
#******    (6)
#*****     (5)
#****      (4)
#***       (3)
#**        (2)
#*         (1)
#Hint: for i in range(10,0,-1)

for row in range(10, 0, -1):
	print()
	for column in range(row):
		print("*", end = "")