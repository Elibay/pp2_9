# file = open("2.txt", "r", encoding="UTF-8")
# a = file.read()
# print(a)
import re

file = open("row.txt", "r", encoding="UTF-8")
# a = file.rea

# has_finished = False
# while True:
#     a = file.readline()
#     # print(a)
#     if not a:
#         break
#     if has_finished:
#         print(a)
#         has_finished = False
#     if re.match("ИТОГО:", a):
#         has_finished = True

BIN = r"БИН [0-9]{12}"
s = file.read()

print(re.findall(BIN, s))

