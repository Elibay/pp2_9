def a_plus_b(a):
    global b
    b = 5
    return a + b

x = a_plus_b(5)
print(b)
print(x)
