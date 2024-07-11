# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(not(x <= z) or (y == w) or y):
#                     print(x, y, z, w)

# mn = 100000
# for n in range(1, 10000):
#     s = bin(n)[2:]
#     s = s + str(s.count("1") % 2)
#     s = s + str(s.count("1") % 2)
#     if int(s, 2) > 75:
#         mn = min(int(s, 2), mn)
# print(mn)
# c =0
# for s1 in "123456789aaaaa":
#     for s2 in "0123456789aaaaa":
#         for s3 in "0123456789aaaaa":
#             for s4 in "0123456789aaaaa":
#                 for s5 in "0123456789aaaaa":
#                     res = s1+s2+s3+s4+s5
#                     if res.count("8") == 1 and (res.count("a") >= 2):
#                         c+=1
#
# print(c)
# c =0
# for s1 in "123456789aaaa":
#     for s2 in "0123456789aaaa":
#         for s3 in "0123456789aaaa":
#             for s4 in "0123456789aaaa":
#                 for s5 in "0123456789aaaa":
#                     res = s1+s2+s3+s4+s5
#                     if res.count("9") == 1 and (res.count("a") <= 3):
#                         c+=1
#
# print(c)
# #
# from itertools import product
# c = 0
# for i in product("0123456789aaaa", repeat = 5):
#     x = ''.join(i)
#     if x[0] != "0" and x.count("a") <= 3 and x.count("9") == 1:
#         c +=1
# print(c)
# f = open("9_17628.csv")
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     if (min(i)+ max(i)) <= (sum(i) - (min(i)+ max(i))):
#         c+=1
# print(c)

# s = "9" * 136
# while "22222" in s or "9999" in s:
#     if "22222" in s:
#         s = s.replace("22222", "99", 1)
#     else:
#         s = s.replace("9999", "2", 1)
# print(s)

# from ipaddress import *
# net = ip_network("112.160.0.0/255.240.0.0", 0)
# c = 0
# for ad in net:
#     if bin(int(ad))[2:].count("1") % 5 == 0:
#         c+=1
# print(c)
# for x in range(1, 2031):
#     s = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
#     s1 = ''
#     while s != 0:
#         s1 += str(s % 6)
#         s //= 6
#     if s1.count("0") == 202:
#         print(x)
#         break

# for a in range(1000):
#     c = 0
#     for x in range(300):
#         for y in range(300):
#             if (((x + y) <= 30) or (y <= (x + 2)) or (y >= a)):
#                 c += 1
#     if c == 90000:
#         print(a)

# f = [1] * 2026
#
# for n in range(2026):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = (n+1) * f[n-1]
# print((f[2024] - 3 * f[2023])/f[2022])

# f = open("17_17636.txt")
# g = [int(i) for i in f]
# mx_3_3x = 0
# mx = 0
# c = 0
# for i in g:
#     if str(i)[-1] == "3" and len(str(abs(i))) == 3:
#         mx_3_3x = max(mx_3_3x, i)
# for i in range(len(g) - 2):
#     if (g[i] + g[i+1] + g[i + 2]) <  mx_3_3x and ((str(g[i])[-1] == "3" and len(str(abs(g[i]))) == 3) or (str(g[i+1])[-1] == "3" and len(str(abs(g[i+1]))) == 3) or (str(g[i+2])[-1] == "3" and len(str(abs(g[i+2]))) == 3)):
#         c+=1
#         mx = max(mx, (g[i] + g[i+1] + g[i + 2]))
# print(c, mx)
#одна куча
# from functools import lru_cache
# heap = 39
# @lru_cache(maxsize=None)
# def game_result(s):
#     if s >= heap:
#         return 0
#     next_codes = [game_result(s+1),game_result(s+3), game_result(s*2)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
#
# for i in range(1, heap):
#     if game_result(i) == -1:
#         print("19 ---", i)
# for i in range(1, heap):
#     if game_result(i) == 2:
#         print("20 ---", i)
# for i in range(1, heap):
#     if game_result(i) == -2:
#         print("21 ---", i)


# def f(x, y):
#     if x < y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x - 2, y) + f(x//2, y)
# print(f(32, 14)* f(14, 1))
# cnt = 0
# n = 700000
# while cnt != 5:
#     for i in range(2, n+1):
#         if n % i == 0:
#             if str((i + n//i))[-1] == "4":
#                 print(n, i+n//i)
#                 cnt += 1
#             break
#     n +=1

# from fnmatch import fnmatch
# for i in range(0, 10**10+1, 8993):
#     if fnmatch(str(i), '89*4?5?7?'):
#         print(i, i // 8993)


# ищет целые число большие 800000 у кот делитель оканч на 9 и не равен 9
# в ответ первые 5 чисел и для каждого минимальный делитель
# def div(x):
#     d = set()
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             d |= {i, x // i}
#     return sorted(d)
#
# for x in range(800001, 800100):
#     d = [i for i in div(x) if i % 10 == 9 and i != 9]
#     if len(d) > 0:
#         print(x, min(d))