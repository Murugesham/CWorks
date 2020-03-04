from tkinter import *
parent=Tk()
from tkinter import messagebox
def fun():
    messagebox.showinfo("Hello","red button clicked")
redbutton=Button(parent,text="Red",fg="red",command=fun)
redbutton.pack(side=LEFT)
greenbutton=Button(parent,text="Black",fg="black")
greenbutton.pack(side=RIGHT)
bluebutton=Button(parent,text="Blue",fg="blue")
bluebutton.pack(side=TOP)
blackbutton=Button(parent,text="Green",fg="red")
blackbutton.pack(side=BOTTOM)
parent.mainloop()
