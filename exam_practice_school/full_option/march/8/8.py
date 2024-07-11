# print("x y z w u")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x == (w or y)) or ((w<=z) and (y <= w))):
#                         print(x, y, z, w)
# for n in range(1, 100):
#     s = bin(n)[2:][::-1]
#     for x in s:
#         if x == "0":
#             s=s[1:]
#         else:
#             break
#     if int(s, 2) == 11:
#         print(n)
#
# from itertools import product,permutations
# alph = "ГЕОРГИЙ"
# words = permutations(alph, 7)
# c = set()
# for w in words:
#     word = "".join(w)
#     if "ГГ" not in word:
#         c.add(word)
# print(len(c))
# f = open('09 (2).csv')
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     povt = [c for c in i if i.count(c) > 1]
#     if len(set(i)) < len(i) and i.count(max(i)) == 1 and sum(povt) < max(i):
#         c += 1
# print(c)
#
# for a in range(100):
#     c = 0
#     for x in range(300):
#         for y in range(300):
#             if (y + 2 * x < a) or (x > 30) or (y > 20):
#                 c += 1
#     if c == 90000:
#         print(a)
#         break
# heap = 47
# from functools import lru_cache
# @lru_cache(maxsize = None)
# def game_res(x):
#     if x >= heap:
#         return 0
#     next_codes = [game_res(x+1), game_res(x+4), game_res(x*2)]
#     neg = [c for c in next_codes if c <= 0]
#     if neg:
#         res = -max(neg)+1
#     else:
#         res = -max(next_codes)
#     return res
#
# for i in range(1, heap):
#     if game_res(i) == 2:
#         print("20 ---", i)
# for i in range(1, heap):
#     if game_res(i) == -2:
#         print("21 ---", i)

# for i in range(95632, 95700):
#     dividers = []
#     for j in range(1, i+1):
#         if j % 2 == 0:
#             if i % j == 0:
#                 dividers.append(j)
#     if len(dividers) == 6:
#         print(dividers)
