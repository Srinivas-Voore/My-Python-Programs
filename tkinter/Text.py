from tkinter import *
screen=Tk()
t=Text(screen,height=2,width=30)
t.pack()
t.insert(END,'this is editable line 1\nthis is editable line 2\n')
mainloop()
