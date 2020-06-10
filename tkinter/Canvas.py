from tkinter import *
screen=Tk()
w=Canvas(screen,width=40,height=60)
w.pack()
ch=20
cw=200
y=int(ch/2)
w.create_line(0,y,cw,y)
screen.mainloop
