# print("x y z w")
# for x in  range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x and not(y)) or (y == z) or w):
#                     print(x, y, z, w)

# for n in range(1000000, 1, -1):
#     r = bin(n)[2:]
#     if n % 5 == 0:
#         r += bin(5)[2:]
#     else:
#         r += '1'
#     if int(r, 2) % 7 == 0:
#         r += bin(7)[2:]
#     else:
#         r += '1'
#     if int(r, 2) < 1855663:
#         print(n)
#         break

# for i in range(200, 500):
#     s = "1" * i
#     while "111" in s or "222" in s:
#         s = s.replace("111", "22", 1)
#         s = s.replace("222", "1", 1)
#     if not "2" in s:
#
#         print(s, i)
#         break
#
# def f(x, y):
#     if x > y or x == 10:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+1, y) + f(x*2, y)
#
# def f1(x, y):
#     if x > y or x == 9:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f1(x + 1, y) + f1(x * 2, y)
# print(f(1, 9) * f(9, 20) + f1(1, 10) * f1(10, 20) )
#
# for a in range(1, 100):
#     c = 0
#     for x in  range(1, 1000):
#         if ((72 % x == 0) <= (90 % x != 0) or ((a - x) > 80)):
#             c+=1
#     if c == 999:
#         print(a)
#         break
# from functools import lru_cache
# heaps = 141
# @lru_cache(maxsize=None)
# def game_result(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_result(x+1, s),game_result(x, s+1), game_result(x*4, s), game_result(x, s*4)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
# heap = 9
# for i in range(1, heaps):
#     if game_result(heap, i) == -1:
#         print("19 ---", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == 2:
#         print("20 ---берем последний ответ", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == -2:
#         print("21 --- берем минимальный", i)
for i in range(489421, 489440):
    diveders = []
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            diveders.append(i)
    if len(diveders) == 4:
        print(diveders)