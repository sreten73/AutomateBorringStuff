#! python3
# move_mouse.py
# Automatically move mouse every 45 seconds 15 times.


import pyautogui
import time
import random

counter = 0
while counter < 15:
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Generate a random position within the screen bounds
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Move the mouse to the random position
    pyautogui.moveTo(x, y)

    # Wait for 45 seconds before moving the mouse again
    time.sleep(45)

    # Increment the counter variable
    counter += 1