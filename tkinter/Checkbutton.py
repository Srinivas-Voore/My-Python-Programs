from tkinter import *
screen=Tk()
var1=IntVar()
Checkbutton(screen,text='male',variable=var1).grid(row=0,column=0)
var2=IntVar()
Checkbutton(screen,text='female',variable=var2).grid(row=1,column=0)
mainloop()
