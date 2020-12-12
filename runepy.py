from logger import logger

from time import sleep

from controller_keyboard import controller as keyboard
from controller_mouse import controller as mouse

from module_mining import module as mining

import os
from PIL import ImageGrab
from PIL import Image

# [TODO] Add a kill switch to all running macros
class RunePy:
    def __init__(self):
        logger.log("RunePy Initializing")

        keyboard.registerHotkey("ctrl+alt+s", self.shutdown, "Shutdown")

    def shutdown(self):
        logger.log("RunePy Shutting Down, but not really... this needs to be fixed")

    # [TODO] Don't do this... fix it
    def run(self):
        while True:
            #sleep(3.0)
            # 23 pixels high, down 36 for first black

            '''         
            coords = mouse.coords()
            img = ImageGrab.grab(bbox = (coords[0], coords[1], coords[0] + coords[2], coords[1] + coords[3]))

            xDelta = 0
            yDelta = 36
            mouseLoc = mouse.get_position()
            x = mouseLoc[0] - coords[0] + xDelta
            y = mouseLoc[1] - coords[1] + yDelta
            point = img.getpixel((x, y))
            '''

            # [NOTE] Aaron came up with this, I'm not that smart
            if sum(point) == 0:
                length = 30

                totalA = 0
                for n in range(-length, length):
                    point = img.getpixel((x + n, y + 14))
                    totalA += sum(point)

                totalB = 0
                for n in range(-length, length):
                    point = img.getpixel((x + n, y + 10))
                    totalB += sum(point)

                total = int("{}{}".format(totalA, totalB))
                if total != 0:
                    print(total)

            '''desktop = os.path.expanduser("~/Desktop")
            path = "{}/test.png".format(desktop)
            img.save(path)'''

            sleep(0.01)

bot = RunePy()
bot.run()
