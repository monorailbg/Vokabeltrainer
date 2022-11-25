from tkinter import *
from tkinter.ttk import *
import time


def start():
    s = 60
    download = 0
    speed = 1
    while (download < s):
        time.sleep(1)
        bar['value'] += (speed / s) * 100
        download += speed
        text.set(str(download) + "/" + str(s) + "s")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="start", command=start).pack()

window.mainloop()
