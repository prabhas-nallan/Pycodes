import random
print("Game : Rock Paper Scissor\n")
print("You got 10 chances\n")
c=0
h=0

for i in range(1,11):
	lst=["Rock","Paper","Scissor"]
	rand=random.choice(lst)
	userinp=input("Enter Rock , Paper or Scissor  ")
	if userinp==rand:
		print("Tie")
	elif userinp=="Rock" and rand=="Paper":
		c=c+1
		print("You lose")
	elif userinp=="Rock" and rand=="Scissor":
		h=h+1
		print("You win")
	elif userinp=="Paper" and rand=="Scissor":
		c=c+1
		print("You lose")
	elif userinp=="Paper" and rand=="Rock":
		h=h+1
		print("You win")
	elif userinp=="Scissor" and rand=="Rock":
		c=c+1
		print("You lose")
	elif userinp=="Scissor" and rand=="Paper":
		h=h+1
		print("You win")
	else:
		print("Invalid input")

if i==10:
	print("\nGame over")

tie_p=i-(h+c)
print(f"Your score is {h}")
print(f"Computer score is {c}")
print(f"Tied {tie_p}")
if c>h:
	print("\nYou lost the game")
else:
	print("\nYou won the game")
