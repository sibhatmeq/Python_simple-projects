from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Adding frames")

r =IntVar()
r.set("2")


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Cheese")
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()

# my_label = Label(root, text=pizza.get())
# my_label.pack()

myButton =Button(root, text="click me", command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()