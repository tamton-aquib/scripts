#!/usr/bin/env python3

import pyautogui as pog
import sys, time

words = "nice" if len(sys.argv) <= 2  else sys.argv[1]

time.sleep(3)

for i in range(3 if len(sys.argv) <= 3 else int(sys.argv[2])):
    pog.write(words)
    pog.press("enter")
    time.sleep(0.5)
