def f(a, b, m):
    if a + b > 80: return m % 2 == 0
    if m == 0: return 0
    m -= 1
    h = (f(a + 1, b, m), f(a * 2, b, m), f(a, b + 1, m), f(a, b * 2, m))
    return any(h) if not m % 2 else all(h)

print([s for s in range(1, 74) if f(7, s, 4) > f(7, s, 2)])
