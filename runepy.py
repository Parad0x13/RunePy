from common import *
from logger import logger
from hotkeys import hotkeys

from time import sleep

from keyboardcontroller import keyboardcontroller

class RunePy:
    def __init__(self):
        logger.log("RunePy Initializing")

        #hotkeys.register("<ctrl>+<alt>+k", self.shutdown)
        #hotkeys.register("<ctrl>+<alt>+l", self.login)

        #hotkeys.register("<ctrl>+<alt>+l", keyboardcontroller.fff)

    def login(self):
        keyboardcontroller.type("hiya")

    def shutdown(self):
        logger.log("RunePy Shutting Down, but not really... this needs to be fixed")

    # [TODO] Don't do this... fix it
    def run(self):
        hotkeys.run()

        while True: sleep(1.0)

bot = RunePy()
bot.run()
