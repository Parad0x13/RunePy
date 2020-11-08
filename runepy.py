from common import *
from logger import logger
from hotkeys import hotkeys

class RunePy:
    def __init__(self):
        logger.log("RunePy Initializing")
        hotkeys.register("^!K", self.shutdown)

    def shutdown(self):
        logger.log("RunePy Shutting Down")

bot = RunePy()
