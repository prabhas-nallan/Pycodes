x=50
def show():
	global x#To modify global variable in local,if we want to make any variable as global , we use global keyword
	x=40
	p=3
	print(x,p)
show()
print("In main",x)
