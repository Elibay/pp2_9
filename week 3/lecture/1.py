a = []
a = [1, 2, "abc", 1.12]
b = (1, 2, "abc", 1.12)
a.append("abc")
# for i in b:
#     print(i, type(i))
n = len(b)
# for (int i = 0; i < n; ++ i) {
#
# }
# print(range(n))
# range(n) = (0...n)
for i in range(n, 0, -1):
    print(i)
