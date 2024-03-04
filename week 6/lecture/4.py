import os
from colorama import Fore, Back, Style

path = "../../week 3"

dir_list = os.listdir(path)

print(f"All files and directories in {path} is: ")

dir_list.sort()

# with os.scandir(path) as it:
#     for entry in it:
#         if entry.is_dir():
#             print(Fore.GREEN + entry.name)
#         else:
#             print(Fore.RED + entry.name)
# print()

for i in dir_list:
    full_path = path + "/" + i
    try:
        os.listdir(full_path)
        print(Fore.GREEN + full_path)
    except Exception as e:
        print(Fore.RED + full_path)


# print(x)
