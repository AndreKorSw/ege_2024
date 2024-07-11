from turtle import *
import time

tracer(0)
lt(90)
m = 10
for i in range(2):
    fd(6*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(3*m)
lt(90)
down()
for i in range(2):
    fd(77*m)
    rt(90)
    fd(45*m)
    rt(90)
up()
for x in range(-25, 25):
    for y in range(-25, 25):
        goto(x*m, y*m)
        dot(3, "red")

update()
time.sleep(100)