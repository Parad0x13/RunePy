import time
from runepy_common import logger

from runepy_controller import keyboard
from runepy_controller import mouse

# This is still very much a WIP
def mineOre():
    start = mouse.get_position()

    for n in range(5):
        mouse.move(start[0], start[1])
        mouse.click()
        time.sleep(3.0)

logger.log("Mining Module Initiating")
keyboard.registerHotkey("ctrl+alt+m", mineOre, "Ore Mining")
