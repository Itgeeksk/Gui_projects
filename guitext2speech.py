from tkinter import *
from gtts import gTTS
import os

root = Tk()
root.title("Text to Speech")
root.geometry("700x100")

taking_input = Entry(root)
taking_input.pack(ipadx= 400, ipady=20)

def convert():
    user_input = taking_input.get()
    word = gTTS(text = user_input, lang='en')
    filename = "Texttospeech.mp3"
    word.save(filename)
    os.system(f"start {filename}")

convert_button = Button(root, text="Convert", command=convert).pack()

root.mainloop()