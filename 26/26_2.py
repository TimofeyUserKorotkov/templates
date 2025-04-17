f = sorted(list(map(int, open('26_2.txt'))), reverse=True)
cs = [f[0]]
for i in f[1:]:
    if cs[-1] - i > 8:
        cs.append(i)
print(len(cs), cs[-1])
