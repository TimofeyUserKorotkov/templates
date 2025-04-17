f, k = sorted(list(map(int, open('26_3.txt')))), 0
res = [_ for _ in f if (k := k + _) <= 8200]
for i in range(8200 - sum(res)):
    if res[-1] + i in f[len(res) - 1:]:
        mx = res[-1] + i
print(len(res), mx)
