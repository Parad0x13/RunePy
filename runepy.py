from common import *
from logger import logger
from hotkeys import hotkeys

class RunePy:
    def __init__(self):
        logger.log("RunePy Initializing")
        hotkeys.register("<ctrl>+<alt>+k", self.shutdown)
        hotkeys.register("<ctrl>+<alt>+t", self.test)

    def shutdown(self):
        logger.log("RunePy Shutting Down")
        #exit()

    def test(self):
        print("fwewffwefwerwfer")

bot = RunePy()
