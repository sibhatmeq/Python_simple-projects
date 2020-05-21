from tkinter import *

root = Tk()

e = Entry(root, width=30, borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name!", command=myClick, fg="blue", bg="#000000")
myButton.pack()

root.mainloop()
