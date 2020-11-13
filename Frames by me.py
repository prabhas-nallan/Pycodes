from tkinter import *
root=Tk()
f1=Frame(root,bg="green",borderwidth=6,relief=SUNKEN)
f1.pack(side=RIGHT,fill=Y)
f2=Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
f2.pack(side=LEFT,fill=Y)
#ex='''Iam tryna do Tkinter, but my mind stops\n working while doing it\n. I dont know how to process my brain\n.I gotta find a way to stop it'''
lab=Label(f1,text="Welcome",padx=150,pady=100)
lab.pack()
lab2=Label(f2,text="Hello",padx=150)
lab2.pack()
root.mainloop()