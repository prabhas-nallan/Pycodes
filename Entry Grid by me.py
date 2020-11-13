from tkinter import *
root=Tk()
root.title("My Details")
root.geometry("1000x1000")
def fetch():
	print(f"{namevar.get(),agevar.get(),mobilevar.get()}")
	with open("file.txt","a") as f:
		f.write(f"{namevar.get(),agevar.get(),mobilevar.get()}\n")
		
detail=Label(root,text="My Details",font="comicsansm 10 bold",pady=10)
name=Label(root,text="Name")
age=Label(root,text="Age")
mobile=Label(root,text="Mobile")
detail.grid()
name.grid()
age.grid()
mobile.grid()

namevar=StringVar()
agevar=StringVar()
mobilevar=StringVar()

nameinput=Entry(root,textvariable=namevar)
ageinput=Entry(root,textvariable=agevar)
mobileinput=Entry(root,textvariable=mobilevar)

nameinput.grid(row=1,column=1,pady=10)
ageinput.grid(row=2,column=1,pady=10)
mobileinput.grid(row=3,column=1,pady=10)

b=Button(root,text="Submit",command=fetch)
quit=Button(root,text="quit",command=quit)
b.grid(row=4,column=1,pady=10)
quit.grid(row=5,column=1,pady=10)

root.mainloop()