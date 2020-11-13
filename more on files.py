f=open("tarun.txt")
#f.tell() tells about where is the file pointer 
f.seek(10)
print(f.tell())
print(f.readline())
#f.seek() reads the file from starting, when we give it , from where we give it to read
#f.seek(10)
#print(f.tell()) 
print(f.readline())
#print(f.tell())
print(f.readline())
f.close()