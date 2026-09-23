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

progress.grid(row=0,column=1,padx=675)

Button(root,text='download',command=bar).grid(row=1,column=1,padx=675)

root.mainloop()
        
    
    
    
    
    
