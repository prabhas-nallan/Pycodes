#x=50
#def show():
	#global x#To modify global variable in local,if we want to make any variable as global , we use global keyword
	#x=40
	#p=3
	#print(x,p)
#show()
#print("In main",x)


x=100
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)
