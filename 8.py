from tkinter import *
parent=Tk()
from tkinter import messagebox
def fun():
    messagebox.showinfo("11:53:35")
redbutton=Button(parent,text="Time",fg="red",command=fun)
redbutton.pack(side=TOP)
parent.mainloop()