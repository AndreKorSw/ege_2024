# f = open("09.csv")
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     if len(set(i)) == len(i):
#         chet = []
#         nechet = []
#         for j in i:
#             if j % 2 == 0:
#                 chet.append(j)
#             else:
#                 nechet.append(j)
#         if len(nechet) > len(chet) and sum(chet) > sum(nechet):
#             c += 1
# print(c)
# from itertools import product
# alph = sorted(["В", "И", "Н", "Т"])
# words = product(alph, repeat = 5)
#
# for i, j in enumerate(words):
#     if i == 1018:
#         print(j)

#
# heap = 4
# heaps = 45
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def game_res(x, s):
#     if x + s >= heaps:
#         return 0
#     next_codes = [game_res(x+1, s), game_res(x, s+1), game_res(x, s*3), game_res(x*3, s)]
#     neg = [i for i in  next_codes if i <= 0]
#     if neg:
#         res = -max(neg) + 1
#     else:
#         res = -max(next_codes)
#     return  res
#
# for i in range(1, heaps):
#     if game_res(heap, i) == 2:
#         print("20-", i)
#
# for i in range(1, heaps):
#     if game_res(heap, i) == -2:
#         print("21-", i)


# f = open("24.txt")
#
# mx=0
# mxall=0
# for s in f:
#     k=1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]: #если буквы совпадают то увеличиваем счетчик длинны максимальной подстроки
#             k+=1
#             if k>mx:
#                 mx=k
#                 mxall=s.count(s[i])# считаем количество максималььно посторяюшихся в строке
#             if k==mx:
#                 mxall = max(s.count(s[i]), mxall)
#         else:
#             k=1
# print(mxall)
# from fnmatch import *
# for i in range(0, 10**10, 4891):
#     if fnmatch(str(i),"1?7602*0"):
#         print(i)


# f = open("17.txt")
# g =[int(i) for i in f]
# mx_13 = 0
# for i in g:
#     if str(i)[-2:] == "13":
#         mx_13 = max(mx_13, int(i))
# count = 1
# mi_sum = 10000
# for i in range(len(g) - 2):
#     d = [g[i], g[i+1], g[i+2]]
#     c = 0
#     for x in d:
#         if 100 <= x < 1000:
#             c+=1
#     if c == 2 and sum(d) < mx_13:
#         count+=1
#         mi_sum = min(mi_sum, sum(d))
# print(count, mi_sum)