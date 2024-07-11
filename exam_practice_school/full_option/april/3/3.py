# from functools import lru_cache
# heap = 69
#
# @lru_cache(None)
# def gameres(s):
#     if s >= heap:
#         return 0
#     nextcodes = [gameres(s+1), gameres(s+4), gameres(s*5)]
#     negative = [i for i in nextcodes if i <= 0]
#     if negative:
#         res = -max(negative)+1
#     else:
#         res = -max(nextcodes)
#     return res
#
# for i in range(1, heap):
#     if gameres(i) == -1:
#         print(i)
# for i in range(1, heap):
#     if gameres(i) == 2:
#         print(i)
# for i in range(1, heap):
#     if gameres(i) == -2:
#         print(i)
# for i in range(1, 100):
#     s = bin(i)[2:]
#     if i % 2 == 0:
#         s += "10"
#     else:
#         s+= "01"
#     if int(s, 2) <= 102:
#         print(int(s, 2))

f = open("9_2024 (1).csv")
g = [list(map(int, i.split(","))) for i in f]
c = 0
for i in g:
    if len(set(i)) == 4 and ((sum(i) - sum(set(i))) / 2) < sum(i)/len(i):
        c+=1
print(c)