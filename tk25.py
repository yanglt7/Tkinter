from tkinter import *

root = Tk()

text = Text(root, width=50, height=30)
text.pack()

photo = PhotoImage(file="bg.gif")

def show():
    text.image_create(END, image=photo)

b1 = Button(text, text="点我点我", command=show)
text.window_create(INSERT, window=b1)

mainloop()
