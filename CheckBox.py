from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("CheckBox in python")
root.geometry("500x500")

def show():
    my_label = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="check this box, I adore you ", variable=var, onvalue="pizza", offvalue="Hamburger ")
c.deselect()
c.pack()


myButton= Button(root, text="show selection", command=show).pack()

root.mainloop()