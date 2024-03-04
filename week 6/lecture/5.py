# from msvcrt import getch if you use windows you can use this command
# from msvcrt import getch

import sys, tty, termios


def getch(char_width=1):
    '''get a fixed number of typed characters from the terminal.
    Linux / Mac only'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(char_width)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# print(ord(getch()))
# "<>"

while True:
    key = ord(getch())
    if key == 27:  # Entered ESC
        break
    if key == 13:  # Enter
        print('enter!')
    if key == 60:  # up symbol <
        print('up!')
    if key == 62:  # downl symbol >
        print('down!')
