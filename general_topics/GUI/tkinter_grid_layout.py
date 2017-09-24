from tkinter import *


root = Tk()

label_login = Label(root, text='Login')
label_password = Label(root, text='Password')

entry_login = Entry(root)
entry_password = Entry(root)

checkbox = Checkbutton(root, text='Keep me logged in')

label_login.grid(row=0, sticky=E)
label_password.grid(row=1, sticky=E)
entry_login.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
checkbox.grid(columnspan=2)

root.mainloop()
