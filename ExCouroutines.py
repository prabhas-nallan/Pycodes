import time
def Searcher2():
    time.sleep(3)
    f=open("myfile.txt")
    read=f.read()

    while True:
        text=(yield)
        if text in read:
            print("Text found")
        else:
            print("Not found")
search2=Searcher2()
inp=input("Enter the text ")
print("Search started")
next(search2)
search2.send(inp)
inp=input("Enter the text ")
search2.send(inp)
inp=input("Enter the text ")
search2.send(inp)
inp=input("Enter the text ")
search2.send(inp)
search2.close()