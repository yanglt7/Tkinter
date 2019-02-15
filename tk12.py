from tkinter import *

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

textLabel1 = Label(frame1, text="作品:", justify=LEFT)
textLabel1.pack(side=LEFT)

textLabel2 = Label(frame2, text="作者:", justify=LEFT)
textLabel2.pack(side=LEFT)

e1 = Entry(frame1)
e1.pack(padx=10, pady=10)
e1.delete(0, END)
e1.insert(0, "零基础入门学习 Python")

e2 = Entry(frame2)
e2.pack(padx=10, pady=10)
e2.delete(0, END)
e2.insert(0, "小甲鱼")

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

opts = [("获取信息", 1), ("退出", 2)]

v = IntVar()

for opt, num in opts:
    b = Radiobutton(root, text=opt, variable=v, value=num, indicatoron=False)
    b.pack(side=LEFT, padx=20)

mainloop()
