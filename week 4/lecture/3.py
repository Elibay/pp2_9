a = (i ** 2 for i in range(10))
# (0, 1, 4, 9...)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(a)

# a = {
#     "apple": {
#         "id": 1,
#         "kaz_name": "alma",
#         "sort": "Almaty Aport",
#     },
#     ""
# }
fruits = [
    {
        "id": 1,
        "kaz_name": "alma",
        "sort": "Almaty Aport"
    },
    {
        "id": 2,
        "kaz_name": "banan",
        "sort": "African banana"
    },
]
print(fruits[0]["id"])