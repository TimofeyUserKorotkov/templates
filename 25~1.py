def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d.update((n // i, i))
    return min(d) + max(d) if d else 0

k = 0
for i in range(700000, 999999):
    if (m := f(i)) % 10 == 4:
        print(i, m)
        k += 1
    if k == 5:
        break
