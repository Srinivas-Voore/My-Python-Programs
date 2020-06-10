from tkinter import *
screen=Tk()
menu=Menu(screen)
screen.config(menu=menu)

filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=screen.quit)

helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')

mainloop()
