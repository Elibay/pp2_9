# a = open("2.txt", "r", encoding="UTF-8")
# print(a.read())
import re
a = open("row.txt", "r", encoding="UTF-8")
s = a.read()
print(s)
reg = r"[0-9]{11}"
print(re.findall(reg, s))

