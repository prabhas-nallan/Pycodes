a=100
def show(*args):
	return args

def add(*a):
	sum=0
	for i in a:
		sum=sum+i
	return sum

print(show(1,100))