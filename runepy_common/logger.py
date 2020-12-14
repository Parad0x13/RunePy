import os

from runepy_common import globals

def log(data, priority = globals.PRIORITY_NORMAL, verbose = True):
    string = "[{}]{}".format(priority, data)

    if verbose:
        local = "./local_logs"
        logFile = "{}\\{}_RunePy_Log.txt".format(local, globals.epoch())
        if not os.path.exists(local):
            os.makedirs(local)
        with open(logFile, "a") as fh:
            fh.write("{} {}\n".format(globals.epoch(), string))

    print(string)
