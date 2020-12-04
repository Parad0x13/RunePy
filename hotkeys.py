import pynput
from logger import logger

class Hotkeys:
    def __init__(self):
        logger.log("Hotkeys Initiating")

        self.hotkeys = {}

    def register(self, hotkey, function):
        logger.log("Attempting to register the hotkey {}".format(hotkey))

        # [TODO] Sanity check that the hotkey doesn't already exist
        self.hotkeys[hotkey] = function

    def run(self):
        # Here we actually register all Global Hotkeys

        logger.log("Starting hotkey listener with {} hotkeys".format(len(self.hotkeys)))
        listener = pynput.keyboard.GlobalHotKeys(self.hotkeys)
        listener.start()

hotkeys = Hotkeys()    # [TODO] Consider if this should be global, like logger, or if we should confine it's scope
