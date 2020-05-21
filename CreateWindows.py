from tkinter import *
from PIL import ImageTk, Image

from tkinter import messagebox

root = Tk()
root.title("Creating a new Windows")


def open():
    global my_img
    top = Toplevel()
    lbl = Label(top, text="Hello world", ).pack()
    my_img = ImageTk.PhotoImage(Image.open("images\sibe1.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second window", command=open).pack()


root.mainloop()
