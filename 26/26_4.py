f = sorted(list(map(int, reversed(i.split()))) for i in open('26_4.txt'))

res = [f[0]]
for i in f[1:]:
    if res[-1][0] <= i[1]:
        res.append(i)

print(len(res), max([i for i in f if i[1] >= res[-2][0]])[0])