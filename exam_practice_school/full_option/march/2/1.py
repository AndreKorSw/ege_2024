# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((y <= z) or  ( (not(x)) and w)) == (w == z)):
#                     print(x, y, z, w)
# for i in range(1000, 10000):
    # x = str(i)
    # s1 = int(x[0]) + int(x[1])
    # s2 = int(x[1]) + int(x[2])
    # s3 = int(x[2]) + int(x[3])
    # d = sorted([s3, s2, s1], reverse= True)[:2]
    # res = str(d[1]) + str(d[0])
    #
    # if res == "1418":
    #     print(i)
    #     break

# from itertools import permutations
# alph = "полина"
# v = "оаи"
# k = "плн"
# words = permutations(alph)
#
# c = 0
# for w in words:
#     word = "".join(w)
#     flag = True
#     for i in range(len(word) - 1):
#         if (word[i] in v and word[i+1] in v) or (word[i] in k and word[i+1] in k):
#             flag = False
#     if flag:
#         c += 1
# print(c)
# s = 101 * "1"
# while "1111" in s:
#     s = s.replace("1111", "22", 1)
#     s = s.replace("222", "1", 1)
# print(s)

# s = 36**7 + 6**19 - 18
# x= ""
# while s != 0:
#     x += str(s % 6)
#     s //= 6
# print(x)
# print(x.count("5"))

# for a in range(1000):
#     c = 0
#     for x in range(300):
#         for y in range(300):
#             if (3 * x + 4 * y != 70) or (a > x) or (a > y):
#                 c += 1
#     if c == 90000:
#         print(a)
#         break

# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return f(n-1)*n
# print(f(5))

#
# f = open("17 (3).txt")
# g = [int(i) for i in f]
# mx = -1111111111
# c = 0
#
# for i in range(len(g)-1):
#     if g[i] % 3 == 0 or g[i+1] % 3 == 0:
#         c+=1
#         mx = max(mx, g[i] + g[i+1])
# print(c, mx)


# heap = 4
# heaps = 82
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def game_res(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_res(x+1, s), game_res(x, s+1), game_res(x*4, s),game_res(x, s*4)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
# for i in range(1, heaps):
#     if game_res(heap, i) == -1:
#         print("")
# for i in range(1, heaps):
#     if game_res(heap, i) == 2:
#         print("20:", i)
# for i in range(1, heaps):
#     if game_res(heap, i) == -2:
#         print("21: ", i)
#def f(x, y):
#     if x > y or x == 6 or x == 12:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x * 2, y) + f(x + 3, y)
# print(f(3, 16))
# f = open("24 (1).txt")
# d = {}
# g = [i for i in f.readline()]
# for i in range(len(g)):
#     if g[i] == "A":
#         if g[i+1] not in d:
#             d[g[i+1]] = 0
#         d[g[i + 1]] += 1
# # print(d)
# n = 452021+1
# cnt = 0
# while cnt!= 5:
#     diveders = []
#     for i in range(2, n):
#         if n % i == 0:
#             diveders.append(i)
#             m = max(diveders) + min(diveders)
#             if m % 7 == 3:
#                 cnt += 1
#                 print(n, m)
#     n += 1

# n = 452021+1
# cnt = 0
# while cnt != 5:
#     for i in range(2, n):
#         if n % i == 0:
#             m = (i + (n // i))
#             if m % 7 == 3:
#                 cnt+=1
#                 print(n, m)
#             break
#     n+=1
#
