from common import *
import logger

class RunePy:
    def __init__(self):
        self.logger = logger.Logger()
        self.logger.log("RunePy Initializing")

bot = RunePy()
