from tkinter import *


def pack_layout():
    top_frame.pack()
    bottom_frame.pack(side=BOTTOM, fill=X)
    button_1.pack(side=LEFT)
    button_2.pack(side=LEFT)
    button_3.pack(side=LEFT)
    button_4.pack()
    label_x.pack(fill=X)


root = Tk()

top_frame = Frame(root)
bottom_frame = Frame(root)

button_1 = Button(top_frame, text='Button 1', fg='red')
button_2 = Button(top_frame, text='Button 2', fg='blue')
button_3 = Button(top_frame, text='Button 3', fg='green')
button_4 = Button(bottom_frame, text='Button 4', fg='purple')

label_x = Label(bottom_frame, text='Label X', bg='red', fg='white')

pack_layout()

root.mainloop()
