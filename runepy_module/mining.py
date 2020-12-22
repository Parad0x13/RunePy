import time
from runepy_common import logger

from runepy_controller import keyboard
from runepy_controller import mouse

# This is still very much a WIP
def mineOre():
    start = mouse.get_position()

    for n in range(5):
        mouse.move(start[0], start[1])
        mouse.click()
        time.sleep(3.0)

logger.log("Mining Module Initiating")
keyboard.registerHotkey("ctrl+alt+m", mineOre, "Ore Mining")

# This is a horrible search for mining ore rockertunities
import time
def executeRockertunities(goal = "Mine Copper rock"):
    while True:
        try:
            img = screen.get_screenshot()
            vaultX = []
            vaultY = []
            r = 165
            g = 148
            b = 51
            size = 0.05
            for y in range(img.height):
                for x in range(img.width):
                    pixel = img.getpixel((x, y))
                    if pixel[0] > (r * (1.0 - size)) and pixel[0] < (r * (1.0 + size)):
                        if pixel[1] > (g * (1.0 - size)) and pixel[1] < (g * (1.0 + size)):
                            if pixel[2] > (b * (1.0 - size)) and pixel[2] < (b * (1.0 + size)):
                                vaultX.append(x)
                                vaultY.append(y)
            print(len(vaultX))
            xPrime = (sum(vaultX) / len(vaultX)) + screen.coords[0]
            yPrime = (sum(vaultY) / len(vaultY)) + screen.coords[1]
            move(xPrime, yPrime)

            time.sleep(1.0)
            value = get_overlay_calculation()
            print("is")
            print(value)
            if value[1] == goal:
                mouse.click("left")
                time.sleep(1.0)
        except: pass

keyboard.registerHotkey("ctrl+alt+a", testing, "Executing Rockertunities")
