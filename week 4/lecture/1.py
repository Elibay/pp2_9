# def a_plus_b(a):
#     global b
#     b = 5
#     return a + b

# x = a_plus_b(5)
# print(b)
# print(x)


def a_plus_b(a):
    # def get_b():
        # return 5
    global b
    b = 5
    return a + b

# print(a_plus_b(1))
# # print(get_b())
# print(b)
# b = 6
# print(b)
# print(a_plus_b(1))



# a = ("apple", "banana", "orange")

# i = iter(a)
# # next(i)
# print(next(i))
# # next(i)
# print(next(i))
# # next(i)
# print(next(i))
# print(next(i))
# for i in a:
    # print(i)

# a = (i ** 2 for i in range(1, 7))
# # a = (1, 4, 9, 16, 25, ... 7 * 7)
# for i in a:
#     print(i)
# print(a)

import datetime

x = datetime.datetime.now()
print(x.strftime("%d.%m.%Y"))
