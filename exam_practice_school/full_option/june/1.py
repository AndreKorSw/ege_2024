# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not((x and not(y) or (y == z) or not(w))):
#                     print(x, y, z, w)

# for n in range(1, 1000):
#     s = bin(n)[2:]
#     if n % 3 == 0:
#         s = s + s[-3:]
#     else:
#         s += bin(3 * (n % 3))[2:]
#     if int(s, 2) < 100:
#         print(n)
# from itertools import product
# alph = sorted("КОМПЬЮТЕР")
#
# words = product(alph, repeat = 5)
#
# for i, j in enumerate(words):
#     j = ''.join(j)
#     if j.count('К') == 2 and j[0] != "Ь":
#         if (i + 1) % 2 != 0:
#             print(i + 1, j)

# f = open("09.csv")
# g = [list(map(int, i.split(";"))) for i in f]
# c = 0
# for i in g:
#     if len(set(i)) == 5 and (max(i) + min(i)) * 3 <= (sum(i)- max(i) + min(i)) * 2:
#         c+=1
# print(c)

# for n in range(3, 1000):
#     s = "3" + "5" * n
#     while "25" in s or "355" in s or "555" in s:
#         if "25" in s:
#             s = s.replace("25", "3", 1)
#         if "355" in s:
#             s = s.replace("355", "52", 1)
#         if "555" in s:
#             s = s.replace("555", "23", 1)
#     sm = 0
#     for i in s:
#         sm += int(i)
#     if sm == 27:
#         print(n)
#         break
#
#
#
#
# from ipaddress import ip_network
# net = ip_network("192.168.135.160/255.255.254.0", 0)
# c = 0
# for ip in net:
#     if bin(int(ip))[2:].count("0") > bin(int(ip))[2:].count("1"):
#         c+=1
# print(c)

# alphabet = "0123456789abcdefg"
# mn = 100000000000000000000000
# for x in range(15):
#     # f = int(f'97968{x}13', 15) + int(f'7{x}213', 15)
#     s1 = 9 * 15**7 + 7 * 15 **6 + 9 * 15** 5 + 6 * 15 ** 4 +8 * 15**3 + x * 15** 2 + 1 * 15 + 3
#
#     s2 = 7 * 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 1 * 15 + 3
#     f = s1 + s2
#     if f % 14 == 0:
#         mn = min(mn, f // 14)
# print(mn)

# for a in range(0, 1000):
#     k = 0
#     for x in range(0, 1000):
#         if ((x & 39 == 0) or (((x & 11) == 0) <= ((x & a) != 0))):
#             k += 1
#     if k == 1000:
#         print(a)
#         break

# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n + 3 + f(n + 3)
#
# print(f(23) - f(21))

# f = open("17 (1).txt")2 3214675748
#
# g = [int(i) for i in f]
# min_5 = 10000
# mx_sum = 0
# for i in g:
#     if str(i)[-1] == "5" and 100 <= abs(i) < 1000:
#         min_5 = min(min_5, i)
# c = 0
# for i in range(len(g) - 1):
#     if ((100 <= abs(g[i]) < 1000) or (100 <= abs(g[i+1]) < 1000)) and ((g[i] + g[i + 1]) % min_5 == 0):
#         c += 1
#         mx_sum = max(mx_sum,g[i]** 2 + g[i + 1]** 2)
# print(c, mx_sum)

#одна куча
# from functools import lru_cache
# heap = 78
# @lru_cache(maxsize=None)
# def game_result(s):
#     if s >= heap:
#         return 0
#     next_codes = [game_result(s+1),game_result(s+4), game_result(s*4)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
#
# for i in range(1, heap):
#     if game_result(i) == 1:
#         print("19 ---", i)
# for i in range(1, heap):
#     if game_result(i) == 2:
#         print("20 ---", i)
# for i in range(1, heap):
#     if game_result(i) == -2:
#         print("21 ---", i)
# f = open("24 (1).txt").readline().replace("Q", "*").replace("R", "*").replace("S", "*").split("**")
# print(len(sorted(f, key = lambda x: -len(x))[0]))
# # print(f)