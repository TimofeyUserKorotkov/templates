f = open('26.txt').readlines()
n, e = int(f[0]), [list(map(int, i.split())) for i in f[1:]]
print(n, e)