from itertools import *

res = list()
for k in range(1, 20):
	cnt = 0
	for x in product('01', repeat=20):
		if x.count('0') == k:
			cnt += 1
	if len(str(cnt)) == 6: res += [[k, [cnt]]]
print(max(res))