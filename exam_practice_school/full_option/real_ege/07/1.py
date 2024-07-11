# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(not(x <= w) or (y <= z) or not(y)):
#                     print(x, y, z, w)
# f = open('9_17522.csv')
# g = [list(map(int, i.split(','))) for i in f]
# c = 0
# for i in g:
#     if len(set(i)) == 3 and max(i) < (sum(i) - max(i)):
#         c+=1
# print(c)
# s = "9" * 100
# while "33333" in s or "999" in s:
#     if "33333" in s:
#         s = s.replace('33333', "99", 1)
#     else:
#         s = s.replace("999", '3', 1)
#
# print(s)
#
# from ipaddress import *
# ip_nep = ip_network("172.16.128.0/255.255.192.0")
# cnt = 0
# for ip_ad in ip_nep:
#     if bin(int(ip_ad))[2:].count("1") % 2 != 0:
#         cnt+=1
# print(cnt)
from functools import lru_cache


# for n in range(1, 1000):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = "10" + s[2:] + "0"
#     else:
#          s = "11" + s[2:] + "1"
#     if int(s, 2) > 50:
#         print(n)
#         break

# for x in range(2030+1, 1, -1):
#     s = 3**100 - x
#     s1 = ''
#     while s != 0:
#         s1 += str(s % 3)
#         s //= 3
#     if s1.count("0") == 5:
#         print(x)
#         break

#
#
# f = [1] * 2026
#
# for n in range(1, 2026):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n-1]
#
# print((2*f[2024]+f[2023])/f[2022])
#
# f = open('17_17530.txt')
# g = [int(i) for i in f]
# minp = min(g)
# min_s = 10000
# c = 0
# for i in range(len(g) - 1):
#      if g[i] % 55 == minp or g[i + 1] % 55 == minp:
#          c+= 1
#          min_s = min(min_s, g[i] +g[i+1])
# print(c, min_s)
# from functools import lru_cache
# heaps = 65
# @lru_cache(maxsize=None)
# def game_result(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_result(x+1, s),game_result(x, s+1), game_result(x*3, s), game_result(x, s*3)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
# heap = 6
# for i in range(1, heaps):
#     if game_result(heap, i) == -1:
#         print("19 ---", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == 2:
#         print("20 ---берем последний ответ", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == -2:
#         print("21 --- берем минимальный", i)

def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    else:
        return f(x-1, y) + f(x//2, y)

print(f(30, 8)*f(8, 1))