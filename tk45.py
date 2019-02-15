from tkinter import *

root = Tk()

def callback(event):
    print("点击位置:", event.x, event.y)#相对于应用程序左上角的位置

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.pack()

mainloop()
