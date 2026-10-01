from tkinter import *


root=Tk()
root.title("Student Selecter")
root.geometry("350x350")

frame=Frame(root,highlightbackground="lightblue",bd=3)
frame.pack(padx=20,pady=20)

Label(frame,text="Select a student",highlightbackground="light blue").pack()

listbox=Listbox(frame,height=8,width=25)
listbox.pack(side=LEFT)


students = [
    "Aarav",
    "Amelia",
    "Oliver",
    "Zara",
    "Ayan",
    "Iona",
    "Pippa",
    "Alex",
    "Ava",
    "Swara",
    "Alan",
    "Gabriella",
    "Oore",
    "Sinmi",
    "Laolu",
]

for student in students:
    listbox.insert(END,student)
Scrollbar=Scrollbar(frame)
Scrollbar.pack(side=RIGHT,fill=Y)
listbox.config(yscrollcommand=Scrollbar.set)
Scrollbar.config(command = listbox.yview)

def select_student():
    selected=listbox.curselection()

    if selected:
        name=listbox.get(selected[0])
        result.config(text="Selected:"+name)


Button(root,text="SELECT STUDENT",command=select_student).pack()


result=Label(root,text="")
result.pack()


root.mainloop()









