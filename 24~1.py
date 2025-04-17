f = open('files/24.txt').readline().split('AB')
res = []
for i in range(len(f) - 100):
    res.append(len('AB'.join(f[i:i + 101])))
print(max(res) + 2)
