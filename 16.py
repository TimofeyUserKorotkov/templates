from sys import *

setrecursionlimit(10**9)
f = lambda n: 1 if n == 1 else n * f(n - 1)
print((f(2024) // 4 + f(2023)) // f(2022))
