# https://github.com/boppreh/keyboard#api
import keyboard

import time

from runepy_common import logger

logger.log("Keyboard Controller Initiating")

# [TODO] Add sanity checks for duplicate hotkeys
def registerHotkey(hotkey, function, details):
    logger.log("Registering a hotkey {} -> '{}'".format(hotkey, details))
    keyboard.add_hotkey(hotkey, lambda: function())

def removeHotkey(hotkey): pass

def send(code):
    keyboard.send(code)
    time.sleep(0.25)    # Forces command to finish

def write(text):
    keyboard.write(text, delay = 0.025)
    time.sleep(0.25)    # Forces command to finish
