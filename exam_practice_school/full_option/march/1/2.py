# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((x <= y) and (y <= w)) or  (z ==(x or y))):
#                     print(x, y, z, w)
# for i in range(10000, 100000):
#     x = str(i)
#     s1 = int(x[0]) + int(x[2]) + int(x[4])
#     s2 = int(x[1]) + int(x[3])
#     res = str(min(s2, s1)) + str(max(s1, s2))
#     if int(res) == 723:
#         print(i)
#         break
# from itertools import product, permutations
# alph = "ОЛЬГА"
# vow = "АО"
# words = permutations(alph)
# for w in words:
#     word = "".join(w)
#     if word[0] != "Ь":
# s = 2 * 216**6 + 3 * 36 **9 - 432
# x = ""
# while s != 0:
#     x += str(s%6)
#     s //= 6
# print(x.count("5"))

# f = open("17 (2).txt")
# g = [int(i) for i in f]
# mx = 0
# s = 0
# for i in range(len(g) - 1):
#     for j in range(i +1, len(g)):
#         if (g[i] % 160 != g[j] % 160) and  (g[i] % 7 == 0  or g[j] % 7 == 0):
#             mx = max(mx, g[i]+ g[j])
#             s += 1
#
# print(s, mx)
# heap = 7
# heaps = 77
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def game_res(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_res(x+1, s), game_res(x, s+1), game_res(x*2, s),game_res(x, s*2)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
#
#
# for i in range(1, heaps):
#     if game_res(heap, i) == -1:
#         print("19 ---", i)
# for i in range(1, heaps):
#     if game_res(heap, i) == 2:
#         print("20 ---берем последний ответ", i)
# for i in range(1, heaps):
#     if game_res(heap, i) == -2:
#         print("21 --- берем минимальный", i)
# for i in range(123456789, 223456789 + 1):
#     dividers = set()
#     if (i ** 0.5) == int(i ** 0.5):
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 dividers.add(i//j)
#                 dividers.add(j)
#             if len(dividers) > 3:
#                 break
#         if len(dividers) == 3:
#             print(i, max(dividers))
# f = open("inf_22_10_20_26.txt")
# n = int(f.readline())
# tovary = [int(i) for i in f]
# max_price = 0
# sum_tov = 0
# for i in range(tovary):
#
