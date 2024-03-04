import os

x = os.getcwd()

path = "../../"

dir_list = os.listdir(path)

print(f"All files and directories in {path} is: ")

print(dir_list)

dir_list.sort()

print(dir_list)
# print(x)
