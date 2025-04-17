li = [[2, 1, 4], [1, 3, 3], [1, 4, 2], [3, 1, 4], [2, 4, 2]]


def mst(l, ix, lim=10):
	keys = {sum(i[ix[_]] * 10**(lim * (2 - _)) for _ in range(2)): i for i in l}
	return [keys[_] for _ in sorted(keys)]

print(mst(li, (1, 0, 2)))

# t = {1: 231, 5: 1, 354: 21}
# t = sorted(t)
# print(t)