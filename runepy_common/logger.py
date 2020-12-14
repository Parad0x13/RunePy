import os
import time

from runepy_common import globals

def epoch():
    return str(time.time()).split(".")[0]

def log(data, priority = globals.PRIORITY_NORMAL, verbose = False):
    string = "[{}]{}".format(priority, data)

    if verbose:
        desktop = os.path.expanduser("~/Desktop")
        logFile = "{}\\{}_RunePy_Log.txt".format(desktop, epoch())
        with open(logFile, "a") as fh:
            fh.write("{} {}\n".format(epoch(), string))

    print(string)
