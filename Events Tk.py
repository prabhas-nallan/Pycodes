from tkinter import *
root=Tk()
def tarun(event):
	print(f"you clicked at {event.x},{event.y}")
root.title("Events in Tkinter")
root.geometry("644x344")
widget=Button(root,text="click me please")
widget.pack()
widget.bind("<Button-1>",tarun)
widget.bind("Double-1",quit)
root.mainloop()