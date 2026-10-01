from tkinter import*
from tkinter import messagebox


root=Tk()
root.geometry("300x200")


w=Label(root,text="I am a message box",font="50")
w.pack()


messagebox.showinfo("showinfo","information")
messagebox.showwarning("showwarning","warning")
messagebox.showerror("showerror","error")
messagebox.askquestion("askquestion","ARE U SURE")
messagebox.askokcancel("askokcancel","Want to countinue")
messagebox.askyesno("askyesno","Find the value")
messagebox.askretrycancel("askretrycancel","Try again")


root.mainloop()
 