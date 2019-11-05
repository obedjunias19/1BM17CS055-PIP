from tkinter import * 
from tkinter.ttk import * 
from time import strftime
from tkinter import messagebox
'''
def file1:
    messagebox.showinfo("Menu info","File option pressed")
def open1:
    messagebox.showinfo("Menu info","Open option pressed")
def save1:
    messagebox.showinfo("Menu info","Save option pressed")'''
# creating tkinter window 
root = Tk() 
root.title('Menu Demonstration') 
  
# Creating Menubar 
menubar = Menu(root) 
  
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = messagebox.showinfo("Menu info","File option pressed")) 
file.add_command(label ='Open...', command = messagebox.showinfo("Menu info","Open option pressed")) 
file.add_command(label ='Save', command = messagebox.showinfo("Menu info","Save option pressed")) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command = None) 
edit.add_command(label ='Paste', command = None) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 


# display Menu 
root.config(menu = menubar) 
mainloop()


