#!/usr/bin/env python3
import googletrans
from tkinter import Tk, Label, Button

root = Tk()
root.geometry('640x400+320+180')

sentence = root.clipboard_get()

translator = googletrans.Translator()
nice = translator.translate(sentence)

for i in range(5):
	Label(root, text=f" ").pack()
	
Label(root, text=f"From: {nice.src}").pack()
Label(root, text=f"To  : {nice.dest}").pack()
Label(root, text=f"Translation: {nice.text}").pack()

close_button = Button(root, text="close", command=root.destroy).pack()

root.mainloop()
