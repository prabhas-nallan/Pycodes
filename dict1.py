lst=[]
n=int(input("Enter the No. of keys "))
for i in range(n):
	x=(input("Enter the keys "))
	lst.append(x)
lst1=[]
for j in range(n):
	y=(input("Enter the values "))
	lst1.append(y)	
z=dict(zip(lst,lst1))
print(z)
for i in z:
	try:
		inp=(input("Enter the key you want "))
		print(z[inp])
	except:
		print("Invalid input")