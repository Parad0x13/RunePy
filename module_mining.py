import time
from logger import logger

from controller_keyboard import controller as keyboard
from controller_mouse import controller as mouse

class Module_Mining:
    def __init__(self):
        logger.log("Mining Module Initiating")
        keyboard.registerHotkey("ctrl+alt+m", self.mineOre, "Ore Mining")

    # This is still very much a WIP
    def mineOre(self):
        start = mouse.get_position()

        for n in range(5):
            mouse.move(start[0], start[1])
            mouse.click()
            time.sleep(3.0)

module = Module_Mining()
