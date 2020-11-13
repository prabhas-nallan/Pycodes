f=open("tarun.txt","rt")
print(f.readlines())
#print(f.readline(),end="")
#print(f.readline(),end="")
#print(f.readline())
#When ever I use f.read() it becomes empty and I cant iterate
#content=f.read()
#To read character by char
#for lines in content:
	#print(lines)
#print(content)
#for line in f:
	#print(line,end="")
#It gives us the 1st no. of characters
#content=f.read(3)
#print("1",content)
#If we rewrite it again it gives the next No. of characters
#content=f.read(3)
#print("2",content)
f.close()