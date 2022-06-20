from tkinter import *
from tkinter.ttk import *
from time import strftime

def pre_time():
    cur_time = strftime("%H:%M:%S %p")
    label.config(text = cur_time)
    label.after(1000, pre_time)


root = Tk()
root.title("Clock")


label = Label(root, font= ('calibri', 40, 'bold'))
label.pack()
pre_time()
root.mainloop()

