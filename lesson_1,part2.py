from tkinter import*
root=Tk()
root.title("News letter")
root.geometry("300x180")
root.config(bg="light blue")

Label(root,text="subscribe to are news letter",bg="light blue").grid(row=0,column=1,padx=10,pady=10)
Label(root,text="email",bg="light blue").grid(row=1,column=0,padx=10,pady=10)

email_entry=Entry(root,width=20,show = "*" )
email_entry.grid(row=1,column=1,padx=10,pady=10)


def suscribe():
    email=email_entry.get()
    print("email:",email)


def cancel():
    root.destroy()


subscribe_btn=Button(root,text="Login",bg="lightgreen",width=10,command=suscribe)
subscribe_btn.grid(row=2,column=0,padx=10,pady=20)

cancel_btn=Button(root,text="cancel",bg="salmon",width=10,command=cancel)
cancel_btn.grid(row=2,column=1,padx=10,pady=20)

root.mainloop()
