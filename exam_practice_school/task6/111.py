from turtle import *
# Вперед 10
# Опустить хвост
# Повтори 5 [Вперед -6 Налево 180 Вперед 4 Направо 90]
# Назад 5
# Повтори 8 [Вперед 3 Направо 135 Назад 5 Направо 45]
m = 30 #масштаб
tracer(0)
pu()
forward(10*m)
pd()
for i in range(5):
    forward(-6*m)
    left(180)
    forward(4*m)
    right(90)
forward(-5*m)
for i in range(8):
    forward(3*m)
    right(135)
    backward(5*m)
    right(45)
pu()
for x in range(-25, 25):
    for y in range(-20, 30):
        goto(x*m, y*m)
        dot(3)
done()