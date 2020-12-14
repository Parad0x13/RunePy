import time

PRIORITY_NORMAL = "+"
PRIORITY_WARN = "?"
PRIORITY_ERROR = "!"

def epoch(): return str(time.time()).split(".")[0]
