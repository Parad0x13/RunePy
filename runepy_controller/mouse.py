# https://github.com/boppreh/mouse#api
import mouse

# https://pypi.org/project/PyGetWindow/
import pygetwindow

from PIL import ImageGrab
from PIL import Image

import pyperclip

from runepy_common import logger
from runepy_common import globals

from runepy_controller import keyboard

# Coords shows the shadow of the window as well
# [TODO] Fix a bug where if you resize this does not update dynamically
coords = []
def findRunescape():
    global coords
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

    coords.append(rs.left)
    coords.append(rs.top)
    coords.append(rs.width)
    coords.append(rs.height)

# [TODO] Implement xRange, yRange, and durationRange
# Possibly rename them to something more approriate mathematically? Smear?
def move(x, y, rel = False, duration = 0.1, xRange = 0, yRange = 0, durationRange = 0):
    global coords

    mouse.move(x, y, absolute = not rel, duration = duration)

# Change this to click(self, x = -1, y = -1, button = "left", holdPosition = True)
# Where -1 implies current position by default allowing movement to location by default
# holdPosition means it goes back to start otherwise allow you to move the mouse freely
def click(button = "left"):
    mouse.click(button)

def get_position():
    return mouse.get_position()

def get_pixel_color_win32gui(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    #long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.ReleaseDC(i_desktop_window_id, i_desktop_window_dc)
    #return hex(i_colour)
    return i_colour

# [TODO] Find a way to factor out getting the pixel color without recalculating ImageGrab.grab()
def get_custom_overlay_color_value_in_range_PIL(xDelta, yDelta, goal):
    global coords

    mouseLoc = mouse.get_position()
    x = mouseLoc[0] - coords[0] + xDelta
    y = mouseLoc[1] - coords[1] + yDelta

    # [TODO] I don't like how it's grabbing the entire screen, find a way to optimize this
    img = ImageGrab.grab(bbox = (coords[0], coords[1], coords[0] + coords[2], coords[1] + coords[3]))

    # We don't want to crash if the mouse goes outside the bounds of the screen
    if x < coords[0] or x >= coords[2] or y < coords[1] or y >= coords[3]: return

    rgb = img.getpixel((x, y))

    # We don't care if the rgb doesn't match the goal
    # We can pass custom value calculation as an optimization
    if sum(rgb) != goal: return None

    # [NOTE] Aaron came up with this, I'm not that smart
    # It iterates over 'length' and calculates a custom value depending on the cursor overlay text
    # This is an arbitrary value that seems to work well
    length = 30

    totalA = 0
    for n in range(-length, length):
        rgbA = img.getpixel((x + n, y + 14))
        totalA += sum(rgbA)

    totalB = 0
    for n in range(-length, length):
        rgbB = img.getpixel((x + n, y + 10))
        totalB += sum(rgbB)

    total = int("{}{}".format(totalA, totalB))
    if total != 0: return total

    return total

    '''desktop = os.path.expanduser("~/Desktop")
    path = "{}/test.png".format(desktop)
    img.save(path)'''

def get_overlay_calculation():
    # 23 pixels high, down 36 for first black
    val = get_custom_overlay_color_value_in_range_PIL(xDelta = 0, yDelta = 36, goal = 0)

    knownVals = {
        # Useful
        1221611348: "Chop down Tree",
        1337311348: "Chop down Oak",
        1073511544: "Chop down Willow",
        1267511280: "Chop down Yew",
        1444210066: "Chop down Dead tree",
        1404512214: "Chop down Elder tree",

        119977814: "Mine Copper rock",
        87878082: "Mine Tin rock",
        106627108: "Mine Clay rock",
        106908183: "Mine Iron rock",
        93419211: "Mine Mithril rock",
        132608398: "Mine Adamantite rock",

        940910237: "Smith Anvil",
        1248611495: "Heat Forge",
        1268810466: "Smelt Furnace",
        86368602: "Form Pottery Wheel",
        89767990: "Fire Pottery oven",
        100648024: "Rake Spirit Tree Patch",
        99627854: "Inspect Sprit Tree Patch",
        121979178: "Rake Bush Patch",
        121879451: "Inspect Bush Patch",
        112796900: "Rake Tree patch",
        115927074: "Inspect Tree patch",
        106977338: "Exchange Tool leprechaun",
        109279533: "Pick Onion",
        1169310334: "Listen to Musician",

        102699384: "Net Fishing spot",

        1385610892: "Bank Banker",
        130069885: "Bank Bank booth",
        136009894: "Deposit Bank deposit box",
        1179810744: "Bank Gnome Banker",

        138979582: "Open Door",
        148038536: "Close Door",
        140559981: "Climb-up Stairs",
        147169292: "Climb-up Staircase",
        1318411501: "Climb-down Stairs",
        1305810234: "Climb-down Staircase",
        158349028: "Climb-up Ladder",
        154219220: "Climb Ladder",
        1277610270: "Climb-down Ladder",
        116439793: "Open Drawers",
        120468028: "Search Drawers",
        116099866: "Search Bookcase",
        119837945: "Open Trapdoor",
        120317484: "Open Closed chest",
        125107606: "Search Chest",
        129526926: "Search Crate",
        149019616: "Open Gate",
        149308876: "Close Gate",

        151397033: "Pick Cabbage",
        116758075: "Pick Potato",
        114038687: "Pick Wheat",
        888910172: "Fill Sink",
        119008330: "Fill Waterpump",
        119347650: "Fill Water barrel",
        112648805: "Cook-at Cooking range",

        119469872: "Exit to Burthorpe",

        # Burthorpe's Agility Course
        135928445: "Walk Log Beam",
        1228710729: "Climb-up Wall",
        147969302: "Walk-across Balancing ledge",
        125756900: "Climb-over Obstacle low wall",
        1087010320: "Swing-on Rope swing",
        121399168: "Swing-across Monkey bars",
        1363110443: "Jump-down Ledge",
        1347311576: "Take Empty pot",

        # Less Useful
        1384810444: "Open Sedimentary geode",
        104388840: "Prod Sick-looking sheep (1)",
        114619714: "Take Pideon cage",

        113949019: "Talk-to Jerico",

        104728041: "Attack Rabbit (level: 1)",
        116117089: "Attack Guard (level: 18)",
        81617811: "Attack Man (level: 4)",
        95208534: "Attack Woman (level: 4)",
        121557531: "Attack Guard dog (level: 33)",
    }
    tooltip = "Unknown"
    try: tooltip = knownVals[val]
    except: pass

    return (val, tooltip)

def get_cursor_info(xDelta = 0, yDelta = 0):
    p = get_position()

    #string = "{} = {}".format(p, get_pixel_colour(p[0], p[1]))

    # Beg Experimenting
    return get_pixel_colour(p[0] + xDelta, p[1] + yDelta)##############

    string = "{} = {}".format(p, get_pixel_colour(p[0] + xDelta, p[1] + yDelta))

    # End Experimenting

    #pyperclip.copy(string)
    #spam = pyperclip.paste()

    return string

#i_desktop_window_id = win32gui.GetDesktopWindow()
#i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
logger.log("Mouse Controller Initiating")
findRunescape()
keyboard.registerHotkey("ctrl+alt+c", get_cursor_info, "Grab Cursor Info")
