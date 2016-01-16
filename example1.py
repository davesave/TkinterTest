from tkinter import *           # Importing the Tkinter (tool box) library
root = Tk()                     # Create a background window
                                # Create a list
li = 'Carl Patrick Lindsay Helmut Chris Gwen'.split()
listbx = Listbox(root)           # Create a listbox widget

for item in li:                 # Insert each item within li into the listbox
    listbx.insert(0, item)

listbx.pack()                   # Pack listbox widget
root.mainloop()                 # Execute the main event handler