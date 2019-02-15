from tkinter import *

root = Tk()

photo = PhotoImage(file="bg.gif")
theLabel = Label(root,
                          text="学 Python 到 FishC！",
                          justify=LEFT,
                          image=photo,
                          compound=CENTER,
                          font=("微软雅黑", 20),
                          fg="green")
theLabel.pack()

mainloop()

