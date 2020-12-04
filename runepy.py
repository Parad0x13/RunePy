from logger import logger

from time import sleep

from controller_keyboard import controller as keyboard
from controller_mouse import controller as mouse

from module_mining import module as mining

# [TODO] Add a kill switch to all running macros
class RunePy:
    def __init__(self):
        logger.log("RunePy Initializing")

        keyboard.registerHotkey("ctrl+alt+s", self.shutdown, "Shutdown")

    def shutdown(self):
        logger.log("RunePy Shutting Down, but not really... this needs to be fixed")

    # [TODO] Don't do this... fix it
    def run(self):
        while True: sleep(3.0)

bot = RunePy()
bot.run()
