from tkinter import *

root = Tk()

OPTIONS=[
    "California",
    "458",
    "FF",
    "ENZO",
    "LaFerrari"
    ]

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

mainloop()
