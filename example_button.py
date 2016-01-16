from tkinter import *


def button_command():
        print('buttons are cool')

root = Tk()

button = Button(root, text='Press', command=button_command)
button.pack(padx=20, pady=20)

root.mainloop()
