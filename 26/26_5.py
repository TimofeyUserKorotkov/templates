f = sorted([list(map(int, i.split())) for i in open('26_5.txt')], key=lambda n: n[0])
b = [[0, 0, 0] for _ in range(20)]

for i in f:
    m = min((-1 if _[0] <= i[0] else _[0], b.index(_)) for _ in b)[1]
    if b[m][0] < 1440:
        b[m] = max(b[m][0], i[0]) + i[1], max(b[m][0], i[0]), b[m][2] + 1

print(*min([list(reversed(_)) for _ in b], key=lambda n: [n[0], -1 * n[1]])[:2])