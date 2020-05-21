from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")


def popup():
    response = messagebox.showerror("THis is my popup", "Hello world")
    Label(root, text=response).pack()
    if response == "yes":
         Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()


Button(root, text="popup", command=popup).pack()

root.mainloop()
