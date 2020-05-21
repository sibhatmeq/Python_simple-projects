from tkinter import  *

root =Tk()
#Creating a Label widget
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="my name is Sibhat Mequanint!")

#shoving in to screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()