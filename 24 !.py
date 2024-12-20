f = open('24.txt').readline().split('Y')
res = list()
for i in range(len(f) - 150):
	res += [len('Y'.join(f[i:i + 151]))]
print(max(res))