from tkinter import *
w1=PanedWindow()
w1.pack(fill=BOTH,expand=1)
left=Entry(w1,bd=5)
w1.add(left)

w2=PanedWindow(w1,orient=VERTICAL)
w1.add(w2)
top=Scale(w2,orient=HORIZONTAL)
w2.add(top)
mainloop()
