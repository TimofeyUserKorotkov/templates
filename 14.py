def f(n, s):
    r = ""
    while n > 0:
        r = str(n % s) + r
        n = n // s
    return r


for i in range(2031, 0, -1):
    s = 3**100 - i
    if f(s, 3).count('0') == 1:
        print(i)
        break
