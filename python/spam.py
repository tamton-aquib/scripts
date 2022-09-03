import pyautogui as pog
from time import sleep

words = """
This is spamming script from maxcodez. Type the words here to spam
"""

sleep(3) # 3 seconds to get ready before boom

for word in words.strip().split():
    pog.write(word)
    pog.press("enter")
    sleep(0.5)
