from tkinter import *
screen=Tk()
Label(screen,text='First Name').grid(row=0)
Label(screen,text='Last Name').grid(row=1)
e1=Entry(screen)
e2=Entry(screen)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()
