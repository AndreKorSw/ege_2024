# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not(not(x <= z) or (y == w) or y):
#                     print(x, y, z, w)
from functools import lru_cache
from itertools import product

# f = open("1_9.csv")
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     if max(i) < sum(i) - max(i):
#         if i[0] + i[1] == i[2] + i[3] or i[1] + i[2] == i[0] + i[3] or i[3] + i[1] == i[2] + i[0]:
#             c += 1
# print(c)
# mx = 0
# for n in range(3, 10000):
#     s = "7" + "1" * n
#     while "1111" in s or "7777" in s:
#         if "1111" in s:
#             s = s.replace("1111", "77", 1)
#         else:
#             s = s.replace("7777", "1", 1)
#     cur = 0
#     for i in s:
#         cur += int(i)
#
#     mx = max(cur, mx)
# print(mx)

# from ipaddress import ip_network
# net = ip_network("192.168.43.160/255.255.254.0", 0)
# c = 0
# for ip in net:
#     if bin(int(ip))[2:].count("0") > bin(int(ip))[2:].count("1"):
#         c+=1
# print(c)
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n-1)
# for i in range(1, 2025):
#     f(i)
# print((f(2024) - f(2023)) / f(2022))

# f = [0] * 2026
#
# for n in range(1, 2026):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n-1]
# print((f[2024] - f[2023])/f[2022])

# f = open("1_17.txt")
# g =[int(i) for i in f]
# min_19 = min([int(i) for i in g if int(i) % 19 == 0])
# mx= 0
# c = 0
# for i in range(len(g) - 1):
#     if g[i] % min_19 == 0 or g[i+1] % min_19 == 0:
#         c += 1
#         mx = max(mx, g[i] + g[i+1])
# print(c, mx)

from functools import lru_cache
# heaps = 464
# @lru_cache(maxsize=None)
# def game_result(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_result(x+2, s),game_result(x, s+2), game_result(x*3, s), game_result(x, s*3)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
# heap = 13
# for i in range(1, heaps):
#     if game_result(heap, i) == -1:
#         print("19 ---", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == 2:
#         print("20 ---берем последний ответ", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == -2:
#         print("21 --- берем минимальный", i)

# def f(x, y):
#     if x > y or x == 35:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+1, y) + f(x+2, y) +f(x* 2, y)
#
# print((f(4,11)* f(11, 19)* f(19, 45)))

# s = 2*729**2014 + 2 * 243 ** 2016 - 2 * 81**2018 + 2 * 27 **2020 - 2 * 9 ** 2022 - 2024
# x = ""
# while s != 0:
#     x += str(s%27)
#     s//=27
# print(x)
# c = 0
# for i in x:

# alph = "0123456789"
# chet = "12468"
# nechet = "13579"
# words = product(alph, repeat = 12)
# c = 0
# for w in words:
#     word = "".join(w)
#     if word.count("4") == 1 and word[0] != "0":
#         if (word[0] in chet and word[1] in nechet and word[2] in chet and word[3] in nechet and word[4] in chet and word[5] in nechet and word[6] in chet and word[7] in nechet and word[8] in chet and word[9] in nechet and word[10] in chet and word[11] in nechet) or (word[0] in nechet and word[1] in chet and word[2] in nechet and word[3] in chet and word[4] in nechet and word[5] in chet and word[6] in nechet and word[7] in chet and word[8] in nechet and word[9] in chet and word[10] in nechet and word[11] in chet):
#                 c+=1
#
#
# print(c)



f = open("1_24m.txt").readline().replace("Q", "A").replace("R", "A").replace("W", "A").replace("Z", "A").replace("1", "B").replace("2", "B").replace("4", "B").replace("7", "B").strip().split("BB")

print(len(sorted(f, key= lambda x: ("AA" not in x,len(x)))[-1]))