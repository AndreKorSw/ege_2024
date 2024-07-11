# print("x y x w")
# for x in  range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x == (y <= z)) and ((not(w)) <= (x == y)):
#                     print(x, y, z, w)

# for i in range(10000, 100000):
#     s = str(i)
#     s1 = int(s[0]) + int(s[2]) + int(s[4])
#     s2 =  int(s[1]) + int(s[3])
#     res = str(min(s1, s2)) + str(max(s2,s1))
#     if res == "621":
#         print(i)
#         break


# from itertools import  product
# alph = "АКРУ"
# words = product(alph, repeat = 5)
# for i, w in enumerate(words):
#     word = "".join(w)
#     if word[0] == "К":
#         print(i+1)
#         break

# f = open("Задание 9 (1).csv")
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     povt = [c for c in i if i.count(c) > 1]
#     nepovt = [c for c in i if i.count(c) == 1]
#     if len(set(i)) == 4 and sum(nepovt)/len(nepovt) > sum(povt):
#         c += 1
# print(c)


# s = "1" + 98*"9"
# while "19" in s or "299" in s or "3999" in s:
#     s=s.replace("19", "2", 1)
#     s=s.replace("299", "3", 1)
#     s=s.replace("3999", "1", 1)
# print(s)

# s = 4**12 + 2** 32 - 16
# print(bin(s)[2:].count("1"))

# def f(n):
#     if n == 1:
#          return 1
#     if n == 2:
#         return 1
#     elif n > 2:
#         return  f(n-2) + f(n-1)
# print(f(9))

# f = open("17 (4).txt")
# g = [int(i) for i in f]
# c = 0
# mx = 0
# for i in range(len(g) - 1):
#     for j in range(i+1, len(g)):
#         if (g[i] + g[j])% 60 == 0 and (g[i] % 40 == 0 or g[j] % 40 == 0):
#             c += 1
#             mx = max((mx, g[i] + g[j]))
# print(c, mx)
# from functools import lru_cache
# heaps = 75
# @lru_cache(maxsize=None)
# def game_result(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_result(x+1, s),game_result(x, s+1), game_result(x+s, s), game_result(x, s+x)]
#     negative = [i for i in next_codes if i <= 0]
#     if negative:
#         res = -max(negative) + 1
#     else:
#         res = -max(next_codes)
#     return res
# heap = 7
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
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+1, y) + f(x*2, y)
# print(f(3, 18) * f(18, 37))
# f = open("24 (2).txt")
# g = [str(i) for i in f.readline()]
# c = ""
# mx = 0
# for i in range(len(g)):
#     if g[i] != "E":
#         c+=g[i]
#     else:
#         if c.count("A") > 2:
#             mx = max(mx, len(c))
#         c=""
# print(mx)

# for i in range(2000000, 3000000+1):
#     div_res = []
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             if (i//j) - j <= 115:
#                 div_res.append(i//j - j)
#     if len(div_res) > 2:
#         print(i)
#

# f = open("26 (10).txt")
# #
# colvo_gruz, gruz_capacity = map(int, f.readline().split())
# gruzu = sorted(map(int, f), key = lambda x: (-(210 <= x <= 220), x))
# cur_weight = []
# for i in range(colvo_gruz):
#     if sum(cur_weight) + gruzu[i] <= gruz_capacity:
#         cur_weight.append(gruzu[i])
#     elif sum(cur_weight[:-1]) + gruzu[i] < gruz_capacity:
#         cur_weight = cur_weight[:-1]
#         cur_weight.append(gruzu[i])
# print(len(cur_weight), sum(cur_weight)+1)
