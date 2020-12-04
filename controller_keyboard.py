# https://github.com/boppreh/keyboard#api
import keyboard

import time

from logger import logger

class Controller_Keyboard:
    def __init__(self):
        logger.log("Keyboard Controller Initiating")

    # [TODO] Add sanity checks for duplicate hotkeys
    def registerHotkey(self, hotkey, function, details):
        logger.log("Registering a hotkey {} -> '{}'".format(hotkey, details))
        keyboard.add_hotkey(hotkey, lambda: function())

    def removeHotkey(self, hotkey): pass

    def send(send, code):
        keyboard.send(code)
        time.sleep(0.25)    # Forces command to finish

    def write(self, text):
        keyboard.write(text, delay = 0.025)
        time.sleep(0.25)    # Forces command to finish

controller = Controller_Keyboard()
