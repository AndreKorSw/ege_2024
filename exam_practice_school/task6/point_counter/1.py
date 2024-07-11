from turtle import *
color("black", "red")
m = 100# масштаб
begin_fill()

#рисуем фигуру
left(90)# всегда
for i in range(3): #только число которое необходимо для фигуры
    forward(111*m)
    right(120)
end_fill()

canvas = getcanvas()
cnt=0
for y in range(-120*m, 120*m, m):
    for x in range(-120*m, 120*m, m):
        item = canvas.find_overlapping(x,y,x,y)
        if len(item) == 1 and item[0] == 5: #если попадаем внутрь фигуры len(item) == 1  и точка лежит не на черной линиии а внутри item[0] == 5
            cnt += 1
print(cnt)
done()
exit()