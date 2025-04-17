for i in range(10000):
	n = bin(i)[2:]
	n = '10' + n[2:] + '0' if not n.count('1') % 2 else '11' + n[2:] + '1'
	if int(n, 2) > 19:
		print(i)
		break
