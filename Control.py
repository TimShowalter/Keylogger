# Control & listen to mouse
# Control & listen to keyboard

from pynput.mouse import Controller
from pynput.keyboard import Controller

# left -> right, top to bottom
# Top left of screen is (0, 0)

def ControlMouse():
    mouse = Controller()
    mouse.position = (10, 20)

def ControlKeyboard():
    keyboard = Controller()
    keyboard.type("Let's Go!")

ControlKeyboard()