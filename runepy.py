from common import *
from logger import logger
from hotkeys import hotkeys

from time import sleep

class RunePy:
    def __init__(self):
        logger.log("RunePy Initializing")
        hotkeys.register("<ctrl>+<alt>+k", self.shutdown)

    def shutdown(self):
        logger.log("RunePy Shutting Down, but not really... this needs to be fixed")

    # [TODO] Don't do this... fix it
    def run(self):
        hotkeys.run()

        while True: sleep(1.0)

bot = RunePy()
bot.run()
