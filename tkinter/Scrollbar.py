from tkinter import *
screen=Tk()
sb=Scrollbar(screen)
sb.pack(side=RIGHT,fill=Y)
ml=Listbox(screen,yscrollcommand=sb.set)
for line in range(1,100,1):
    ml.insert(END,'this is line number'+str(line))
ml.pack(side=LEFT,fill=BOTH)
sb.config(command=ml.yview)
mainloop()
