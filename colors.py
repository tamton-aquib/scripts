#!/usr/bin/env python3
import pyautogui as pog
import pyperclip
from tkinter import *

root = Tk()
label = Label(root, text="Click to copy the color").pack()

x, y = pog.position()
r, g, b = tuple(pog.pixel(x, y))

rgb_color = f"({r},{g},{b})"
hex_color = f"#{r:02x}{g:02x}{b:02x}"
hex_color_upper = hex_color.upper()

def noice(color_code):
    """noice"""
    pyperclip.copy(color_code)
    root.destroy()

color_frame = Label(root, text=" ", bg=hex_color, width=10, height=2).pack()
btn1 = Button(root, text=rgb_color, width=15, command = lambda: noice(rgb_color)).pack()
btn1 = Button(root, text=hex_color, width=15, command = lambda: noice(hex_color)).pack()
btn3 = Button(root, text=hex_color_upper, width=15, command = lambda: noice(hex_color_upper)).pack()

root.mainloop()
