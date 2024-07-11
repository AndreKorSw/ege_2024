from turtle import *
import time

m = 10
lt(90)
tracer(0)

for i in range(9):
    fd(29*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(3*m)
lt(90)
down()

for i in range(9):
    fd(34*m)
    rt(90)
    fd(84*m)
    rt(90)
up()
for x in range(-25, 25):
    for y in range(-25, 25):
        goto(x*m, y*m)
        dot(3, "red")

update()
time.sleep(100)