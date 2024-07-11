from turtle import *
left(90)
for i in range(4):
    forward(9*20)
    right(90)
    forward(7*20)
    right(90)
pu()
for x in range(15):
    for y in range(15):
        goto((x*20, y*20))
        dot(5)
done()