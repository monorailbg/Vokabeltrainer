import tkinter
from tkinter import *

root = Tk()
root.title('Understanding Layouts in Tkinter, Grid Layout')
root.geometry('400x300')

frame = Frame(root)

Label(frame, text='FORM IN TKINTER', font=('Arial Bold', 16)).grid(row=0, column=0, columnspan=2, pady=(0, 20)) #(top, bottom)

Label(frame, text='First Name').grid(row=1, column=0)
Entry(frame).grid(row=1, column=1)

Label(frame, text='Last Name').grid(row=2, column=0)
Entry(frame).grid(row=2, column=1)

Checkbutton(frame, text='I agree to terms & conditions').grid(row=3, column=0, columnspan=2, sticky=W)

frame.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
