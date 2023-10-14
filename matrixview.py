'''
这是用于显示矩阵的小脚本，输入为numpy数组或矩阵
'''

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import keyboard as kb
import tkinter.messagebox

__version__ = '0.0.2'

def MV(K, Matname):
    if K.ndim == 1:  # 如果K是一维数组，将其变为二维数组
        K = K.reshape(-1, 1)

    # plt.plot()
    def ScrollCommand_h(*xx):  # 在滚动条上点击、拖动等动作
        canvas.xview(*xx)
        canvas_h.xview(*xx)
    def ScrollCommand_v(*xx):  # 在滚动条上点击、拖动等动作
        canvas.yview(*xx)
        canvas_v.yview(*xx)
    def Wheel(event):  # 鼠标滚轮动作
        if kb.is_pressed("shift"):  # 横向滚动
            canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas_h.xview_scroll(int(-1 * (event.delta / 120)), "units")
        else:  # 纵向滚动
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas_v.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"


    root = Tk()
    root.title('MatView.matrix -- ' + Matname)
    root.geometry('1000x600')
    frame = Frame(root, width=1000, height=600)
    frame.pack(expand=True, fill=BOTH)
    # 显示矩阵的主画布
    canvas = Canvas(frame,bg='#FFFFFF',width=1900,height=1020, scrollregion=(0,0,100+K.shape[1]*80,50+K.shape[0]*40))
    # 显示列数的横画布
    canvas_h = Canvas(frame, bg='#FFFFFF', width=1900, height=30, scrollregion=(0,0,100+K.shape[1]*80,0))
    # 显示行数的纵画布
    canvas_v = Canvas(frame, bg='#FFFFFF', width=50, height=1020, scrollregion=(0,0,0,50+K.shape[0]*40))
    # 横向滚动条
    hbar = Scrollbar(frame, orient=HORIZONTAL, command=ScrollCommand_h)
    hbar.pack(side=BOTTOM, fill=X)
    # 纵向滚动条
    vbar = Scrollbar(frame, orient=VERTICAL, command=ScrollCommand_v)
    vbar.pack(side=RIGHT, fill=Y)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas_h.config(xscrollcommand=hbar.set)
    canvas_v.config(yscrollcommand=vbar.set)
    canvas.place(x=0, y=0)
    canvas_h.place(x=0, y=0)
    canvas_v.place(x=0, y=0)




    for i in range(K.shape[1]):  # 横向画布上写列数
        xloc = 90 + i * 80
        yloc = 15
        canvas_h.create_text(xloc, yloc, text=str(i), fill='red')
    for i in range(K.shape[0]):  # 纵向画布上写行数
        xloc = 20
        yloc = 50 + i * 40
        canvas_v.create_text(xloc, yloc, text=str(i), fill='red')

    for i in range(K.shape[0]):  # 主画布上写矩阵
        for j in range(K.shape[1]):
            if K[i, j] == 0:
                xloc = 90 + j * 80
                yloc = 50 + i * 40
                canvas.create_text(xloc, yloc, text='0', fill='blue')
            elif -10000 < K[i, j] < -0.1 or 0.1 < K[i, j] < 10000:
                xloc = 90 + j * 80
                yloc = 50 + i * 40
                canvas.create_text(xloc, yloc, text=str(round(K[i, j], 2)))
            else:
                xloc = 90 + j * 80
                yloc = 50 + i * 40
                canvas.create_text(xloc, yloc, text=str('{:.1e}'.format(K[i, j])))

#####以下为功能区
    def Cross(event):  # 画十字标线
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)  # 获取鼠标在画布canvas中的坐标
        canvas.coords(cross_h, x-2000, y, x+2000, y)
        canvas.coords(cross_v, x, y - 1200, x, y + 1200)
    cross_h = canvas.create_line(0, 0, 0, 0, fill='red')
    cross_v = canvas.create_line(0, 0, 0, 0, fill='red')
    canvas.bind('<Motion>', Cross)

    def DoubleClick1(event):  # 双击鼠标左键显示元素值
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
        i = round((y-50)/40)
        j = round((x-90)/80)
        tkinter.messagebox.showinfo(title=Matname+'[ i , j ]', message='[ '+str(i)+' , '+str(j)+' ]\n'+str(K[i, j]))

    def Draw(event):  # 鼠标右键写字
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
        canvas.create_line((x, y, x+1, y+1), width=2, fill="deepskyblue")

    canvas.bind("<MouseWheel>", Wheel)
    canvas.bind("<Double-Button-1>", DoubleClick1)
    canvas.bind("<B3-Motion>", Draw)

    def ProgramContinue():  # 主程序继续执行的按钮
        root.quit()
        # plt.close()
    stop_button =Button(root, text='继 续', width=5, height=1, command=ProgramContinue)
    stop_button.place(x=0, y=0)

    root.mainloop()

def LV(K, Listname):
    def ScrollCommand_h(*xx):  # 在滚动条上点击、拖动等动作
        canvas.xview(*xx)
        canvas_h.xview(*xx)
    def ScrollCommand_v(*xx):  # 在滚动条上点击、拖动等动作
        canvas.yview(*xx)
        canvas_v.yview(*xx)
    def Wheel(event):  # 鼠标滚轮动作
        if kb.is_pressed("shift"):  # 横向滚动
            canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas_h.xview_scroll(int(-1 * (event.delta / 120)), "units")
        else:  # 纵向滚动
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas_v.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"
    root = Tk()
    root.title('MatView.list -- ' + Listname)
    root.geometry('600x600')
    frame = Frame(root, width=600, height=600)
    frame.pack(expand=True, fill=BOTH)
    # 显示矩阵的主画布
    canvas = Canvas(frame, bg='#FFFFFF', width=1900, height=1020,
                    scrollregion=(0, 0, 10000, 50 + len(K) * 40))
    # 显示列数的横画布
    canvas_h = Canvas(frame, bg='#FFFFFF', width=1900, height=30, scrollregion=(0, 0, 10000, 0))
    # 显示行数的纵画布
    canvas_v = Canvas(frame, bg='#FFFFFF', width=50, height=1020, scrollregion=(0, 0, 0, 50 + len(K) * 40))
    # 横向滚动条
    hbar = Scrollbar(frame, orient=HORIZONTAL, command=ScrollCommand_h)
    hbar.pack(side=BOTTOM, fill=X)
    # 纵向滚动条
    vbar = Scrollbar(frame, orient=VERTICAL, command=ScrollCommand_v)
    vbar.pack(side=RIGHT, fill=Y)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas_h.config(xscrollcommand=hbar.set)
    canvas_v.config(yscrollcommand=vbar.set)
    canvas.place(x=0, y=0)
    canvas_h.place(x=0, y=0)
    canvas_v.place(x=0, y=0)

    for i in range(len(K)):  # 纵向画布上写行数
        xloc = 20
        yloc = 50 + i * 40
        canvas_v.create_text(xloc, yloc, text=str(i), fill='green')

    for i in range(len(K)):  # 主画布上写矩阵
        xloc = 90
        yloc = 50 + i * 40
        canvas.create_text(xloc, yloc, text=str(K[i]), anchor='w')

#####以下为功能区
    def Cross(event):  # 画十字标线
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)  # 获取鼠标在画布canvas中的坐标
        canvas.coords(cross_h, x-2000, y, x+2000, y)
        canvas.coords(cross_v, x, y - 1200, x, y + 1200)
    cross_h = canvas.create_line(0, 0, 0, 0, fill='green')
    cross_v = canvas.create_line(0, 0, 0, 0, fill='green')
    canvas.bind('<Motion>', Cross)

    def DoubleClick1(event):  # 双击鼠标左键显示元素值
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
        i = round((y-50)/40)
        if isinstance(K[i], list):
            LV(K[i], Listname + '['+str(i)+']')
        else:
            tkinter.messagebox.showinfo(title=Listname + '['+str(i)+']', message=str(K[i]))

    def Draw(event):  # 鼠标右键写字
        x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
        canvas.create_line((x, y, x+1, y+1), width=2, fill="deepskyblue")

    canvas.bind("<MouseWheel>", Wheel)
    canvas.bind("<Double-Button-1>", DoubleClick1)
    canvas.bind("<B3-Motion>", Draw)

    def ProgramContinue():  # 主程序继续执行的按钮
        root.quit()
        # plt.close()
    stop_button =Button(root, text='go on', width=5, height=1, command=ProgramContinue)
    stop_button.place(x=0, y=0)

    root.mainloop()

def view(M, name):
    if isinstance(M, list):
        LV(M, name)
    else:
        MV(M, name)



# plt.plot()
# K = np.ones((101,101))
# for i in range(K.shape[0]):
#     for j in range(K.shape[1]):
#         K[i,j] = i+j/1000
# MV(K)