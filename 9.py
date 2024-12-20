cnt = 0
for x in open('246.txt'):
	a = sorted(map(int, x.split()))
	if a[0]**2 <= sum(a[1:]) and sum(d % 2 for d in a) == 2:
		cnt += 1
print(cnt)