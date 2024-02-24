import random
def calculate(a, b, c):
    print(a, b, c)
    return a * b * c

def f(a, b, c):
    for i in range(10):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        yield calculate(x, y, z)

a = f(1, 2, 3)
print(next(a))
print("hello")
print("hello")
print("hello")
print("hello")
print(next(a))
print("hello2")
print(next(a))