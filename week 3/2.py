# i = 1
# n = int(input())
#
# s = ""
# while(n > 0):
#     s = f"{s} {i}"
#     i = i * 2
#     n = n - 1
#
n = int(input())
i = 2
is_prime = True
# <= sqrt(n)
# i <= sqrt(n)
# i * i <= n
while i * i <= n:
    if n % i == 0:
        is_prime = False
    i = i + 1

print(is_prime)
