guessnum=18
chances=5
print("You got 5 chances")
try:
	for i in range(chances):
		inp=int(input("Enter a number "))
		if inp>=5 and inp<=10:
			print("You are far")
		elif inp>=6 and inp<=10:
			print("You got little better ")
		elif inp>=11 and inp<= 15:
			print("You got better")
		elif inp==guessnum:
			print("Congratulations!! You won the game ")
			break
		elif inp>=16 and inp<=20:
			print("You got it almost ")
		else:
			print("You are away from number")
		
except:
	print("Invalid input")

print("You are left with",chances-i-1,"chances\nGame over!")

print("Visit again!")

