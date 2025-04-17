f = [list(map(int, _.split())) for _ in open('files/9.txt')]
k = 0
for i in f:
    if max(i) < sum(i) - max(i) and len(set(i)) == 3:
        k += 1
print(k)
