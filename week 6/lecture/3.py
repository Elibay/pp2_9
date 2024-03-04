from colorama import Fore, Back, Style

print(Fore.RED + "some text in red")
print(Back.GREEN + "and background is green")
print(Style.DIM + "and in dim text")

print(Style.RESET_ALL)
print("back to normal")