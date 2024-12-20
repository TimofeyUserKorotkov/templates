from turtle import *

lt(90)
tracer(0)
screensize(5000, 5000)
m = 20
fd(25 * m); rt(45); fd(50 * m)
up()
bk(50 * m); rt(45); fd(15 * m); lt(90); fd(30 * m)
pd()
rt(180); fd(60 * m); bk(5 * m); rt(90); fd(31 * m)

up()
for x in range(-30, 30):
	for y in range(-30, 30):
		goto(x * m, y * m)
		dot(3, 'red')
update()
done()