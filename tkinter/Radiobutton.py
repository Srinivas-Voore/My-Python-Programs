from tkinter import *
screen=Tk()
v=IntVar()
Radiobutton(screen,text='Python',variable=v,value=1).pack(anchor=W)
Radiobutton(screen,text='Java',variable=v,value=2).pack(anchor=W)
mainloop()
