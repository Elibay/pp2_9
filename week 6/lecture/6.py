import os
from colorama import Fore, Back, Style

path = "../../week 3"

dir_list = os.listdir(path)

print(f"All files and directories in {path} is: ")

dir_list.sort()

current_index = 3

with os.scandir(path) as it:
    index = 0

    for entry in it:

        if index == current_index:
            print(Fore.GREEN + entry.name)
        else:
            print(Fore.RED + entry.name)
        index += 1
