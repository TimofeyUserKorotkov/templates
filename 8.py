from itertools import *

k = 0

for i in product('012121212', repeat=5):
    n = ''.join(i)
    if all(('01' not in n, '10' not in n, n[0] != '0', n.count('0') == 1)):
        k += 1
print(k)