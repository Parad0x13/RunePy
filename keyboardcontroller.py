import pynput

from logger import logger

class KeyboardController:
    def __init__(self):
        logger.log("Keyboard Controller Initiating")

        self.controller = pynput.keyboard.Controller()

    # [TODO] Consider renaming this from type as it belongs to python
    def type(self, text):
        # Press and release space
        #pynput.keyboard.Controller().press(pynput.keyboard.Key.space)
        #pynput.keyboard.Controller().release(pynput.keyboard.Key.space)

        # Type a lower case A; this will work even if no key on the
        # physical keyboard is labelled 'A'
        #pynput.keyboard.Controller().press("a")
        #pynput.keyboard.Controller().release("a")

        # Type two upper case As
        #pynput.keyboard.Controller().press('A')
        #pynput.keyboard.Controller().release('A')
        #with pynput.keyboard.Controller().pressed(pynput.keyboard.Key.shift):
        #    pynput.keyboard.Controller().press('a')
        #    pynput.keyboard.Controller().release('a')

        print("fubar")
        #self.controller.type("abcABC")
        self.controller.press("a")
        self.controller.release("a")

keyboardcontroller = KeyboardController()
