import tkinter as tk
from tkinter import *

window = Tk()
window.title("Menu Example")

menubar = Menu(window)

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

window.config(menu=menubar)

window.mainloop()