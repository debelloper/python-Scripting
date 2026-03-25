import pyautogui
import time
import os

print("Starting automation in 5 seconds...")
time.sleep(5)

# Move mouse
pyautogui.moveTo(500, 300, duration=1)

# Click
pyautogui.click()

# Type something
pyautogui.write("Hello, I am controlling my PC!", interval=0.05)

# Press Enter
pyautogui.press("enter")

# Open Notepad
os.system("notepad")