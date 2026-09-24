from tkinter import * 
from tkinter.ttk import *

root=Tk()

Label(root,text="Email").grid(row=0,column=1,padx=10,pady=10)
Label(root,text="Password").grid(row=1,column=0,padx=10,pady=10)
Label(root,text="what would you like :chicken sandwich, or veg sandwich or none").grid(row=0,column=1,padx=10,pady=10)
Label(root,text="what bevarage would you like :cola,fanta,orange juice,water or none").grid(row=1,column=0,padx=10,pady=10)
Label(root,text="what dessert would you like :ice cream, ice lolly, choclate cake or none").grid(row=0,column=1,padx=10,pady=10)


Email_entry=Entry(root,width=20)
Email_entry.grid(row=1,column=1,padx=10,pady=10)

Password_entry=Entry(root,width=20,show = "*" )
Password_entry.grid(row=1,column=1,padx=10,pady=10)





s1=Spinbox(root,values=('chicken sandwich' ,'veg sandwich', 'none'))
s1.pack()
s2=Spinbox(root,values=('cola','fanta','orange juice','water','none'))
s2.pack()
s3=Spinbox(root,values=('ice cream','ice lolly','choclate cake','none'))
s3.pack()


        

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

Button(root,text='Submit Order',command=bar).grid(row=1,column=1,padx=675)

root.mainloop()
    

    
    
