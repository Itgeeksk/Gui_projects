# Importing modules
import tkinter as tk
from tkinter import font
from tkinter.constants import SUNKEN


# Making the main window to work
root = tk.Tk()
# giving title to the window
root.title("Calculator")

main_frame =tk.Frame(master=root, padx=10)
main_frame.pack()

entry = tk.Entry(master=main_frame, width=80, borderwidth=3 ,font=30)
entry.grid(column=0, row= 0, columnspan=3, ipadx=25, ipady=10)
# functions --------------------
def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        entry.insert("Error")

def click(num):
    entry.insert(tk.END ,num)


# Butttons fro calculator
button_1 = tk.Button(master=main_frame, text="1" , padx = 60 , pady= 40, command=lambda:click(1)).grid(column=0 , row=5) 
button_2 = tk.Button(master=main_frame, text="2" , padx = 60 , pady= 40, command=lambda:click(2)).grid(column=1 , row=5)
button_3 = tk.Button(master=main_frame, text="3" , padx = 60 , pady= 40, command=lambda:click(3)).grid(column=2 , row=5) 

button_4 = tk.Button(master=main_frame, text="4" , padx = 60 , pady= 40, command=lambda:click(4)).grid(column=0 , row=4) 
button_5 = tk.Button(master=main_frame, text="5" , padx = 60 , pady= 40, command=lambda:click(5)).grid(column=1, row=4) 
button_6 = tk.Button(master=main_frame, text="6" , padx = 60 , pady= 40, command=lambda:click(6)).grid(column=2 , row=4) 

button_7 = tk.Button(master=main_frame, text="7" , padx = 60 , pady= 40, command=lambda:click(7)).grid(column=0 , row=3) 
button_8 = tk.Button(master=main_frame, text="8" , padx = 60 , pady= 40, command=lambda:click(8)).grid(column=1 , row=3) 
button_9 = tk.Button(master=main_frame, text="9" , padx = 60 , pady= 40 ,command=lambda:click(9)).grid(column=2 , row=3) 

button_add = tk.Button(master=main_frame, text="+", padx =60, pady= 40, command=lambda:click("+") ).grid(column=0, row= 6)
button_sub = tk.Button(master=main_frame, text="-", padx = 60 , pady= 40, command=lambda:click("-")).grid(column=1, row= 6)
button_divide = tk.Button(master=main_frame, text="/", padx = 60 , pady= 40, command=lambda:click("/")).grid(column=2, row= 6)
button_multiply = tk.Button(master=main_frame, text="*", padx = 60 , pady= 40, command=lambda:click("*")).grid(column=4, row= 4)


button_0 = tk.Button(master=main_frame, text="0" , padx = 60 , pady= 40,command=lambda:click(0)).grid(column=4 , row=3)
button_clear = tk.Button(master=main_frame, text="Clear", padx = 50, pady= 40, command=clear).grid(column=4, row=5,)
button_equal = tk.Button(master=main_frame, text="=", padx = 60, pady= 40, command=equal).grid(column=4, row=6,)


# calling the mainLoop
root.mainloop()