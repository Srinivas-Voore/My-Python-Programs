from tkinter import *
screen=Tk()
lb=Listbox(screen)
lb.insert(1,'Python')
lb.insert(2,'Java')
lb.insert(1,'C')
lb.insert(1,'other')
lb.pack()
mainloop()
