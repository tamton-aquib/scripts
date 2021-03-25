#!/usr/bin/env python3
import pyautogui as pog
import pyperclip

x, y = pog.position()
r, g, b = tuple(pog.pixel(x, y))

rgb_color = f"({r},{g},{b})"
hex_color = f"#{r:02x}{g:02x}{b:02x}"
hex_color_upper = hex_color.upper()

option = pog.confirm(title="Success",
                     text="Click to copy!",
                     buttons=[f"{rgb_color}", f"{hex_color}", f"{hex_color_upper}"])

pyperclip.copy(option)
print(f"Copied {option} to clipboard!")
