f = list(map(int, open('files/17.txt')))
mn, k = min(f), []

for i in range(len(f) - 1):
    if mn in (f[i] % 16, f[i + 1] % 16):
        k.append(f[i] + f[i + 1])
print(len(k), max(k))
