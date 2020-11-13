#f=open("tarun2.txt","w")
#To know the No. of chars you wrote just assign variable to it and print it
#a=f.write("Tarun you are good\n")
#print(a)
#f.close()

#Handel read and write both

f=open("tarun2.txt","r+")
print(f.read())
f.write("bye")