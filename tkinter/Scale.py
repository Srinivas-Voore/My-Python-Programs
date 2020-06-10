from tkinter import *
screen=Tk()
v=Scale(screen,from_=0,to=40,orient=VERTICAL)
v.pack()
h=Scale(screen,from_=0,to=60,orient=HORIZONTAL)
h.pack()
mainloop()
