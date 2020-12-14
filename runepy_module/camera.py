from runepy_controller import mouse
from runepy_controller import keyboard
from random import randint

def compass_pos():
    compass = [22, 46, 39, 66]
    mouse.move(randint(compass[0], compass[2]), randint(compass[1], compass[3]))

keyboard.registerHotkey("ctrl+alt+u", compass_pos, "Moved to compass")
