try:
	age=int(input("Enter your age "))
	if age>18 and age<=100:
		print("You can drive")
	elif age==18:
		print("We will  think about it ")
	elif age<18:
		print("You cannot drive")
	else:
		print("Not possible")
except:
	print("Invalid input ")