# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(x) and y and z and  not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w))):
#                     print(x, y, z, w)

# mn = 100000
# for n in range(1, 10000):
#     s = bin(n)[2:]
#     s = s + str(s.count("1") % 2)
#     s = s + str(s.count("1") % 2)
#     if int(s, 2) > 123:
#         mn = min(int(s, 2), mn)
# print(mn)
# c = 0
# for s1 in "123456789abcd":
#     for s2 in "0123456789abcd":
#         for s3 in "0123456789abcd":
#             for s4 in "0123456789abcd":
#                 for s5 in "0123456789abcd":
#                     res = s1+s2+s3+s4+s5
#                     if res.count("9") == 1 and ((res.count("a") + res.count("b") + res.count("c") + res.count("d")) <= 3):
#                         c+=1
#
# print(c)
# # #

#
# f = open("09_17603.csv")
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     if len(set(i)) == 4 and (min(i) + max(i)) > (sum(i) - (min(i) + max(i))):
#         c+=1
# print(c)
#
# #
# s = "9" * 81
# while "33333" in s or "999" in s:
#     if "33333" in s:
#          s = s.replace("33333", "99", 1)
#     else:
#         s = s.replace("999", "3", 1)
# print(s)

# from ipaddress import *
# net = ip_network("115.198.0.0/255.254.0.0", 0)
# c = 0
# for ad in net:
#     if bin(int(ad))[2:].count("1") % 5 == 0:
#         c+=1
# print(c)
mx = 0
for x in range(1, 2031):
    s = 6 ** 2030 + 6 ** 100  - x
    s1 = ''
    while s != 0:
        s1 += str(s % 6)
        s //= 6
    mx = max(mx, s1.count("0"))
print(mx)
# for a in range(1, 5000):
#     c = 0
#     for x in range(1, 1000):
#         if (((x % 33) == 0) <= (((x % a) != 0) <= ((x % 242)!= 0))):
#             c +=1
#     if c == 999:
#         print(a)

# f = [1] * 2026
# for n in range(2026):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (n+1) * f[n-1]
# print((f[2024]+3 * f[2023])/f[2022])
# f = open("17_17611.txt")
# g = [int(i) for i in f]
# max_7_4 = 0
# mx = 0
# c = 0
# for i in g:
#     if len(str(abs(i))) == 4 and str(i)[-1] == "7":
#         max_7_4 = max(max_7_4, i)
# for i in range(len(g)-2):
#     d = [g[i], g[i+1], g[i+2]]
#     cnt = 0
#     for i in d:
#         if len(str(abs(i))) == 4 and str(i)[-1] == "7":
#             cnt += 1
#     if cnt >=2 and sum(d) > max_7_4:
#         mx = max(mx,sum(d))
#         c+=1
#
# print(c, mx)
#

# from functools import lru_cache
# heaps = 227
# @lru_cache(maxsize=None)
# def game_result(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_result(x+1, s),game_result(x, s+1), game_result(x*2, s), game_result(x, s*2)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
# heap = 17
# for i in range(1, heaps):
#     if game_result(heap, i) == -1:
#         print("19 ---", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == 2:
#         print("20 ---берем последний ответ", i)
# for i in range(1, heaps):
#     if game_result(heap, i) == -2:
#         print("21 --- берем минимальный", i)
#
# def f(x, y):
#     if x < y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x - 2, y) + f(x//2, y)
# print(f(32, 8)* f(8, 1))