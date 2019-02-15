from tkinter import *

root = Tk()

variable = StringVar()
variable.set("one")

w = OptionMenu(root, variable, "one", "two", "three")
w.pack()

def callback():
    print(variable.get())

Button(root, text="点我", command=callback).pack()

mainloop()
