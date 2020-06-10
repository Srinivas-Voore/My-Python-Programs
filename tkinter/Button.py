import tkinter
screen=tkinter.Tk()
screen.title('close screen on button click')
button=tkinter.Button(screen,text="END",width=25,command=screen.destroy)
button.pack()
screen.mainloop()
