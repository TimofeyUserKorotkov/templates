a = [int(x) for x in open('246.txt')]
m = min(a)
tr = []
for i in range(len(a) - 2):
	if abs(a[i] + a[i + 1] + a[i + 2]) % 10 == abs(m) % 10 and sum(x >= 0 for x in a[i:i + 3]) < 2:
		tr += [abs(a[i] + a[i + 1] + a[i + 2])]
print(len(tr), max(tr))