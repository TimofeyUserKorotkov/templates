def f(a, b, i, j):
	if a == 30: i = 1
	if a == 60: j = 1
	if a >= b: return a == b and 0 < i + j < 2
	return f(a + 1, b, i, j) + f(a * 2, b, i, j) + f(a * 3, b, i, j)
print(f(10, 70, 0, 0))