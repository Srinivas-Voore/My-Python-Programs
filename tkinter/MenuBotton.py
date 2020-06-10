from tkinter import *
screen=Tk() 
mb=Menubutton(screen,text ='Help',relief=FLAT) 
mb.grid()
mb.menu=Menu(mb,tearoff=0) 
mb['menu']=mb.menu 
cvar = IntVar() 
avar = IntVar() 
mb.menu.add_checkbutton(label='Contact',variable=cvar) 
mb.menu.add_checkbutton(label='About',variable=avar) 
mb.pack() 
mainloop() 
