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
        #self.current = set()
        self.pressed_vks = set()

        #with keyboard.Listener(on_press = self.on_press, on_release = self.on_release) as listener: listener.join()

        listener = keyboard.Listener(on_press = self.on_press, on_release = self.on_release)
        listener.start()
        #for item in vars(listener): print(item)
        """
        with keyboard.GlobalHotKeys(
            {
                "<alt>+<ctrl>+k": self.test01,
                #"<alt>+<ctrl>+l": self.test02,
            }
        ) as h: h.join()
        """
        #test = keyboard.GlobalHotKeys({"<alt>+<ctrl>+k": self.test01})
        #test.start()
        #print(keyboard.GlobalHotKeys)
        #keyboard.GlobalHotKeys["<alt>+<ctrl>+l"] = self.test02
        #print(keyboard.GlobalHotKeys)
        #print(vars(keyboard.GlobalHotKeys._on_press))
        #print(keyboard.GlobalHotKeys.__doc__)
        #for item in vars(keyboard.GlobalHotKeys): print(item)
        #print(keyboard.GlobalHotKeys.hotkeys)

    def test01(self): print("test01")
    def test02(self): print("test02")

    def get_vk(self, key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        val = key

        # [TODO] I HATE HATE HATE the way I'm doing this here, fix this at some point PLEASE!!!
        if val == keyboard.HotKey.parse("<ctrl_l>")[0]: val = keyboard.HotKey.parse("<ctrl>")[0]
        if val == keyboard.HotKey.parse("<ctrl_r>")[0]: val = keyboard.HotKey.parse("<ctrl>")[0]

        if val == keyboard.HotKey.parse("<alt_l>")[0]: val = keyboard.HotKey.parse("<alt>")[0]
        if val == keyboard.HotKey.parse("<alt_r>")[0]: val = keyboard.HotKey.parse("<alt>")[0]

        #return key.vk if hasattr(key, 'vk') else key.value.vk
        #return val.vk if hasattr(val, 'vk') else val.value.vk
        return val.vk if hasattr(val, 'vk') else val

        #return val

    def is_combination_pressed(self, combination):
        combination = combination._keys

        print(self.pressed_vks)
        print(combination)

        """ Check if a combination is satisfied using the keys pressed in pressed_vks """
        #print(self.pressed_vks)
        #print(combination)
        #print()
        a = set()
        b = set()
        a = self.pressed_vks
        #for key in self.pressed_vks: a.add(self.get_vk(key))
        for key in combination:
            print("adding {}".format(key))
            b.add(self.get_vk(key))
        print(a)
        print(b)
        if a == b: return True
        return False
        #return all([self.get_vk(key) in self.pressed_vks for key in combination])

    """
    def on_press(self, key):
        #def for_canonical(f): return lambda k: f(l.canonical(k))

        #print("something has been pressed")
        #print(vars(self.combinations[0]))

        self.current.add(key)
        #print(self.current)

        found = None
        for combo in self.combinations:
            hk = combo._keys
            #test = keyboard.HotKey.parse(self.current)
            test = self.current
            print("Currently pressing: {}".format(test))
            print("Checking combo: {}".format(hk))
            print()
            if hk == self.current:
                found = combo
                print(hk)

        #if any ([key in combo for combo in self.combinations]):
        #    current.add(key)
        #    if any(all(k in current for k in combo) for combo in self.combinations): execute()
    """

    def on_press(self, key):
        #print(key.value.vk)
        #print(vars(key))
        #print(self.get_vk(key))
        #print()
        vk = self.get_vk(key)  # Get the key's vk
        #print("addding {}".format(vk))
        self.pressed_vks.add(vk)  # Add it to the set of currently pressed keys

        for combination in self.combinations:  # Loop though each combination
            if self.is_combination_pressed(combination):  # And check if all keys are pressed
                #execute()  # If they are all pressed, call your function
                print("Gotacombo! {}".format(combination))
                break  # Don't allow execute to be called more than once per key press

    """
    def on_release(self, key):
        #print("something has been released")

        self.current.remove(key)

        #if any([key in combo for combo in self.combinations]): current.remove(key)
    """
    def on_release(self, key):
        """ When a key is released """
        vk = self.get_vk(key)  # Get the key's vk
        self.pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys

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
