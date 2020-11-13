from tkinter import *
root=Tk()
root.geometry("655x333")
def open():
	print(uservalue.get())
	print(passvalue.get())
user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid()
password.grid()
#Variables classes in Tkinter
#IntVar,BooleanVar,DoubleVar,StringVar
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
b=Button(root,text="Submit",command=open)
b.grid(row=2,column=1)
root.mainloop()