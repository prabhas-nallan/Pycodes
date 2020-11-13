n=int(input("Enter 1st number "))
n1=int(input("Enter 2nd number"))
op=input("Enter the operator from + - * / ")
if op=="+" and n==56 and n1==5:
	print("Sum 77")
elif op=="*" and n==45 and n1==3:
	print("Mul 100")
elif op=="/" and n==34 and n1==6:
	print("Div 10")
elif op=="-":
	print("Sub",n-n1)
elif op=="+":
	print("Sum",n+n1)
elif op=="*":
	print("Mul",n*n1)
elif op=="/":
	print("Div",n/n1)
else:
	print("Error!Check your input")

