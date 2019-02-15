from tkinter import *

root = Tk()

w = Canvas(root, width=400, height=600)
w.pack()

#一个圆
w.create_oval(100, 30, 300, 230, fill="DodgerBlue")

#一个圆
w.create_oval(120, 80, 280, 230, fill="white")

#两个椭圆
w.create_oval(200, 50, 250, 110, fill="white")
w.create_oval(150, 50, 200, 110, fill="white")

#两个椭圆
w.create_oval(178, 73, 190, 95, fill="black")
w.create_oval(210, 73, 222, 95, fill="black")

#两个椭圆
w.create_oval(182, 79, 186, 89, fill="white")
w.create_oval(214, 79, 218, 89, fill="white")

#一个圆
w.create_oval(192, 96, 208, 112, fill="red")

#一条直线
w.create_line(200, 112, 200, 180)

#一条弧线 
w.create_arc(170, 150, 230, 180, start=190, extent=160, style=ARC)

#六条直线
w.create_line(140, 140, 190, 140)
w.create_line(210, 140, 260, 140)

w.create_line(145, 115, 190, 130)
w.create_line(210, 130, 255, 115)

w.create_line(140, 165, 190, 150)
w.create_line(210, 150, 255, 165)

#一个矩形
w.create_rectangle(130, 210, 270, 330, fill="DodgerBlue")

#一个圆
w.create_oval(150, 200, 250, 300, fill="white")

#一个矩形
w.create_rectangle(170, 200, 230, 210, fill="white", outline="")

#一条圆角粗直线
w.create_line(130, 205, 270, 205, fill="red", width=12, capstyle=ROUND)

#一个圆
w.create_oval(190, 205, 210, 225, fill="yellow")

#一个矩形
w.create_rectangle(191, 213, 209, 216, fill="yellow")

#一个圆
w.create_oval(198, 218, 202, 222, fill="red")

#一条直线
w.create_line(200, 222, 200, 225)

#一个扇形 
w.create_arc(170, 220, 230, 280, start=180, extent=180)

#一个扇形 
w.create_arc(188, 318, 212, 342, start=0, extent=180, fill="white")

#一个矩形
w.create_rectangle(190, 328, 210, 332, fill="white", outline="")

#两个椭圆
w.create_oval(110, 315, 192, 350, fill="white")
w.create_oval(208, 315, 290, 350, fill="white")

#两个多边形
points1=[130, 210, 90, 250, 110, 260, 130, 255]
w.create_polygon(points1, fill="DodgerBlue", outline="black")

points2=[270, 210, 310, 250, 290, 260, 270, 255]
w.create_polygon(points2, fill="DodgerBlue", outline="black")

#两个椭圆
w.create_oval(80, 245, 115, 280, fill="white")
w.create_oval(285, 245, 320, 280, fill="white")

mainloop() 
