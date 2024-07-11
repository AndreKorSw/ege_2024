heap = 39
from functools import lru_cache
@lru_cache(None)
def gameres(a):
    if a >= 65:
        return 0
    if a * 3 >= 109: #допусловие если набирает 109 то проигрывает
        nextcodes = [gameres(a + 5), gameres(a + 7)]
    else:
        nextcodes = [gameres(a + 5), gameres(a + 7), gameres(a * 3)] #список с возможными ходами
    negative = [i for i in nextcodes if i <= 0] #список с отрицательными ходами
    if negative:
        return -max(negative) + 1 #выигрыш Пети
    else:
        return -max(nextcodes) # выйгрыш Вани
# могут поменять 20 и 21 местами
for i in range(1, heap):
    if gameres(i) == 1: # -1
        print("19 ---", i)
for i in range(1, heap):
    if gameres(i) == -2: #найдите два минимальных значения S таких,
    # при котором Ваня совершает не более двух ходов и выигрывает.
        print("20 ---", i)
for i in range(1, heap):
    if gameres(i) == 2:# Петя выигрывает, сделав не более двух ходов.
    # Укажите минимальное и максимальное значения S,
    # если известно, что Петя не может гарантированно выиграть, сделав один ход.
        print("21 ---", i)