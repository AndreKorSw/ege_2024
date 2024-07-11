from turtle import *
left(90)
for i in range(7):
    forward(10*30)#умножаем на тридцать так как масштаб маленький изначально по заданию 10
    right(120)
#рисуем точки
pu()
for x in range(11):
    for y in range(11):
        goto((x*30, y*30))#домножаем на тридцать чтобы был масштаб 1;1
        dot(5)
done()
# answer 38 dots
