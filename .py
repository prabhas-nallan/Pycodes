n=int(input("Enter the number of rows "))
num=int(input("Enter 0 or 1 "))
if num==1:
	for i in range(1,n+1):
		for j in range(i):
			print("*",end="")
		print()
elif num==0:
	for i in range(n):
		for j in range(n-i):
			print("*",end="")
		print()