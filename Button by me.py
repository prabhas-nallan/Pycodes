from tkinter import *
root=Tk()
root.geometry("233x100")
def hello():
	print("hello")
f=Frame(root,bg="green",borderwidth=6)
f.pack(side=LEFT,anchor="nw")
b=Button(f,text="Click Here",fg="red",command=hello)
b.pack()
root.mainloop()