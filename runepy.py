from runepy_common import logger

from time import sleep

from runepy_controller import keyboard
from runepy_controller import mouse

from runepy_module import mining
from runepy_module import camera

import os
import sys

# [TODO] Add a kill switch to all running macros
class RunePy:
    def __init__(self):
        self.running = True

        logger.log("RunePy Initializing")

        keyboard.registerHotkey("ctrl+alt+s", self.shutdown, "Shutdown")

    # [TODO] Make this threadsafe so that logs and other files won't be affected
    def shutdown(self):
        logger.log("RunePy is shutting down")
        self.running = False

    # [TODO] Don't do this... fix it
    def run(self):
        while self.running:
            val = mouse.get_overlay_calculation()
            if val[0] is not None:
                print("Overlay {} = {}".format(val[0], val[1]))

            sleep(0.1)

bot = RunePy()
bot.run()
