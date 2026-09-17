from tkinter import *
root=Tk()
root.title("traffic light")
root.geometry("300x300")
root.config(bg="light blue")

Button(root,text="stop",highlightbackground="red").grid(row=0,column=1,padx=10,pady=10)
Button(root,text="go",highlightbackground="green").grid(row=0,column=2,padx=10,pady=10)
Button(root,text="wait",highlightbackground="yellow").grid(row=0,column=3,padx=10,pady=10)

root.mainloop()