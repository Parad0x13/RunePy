import pynput
from logger import logger

from keyboardcontroller import keyboardcontroller

testController = pynput.keyboard.Controller()

def aaa():
    testController.type("abcABC")

class Hotkeys:
    def __init__(self):
        logger.log("Hotkeys Initiating")

        self.hotkeys = {}

    def register(self, hotkey, function):
        logger.log("Attempting to register the hotkey {}".format(hotkey))

        # [TODO] Sanity check that the hotkey doesn't already exist
        self.hotkeys[hotkey] = function

    def bbb(self):
        testController.type("bcdBCD")

    def run(self):
        # Here we actually register all Global Hotkeys

        logger.log("Starting hotkey listener with {} hotkeys".format(len(self.hotkeys)))

        #self.register("<ctrl>+<alt>+l", aaa)
        self.register("<ctrl>+<alt>+u", self.bbb)

        listener = pynput.keyboard.GlobalHotKeys(self.hotkeys)
        listener.start()

hotkeys = Hotkeys()    # [TODO] Consider if this should be global, like logger, or if we should confine it's scope
