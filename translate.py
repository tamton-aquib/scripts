#!/usr/bin/env python3
import googletrans
from tkinter import Tk, Label

root = Tk()

sentence = root.clipboard_get()

translator = googletrans.Translator()
nice = translator.translate(sentence)

label = Label(root, text=nice.text)
label.pack()

root.mainloop()
