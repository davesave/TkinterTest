from tkinter import *


def button_command():
        print('populate')
        # button['bg'] = 'blue'

        for item in ['Liz', 'Tom', 'Chi']:
                listbox.insert(END, item)        # END = position

root = Tk()
root.geometry('600x400+500+500')  # WTF: width x height + topX + topY

listbox = Listbox(root)
button = Button(root, text='Press', command=button_command, padx=100, pady=100)

button.pack()
listbox.pack()

# Run.
root.mainloop()
