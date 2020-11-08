from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard_controller = Controller()

COMBINATIONS = [
    {Key.shift, keyboard.KeyCode(char = "p")},
    {Key.shift, keyboard.KeyCode(char = "P")}
]

current = set()

def execute():
    print("Dectected HotKey")

    # "hitting" backspace to remove the "P",
    # must be unnecessary if we use some other modifier (Alt, Ctrl)
    keyboard_controller.press(Key.backspace)
    keyboard_controller.release(Key.backspace)

    keyboard_controller.type("Hotkey Triggered")

def on_press(key):
    if any ([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS): execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]): current.remove(key)

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener: listener.join()
