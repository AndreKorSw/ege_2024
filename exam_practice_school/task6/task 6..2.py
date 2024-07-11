from turtle import *
left(90)
for i in range(4):
    forward(14*20)
    right(120)
pu()
for x in range(20):
    for y in range(20):
        goto((x*20, y*20))
        dot(5)
done()
