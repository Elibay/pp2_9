import os
from colorama import Fore, Back, Style
import sys, tty, termios

current_index = 0


def getch(char_width=1):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(char_width)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def draw(path):
    with os.scandir(path) as it:
        index = 0

        for entry in it:

            if index == current_index:
                print(Fore.GREEN + entry.name)
            else:
                print(Fore.RED + entry.name)
            index += 1


while True:
    key = ord(getch())
    os.system("clear")  # windows cls
    draw("..")
    if key == 27:  # Entered ESC
        break
    # if key == 13:  # Enter
    #     print('enter!')
    if key == 60:  # up
        current_index -= 1
        current_index = max(0, current_index)
    if key == 62:  # down
        current_index += 1
        # current_index = max(0, current_index)
