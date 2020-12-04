import pynput
from logger import logger

class Hotkeys:
    def __init__(self):
        logger.log("Hotkeys Initiating")

    # [TODO] This is just an example, remove this later
    def printStuff(self):
        # Press and release space
        pynput.keyboard.Controller().press(pynput.keyboard.Key.space)
        pynput.keyboard.Controller().release(pynput.keyboard.Key.space)

        # Type a lower case A; this will work even if no key on the
        # physical keyboard is labelled 'A'
        pynput.keyboard.Controller().press('a')
        pynput.keyboard.Controller().release('a')

        # Type two upper case As
        pynput.keyboard.Controller().press('A')
        pynput.keyboard.Controller().release('A')
        with pynput.keyboard.Controller().pressed(pynput.keyboard.Key.shift):
            pynput.keyboard.Controller().press('a')
            pynput.keyboard.Controller().release('a')

        # Type 'Hello World' using the shortcut type method
        pynput.keyboard.Controller().type('Hello World')

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(self, key):
        print('{0} released'.format(key))
        if key == pynput.keyboard.Key.esc:
            # Stop listener
            return False

    def run(self):
        pynput.keyboard.Listener(on_press = self.on_press, on_release = self.on_release).start()

hotkeys = Hotkeys()    # [TODO] Consider if this should be global, like logger, or if we should confine it's scope
