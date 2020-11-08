from common import *

class Logger:
    def __init__(self):
        pass

    def log(self, data, priority = PRIORITY_NORMAL):
        print("[{}]{}".format(priority, data))

logger = Logger()
