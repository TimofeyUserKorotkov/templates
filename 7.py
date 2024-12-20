for i in range(1, 100):
	v = 1920 * 1080 * i * 50
	if v / 5111000 <= 100:
		print(2**i)