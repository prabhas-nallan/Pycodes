# From Telolusko

#def add(a,*args,**kwargs):
	#c=a
	#print(a)
	#print(args)
	#for i in args:
#		c=c+i
#	return c
#print(add(5,6,7))


#From code with Harry

def print_tarun(*args,**kwargs):
	print(args)
	for i in args:
		print(i)
	for key,values in kwargs.items():
		print(key,values)

d={"Tarun":1,"P":2}
lst=["Tarun","Prabhas","Harsha","Sumanth",45,100,1000]
# If the argument is passed with * it shows out put with only tuple, and has index variation
print_tarun(*lst,**d)
# If If the argument is passed withou * it shows out put with only tuple with in list and has only index 0,and it shows the complete list
print_tarun(lst,d)


