from math import ceil

for i in range(1, 100):
	if ceil(27 * i / 8) * 100000 > 2 * 2**20:
		print(2**i - (2**(i - 1) - 1))
		break