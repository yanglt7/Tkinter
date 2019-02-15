from tkinter import *

root = Tk()

theLB = Listbox(root, selectmode=EXTENDED, height=11)
theLB.pack()

for item  in range(11):
    theLB.insert(END, item)

mainloop()
