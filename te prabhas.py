try:
	x=int(input('Enter a number '))
	r=x%2
	if(r==0):
		print('Even')
	else:
		print('Odd')
except:
	print('Invalid')