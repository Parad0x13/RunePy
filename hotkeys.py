"""
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
"""

from pynput import keyboard
from pynput.keyboard import Key, Controller

from common import *
from logger import logger

class Hotkeys:
    def __init__(self):
        logger.log("Hotkeys Initializing")

        self.combinations = []
        self.current = set()

        #with keyboard.Listener(on_press = self.on_press, on_release = self.on_release) as listener: listener.join()
        listener = keyboard.Listener(on_press = self.on_press, on_release = self.on_release)
        listener.start()

    def on_press(self, key):
        #print("something has been pressed")
        #print(vars(self.combinations[0]))
        self.current.add(key)
        print(self.current)
        #if any ([key in combo for combo in self.combinations]):
        #    current.add(key)
        #    if any(all(k in current for k in combo) for combo in self.combinations): execute()

    def on_release(self, key):
        #print("something has been released")
        self.current.remove(key)
        #if any([key in combo for combo in self.combinations]): current.remove(key)

    def register(self, format, on_activate):
        #"""
        # [TODO] Get this crap out of my software!!!
        def for_canonical(f): return lambda k: f(l.canonical(k))

        # [TODO] Add the ability to name the parent function's name as well
        logger.log("Registering a hotkey {} with on_activate {}".format(format, on_activate.__name__))

        # [TODO] Sanity check on cannonization syntax
        hotkey = keyboard.HotKey(keyboard.HotKey.parse(format), on_activate)
        #print(hotkey.parse())
        print(keyboard.HotKey.parse(format))

        self.combinations.append(hotkey)
        # !!! Left off here, need to find out why/how to get this to parse correctly... !!!

        #with keyboard.Listener(on_press = for_canonical(hotkey.press), on_release = for_canonical(hotkey.release)) as l: l.join()
        #"""
        #print(type(keyboard.GlobalHotKeys))
        #keyboard.GlobalHotKeys[format] = on_activate
        #keyboard.GlobalHotKeys.append([format, on_activate])

hotkeys = Hotkeys()
