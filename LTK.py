#_*_ coding:UTF-8 _*_
from tkinter import *
root =Tk()
li = ['枪兵系','弓兵系','盾兵系','骑兵系','术法系']
movie =['民兵','枪兵','戟兵']
listb = Listbox(root)
listb2 = Listbox(root)
for item in li:
    listb.insert(0,item)
for item in movie:
    listb2.insert(0,item)

listb.pack()
listb2.pack()
root.mainloop()
