# _*_ coding: utf-8 _*_

from Tkinter import *
import time

def get_week():
    listbox.delete(0,END)
    week_num = u'今天' + '(' + time.strftime('%Y%m%d') + ')' + u'是第' + time.strftime('%W') + u'周'
    listbox.insert(END,week_num)

root = Tk()  # 实例一个窗口对象
root.title("第几周")  #窗口的标题
#root.geometry('300x300+500+100') #设置窗口大小和位置
root.geometry('+500+100')  #自适应显示
button = Button(root,text = 'C L I C K',command = get_week) # 创建Button对象
button.grid()  # button显示形式 grid
listbox = Listbox(root,height = 1)  # 创建列表盒子对象
#listbox = Listbox(root,selectmode = SINGLE)
listbox.grid(row = 0, column = 1)  # grid方式显示
root.mainloop() # 显示
