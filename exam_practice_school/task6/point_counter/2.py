import turtle, tkinter
from tkinter import *
from turtle import color, begin_fill, forward, right, end_fill, getcanvas, done
color("black", "red")
m = 100
begin_fill()
for i in range(4):
    forward(25*m)
    right(90)
end_fill()
canvas = getcanvas()
cnt = 0
for y in range(-100*m, 100*m, m):
    for x in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            cnt += 1
print(cnt)
done()
exit()

