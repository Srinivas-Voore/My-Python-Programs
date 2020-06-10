from tkinter import *
screen=Tk()
screen.title('GFG')  

def open():
    top=Toplevel(screen)
    top.title('Python')
    top.mainloop()

btn = Button(screen, text = "open", command = open)  
btn.place(x=75,y=50)  
screen.mainloop()  
