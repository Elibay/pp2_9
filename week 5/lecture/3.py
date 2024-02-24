import re
s = "+77771777777"

s = r"a\n\na"
# print(s)
print(re.match(r"^\+[0-9]{11}", s))
