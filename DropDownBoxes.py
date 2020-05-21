from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("DropDownBoxes in python")
root.geometry("500x500")

# Drop Down Boxes


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
         "Monday",
         "Thuesday",
         "Wensday",
         "Thursday",
         "friday",
         "Saturday"
 ]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="show selection", command=show).pack()

root.mainloop()