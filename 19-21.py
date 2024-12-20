def f(a, m):
	if a <= 33: return m % 2 == 0
	if m == 0: return 0
	h = [f(a - 3, m - 1), f(a - 5, m - 1), f((a + 2) // 3, m - 1)]
	return any(h) if (m - 1) % 2 == 0 else all(h)

print([s for s in range(34, 1000) if f(s, 4) > f(s, 2)])