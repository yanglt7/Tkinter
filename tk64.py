from tkinter import *

import tkinter.filedialog as filedialog

root =Tk()

def callback():
    #fileName = filedialog.askopenfilename(defaultextension=".py")#默认后缀
    fileName = filedialog.askopenfilename(filetypes=[("PNG", ".png"), ("GIF", ".gif"), ("JPG", ".jpg"), ("Python", ".py")])
    #fileName = filedialog.askopenfilename()
    print(fileName)

Button(root, text="打开文件", command=callback).pack()

mainloop()
