from itertools import *

print('x y z w')
for x, y, z, w in product(range(2), repeat=4):
    if not (w <= (x == y)) and (z <= x):
        print(x, y, z, w)
