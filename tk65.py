from tkinter import *

import tkinter.colorchooser as colorchooser

root =Tk()

def callback():
    fileName = colorchooser.askcolor()
    print(fileName)

Button(root, text="选择颜色", command=callback).pack()

mainloop()
