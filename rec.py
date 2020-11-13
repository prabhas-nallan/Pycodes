def fac(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
print(fac(6))

def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
print(fact(5))


