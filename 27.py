from math import dist; xys = set(tuple(map(float, i.replace(',', '.').split(' '))) for i in open('27_A.txt'))
cs = lambda cl: min([(sum(dist(i, j) for j in cl), i) for i in cl])[1]; c = list()
while xys:
	c += [[xys.pop()]]
	for i in c[-1]: e = set([j for j in xys if dist(i, j) < 1]); c[-1] += e; xys -= e
m = [j for j in [i for i in c if len(i) > 10]]
print(*map(int, [sum(cs(i)[0] for i in m) / len(m) * 10**2, sum(cs(i)[1] for i in m) / len(m) * 10**2]))


# d1st = lambda c, p: ((p[0] - c[0])**2 + (p[1] - c[1])**2)**(1 / 2); c = list()
# print(*[len(i) for i in c], sep="\n")