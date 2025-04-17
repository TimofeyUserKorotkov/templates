f = [list(map(int, _.split())) for _ in open('26_1.txt').readlines()]
pls = [99907] * 6662

for i, j in f:
    pls[j] = min(pls[j], i)

res = [(min(pls[i], pls[i + 1]) - 1, i) for i in range(len(pls) - 1)]
print(*max(res))
