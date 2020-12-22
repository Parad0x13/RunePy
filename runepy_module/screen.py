from runepy_common import globals
from PIL import ImageGrab
from PIL import Image
from runepy_common import logger
from runepy_controller import mouse
from runepy_module import screen

# https://pypi.org/project/PyGetWindow/
import pygetwindow

# Coords shows the shadow of the window as well
# [TODO] Fix a bug where if you resize this does not update dynamically
coords = []
def findRunescape():
    coords = globals.coords
    rs = pygetwindow.getWindowsWithTitle('RuneScape')

    valid = None
    for n in rs:
        if n.title == "RuneScape": valid = n
    rs = valid

    if rs == None:
        logger.log("Could not find RuneScape", priority = PRIORITY_ERROR)
        exit()

    logger.log("Found RuneScape")
    if rs.isMinimized: rs.restore()
    else: rs.activate()

    coords = []
    coords.append(rs.left)
    coords.append(rs.top)
    coords.append(rs.width)
    coords.append(rs.height)

def get_screenshot():
    coords = globals.coords

    # [TODO] I don't like how it's grabbing the entire screen, find a way to optimize this
    return ImageGrab.grab(bbox = (coords[0], coords[1], coords[0] + coords[2], coords[1] + coords[3]))

def get_pixel_color_win32gui(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    #long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.ReleaseDC(i_desktop_window_id, i_desktop_window_dc)
    #return hex(i_colour)
    return i_colour