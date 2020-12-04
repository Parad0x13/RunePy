import os
import time

from common import *

class Logger:
    def __init__(self):
        self.desktop = desktop = os.path.expanduser("~/Desktop")
        self.logFile = "{}\\{}_RunePy_Log.txt".format(self.desktop, self.epoch())

    def epoch(self):
        return str(time.time()).split(".")[0]

    def log(self, data, priority = PRIORITY_NORMAL):
        string = "[{}]{}".format(priority, data)

        with open(self.logFile, "a") as fh:
            fh.write("{} {}\n".format(self.epoch(), string))

        print(string)

logger = Logger()
