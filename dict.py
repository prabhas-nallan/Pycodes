#Dict
d1={'Epic':'Mahabharath',
		'Place':'Kurukskehtre',
		'Type':'War'}
print("Keys in dict are ...")
print('Epic')
print('Place')
print('Type')
print("NOTE:It is case sensitive")
for key in d1:
	try:
		n=input("Enter the key ")
		print(d1[n])
	except:
		print("Invalid Input")

