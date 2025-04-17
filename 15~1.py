from itertools import *

f = lambda x, b, c: (15 <= x <= 40) <= (((21 <= x <= 63) and not (b <= x <= c)) <= (not (15 <= x <= 40)))
a = product([_ for i in (15, 21, 40, 63) for _ in (i, i + 1, i - 1)], repeat=2)
print(min(c - b for b, c in a if c - b > 0 and all(f(x, b, c) for x in range(100))))
