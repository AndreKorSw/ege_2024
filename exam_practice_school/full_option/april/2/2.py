# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if ((y <= x) == (w <= (not (z)))) and (w or x):
#                     print(x, y, z, w)
# import inspect

# def summ(x):
#     if x.count("1")%2 != 0:
#         x+="1"
#     else:
#         x += "0"
#     return  x
#
# c=0
# for n in range(1, 10000000000):
#     s = bin(n)[2:]
#     s = summ(s)
#     s = summ(s)
#     if 987654321 <= int(s, 2) <= 2123456789:
#         c+=1
# print(c)


# from itertools import product
# c = 0
# alph = "метро"
# words = product(alph, repeat = 4)
# for i in words:
#     word = "".join(i)
#     if word[0] in "мтр" and word[-1] in "ео":
#         c+=1
# print(c)

# f = open("Задание 9.csv")
# g = [list(map(int, i.split(","))) for i in f]
# for i in g:
#     if len(set(i)) == 4 and
# alph = "0123456789abcdefgh"
# for x in alph:
#     if (int(f"{x}a04", 13) + int(f"1d{x}3", 18)) % 184 == 0:
#         print((int(f"{x}a04", 13) + int(f"1D{x}3", 18)) // 184)
#         break

# f = open("17.txt")
# g = [int(i) for i in f]
# min_7 = 0
# for i in range(len(g)):
#     if abs(g[i]) % 10 == 7:
#         min_7 = min(min_7, g[i])
# max_pair = 0
# c = 0
# for i in range(1,len(g)):
#     if (str(g[i-1])[-1] == str(g[i])[-1]) and (g[i-1]% 7 == 0 or g[i]% 7 == 0) and ((g[i]**2 + g[i-1]**2) <= min_7):
#         c+=1
#         max_pair =max(max_pair, (g[i]**2 + g[i-1]**2))
# print(c, max_pair)
from functools import lru_cache

heap = 65
@lru_cache(maxsize=None)
def gameres(x):
    if x >= heap:
        return 0
    nextcodes = [gameres(x*4), gameres(x+1)]
    negative = [c for c in nextcodes if c <= 0]
    if negative:
        res = -max(negative) + 1
    else:
        res = -max(nextcodes)
    return res
for i in range(1, heap):
    if gameres(i) == -1:
        print("19 ---", i)
for i in range(1, heap):
    if gameres(i) == 2:
        print("20 ---", i)
for i in range(1, heap):
    if gameres(i) == -2:
        print("21 ---", i)

