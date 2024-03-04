import os

x = os.getcwd().split('/')  # "/Users/nuptebek/..."-> ["", "Users", "nuptebek", ...]
full_path = ""
our_folder = x.pop()
for i in x:
    full_path += f"{i}/"

print(full_path)
dir_list = os.listdir(full_path)
#
print(f"All files and directories in {full_path} is: ")
#
#
print(dir_list)

print(f"and our folder is {our_folder}")
