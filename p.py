from tkinter import *

root=Tk()
root.title("SPIN BOX")
s1=Spinbox(root, from_ = 10, to = 22, highlightbackground = "lightgreen")
s1.pack()
s2=Spinbox(root, from_ = 22, to = 10, highlightbackground = "red")
s2.pack()
Label(root,text="10-22",highlightbackground="blue")
root.mainloop()