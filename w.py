from tkinter import * 
from tkinter.ttk import *

root=Tk()

progress=Progressbar(root,orient=HORIZONTAL,length=100,mode="determinate")

def bar():
    import time 
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)

    progress['value']=40
    root.update_idletasks()
    time.sleep(1)

    progress['value']=50
    root.update_idletasks()
    time.sleep(1)

    progress['value']=60
    root.update_idletasks()
    time.sleep(1)

    progress['value']=80
    root.update_idletasks()
    time.sleep(1)

    progress['value']=100

progress.grid(row=0,column=1,padx=675,pady=675)

Button(root,text='SUBMIT ORDER',command=bar).grid(row=1,column=1,padx=675,pady=675)
        

menubar = Menu(root)

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label = "Exit")
menubar.add_cascade(label="File", menu=file_menu)


edit_menu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "edit", menu = edit_menu)


help_menu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "help", menu = help_menu)

settings_menu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "settings", menu = settings_menu)

root.config(menu=menubar)
    

s1=Spinbox(root, from_ = 10, to = 22, highlightbackground = "lightgreen", increment =1 )
s1.pack()
s2=Spinbox(root, from_ = 10, to =22, highlightbackground = "red", increment = -1)
s2.pack()
Label(root,text="10-22",highlightbackground="blue").pack()
root.mainloop()