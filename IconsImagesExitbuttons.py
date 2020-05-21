from tkinter import *

from PIL import ImageTk, Image
root = Tk()
root.title("Learn to code at codemy.com")
root.iconbitmap('images\sibe.png')

my_img = ImageTk.PhotoImage(Image.open("images\sibe.png"))
my_lable = Label(image=my_img)
my_lable.pack()







button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()








root.mainloop()