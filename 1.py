from itertools import *

s = '26 147 456 236 37 134 25'.split()
v = 'gf fe ed da ab ag gb bc cd'.split()

print(*range(1, 8))
for p in permutations('abcdefg'):
	if all(str(p.index(b) + 1) in s[p.index(a)] for a, b in v):
		print(*p)
