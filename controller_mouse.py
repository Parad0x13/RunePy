# https://github.com/boppreh/mouse#api
import mouse

# https://pypi.org/project/PyGetWindow/
import pygetwindow

from common import *
from logger import logger

from controller_keyboard import controller as keyboard

class Controller_Mouse:
    def __init__(self):
        logger.log("Mouse Controller Initiating")
        self.findRunescape()

    def findRunescape(self):
        rs = pygetwindow.getWindowsWithTitle('RuneScape')

        if len(rs) == 0:
            logger.log("Could not find RuneScape", priority = PRIORITY_ERROR)
            exit()
        elif len(rs) == 1:
            logger.log("Found RuneScape")
            self.rs = rs[0]
            self.rs.restore()
            self.rs.activate()
        else:
            logger.log("Found multiple windows of RuneScape", priority = PRIORITY_ERROR)
            exit()

    # This doesn't seem to report correct dimensions...
    # Or at least not the actual game window itself that is
    # It also seems to account for the "shadow" of the window as well
    # This may not really turn out to be a real issue however...
    def coords(self):
        retVal = []
        retVal.append(self.rs.left)
        retVal.append(self.rs.top)
        retVal.append(self.rs.width)
        retVal.append(self.rs.height)
        return retVal

    # [TODO] Implement xRange, yRange, and durationRange
    # Possibly rename them to something more approriate mathematically? Smear?
    def move(self, x, y, rel = False, duration = 0.1, xRange = 0, yRange = 0, durationRange = 0):
        win = self.coords()

        mouse.move(x, y, absolute = not rel, duration = duration)

    # Change this to click(self, x = -1, y = -1, button = "left", holdPosition = True)
    # Where -1 implies current position by default allowing movement to location by default
    # holdPosition means it goes back to start otherwise allow you to move the mouse freely
    def click(self, button = "left"):
        mouse.click(button)

    def get_position(self):
        return mouse.get_position()

controller = Controller_Mouse()
