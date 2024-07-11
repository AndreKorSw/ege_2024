from turtle import *
left(90)
for i in range(4):
    forward(10*10)
    right(90)
pu()
for x in range(15):
    for y in range(15):
        goto((x*10, y*10))
        dot(5)
done()