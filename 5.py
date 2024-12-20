def f(n):
	num = ''
	while n > 0:
		num = str(n % 4) + num
		n //= 4
	return num

res = list()
for n in range(10000):
	ch = f(n)
	if n % 4 == 0:
		ch = '2' + ch + '03'
	else:
		ch += f((n % 4) * 5)
	r = int(ch, 4)
	if r <= 567:
		res += [n]
print(max(res))