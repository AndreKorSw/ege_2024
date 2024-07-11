# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((z <= (x == w)) or not(y <= w)):
#                     print(x, y, z, w)
#
from functools import lru_cache

# 5---------
# mn = 1000
# for n in range(1, 1000):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = "1" + s + "0"
#     else:
#         s = "11" + s + "11"
#     if int(s, 2) > 48:
#         mn = min(mn, (int(s,2)))
# print(mn)

# # 6------------
# from turtle import *
# from time import sleep
# screensize(2000, 2000)
# tracer(0)
# m = 10
#
# lt(90)
#
# for i in range(3):
#     fd(20*m)
#     rt(90)
#     fd(39 * m)
#     rt(90)
# up()
# lt(90)
# backward(16*m)
# rt(90)
# fd(29*m)
# lt(180)
# down()
# for i in range(2):
#     fd(23*m)
#     rt(90)
#     fd(25*m)
#     rt(90)
# up()
#
# for x in range(-25, 60):
#     for y in range(-25, 25):
#         setpos(x*m, y*m)
#         dot(5, "red")
#
# update()
# done()
# 8------------
# from itertools import product
# bad = ["01", "10", "21", "12", "41", "14", "61", "16", "18", "81"]
# count = 0
#
# words = product("012345678", repeat = 5)
# for w in words:
#     word = "".join(w)
#     if word[0] != "0" and word.count("1") == 1:
#         c = 0
#         for x in bad:
#             if x in word:
#                 c += 1
#         if c == 0:
#             count += 1
# print(count)
#
#
#
# 9----------------
# f = open("9.csv")
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     for x in i:
#         if i.count(x) == 3 and min(i) < x < max(i) and len(set(i)) == 5:
#             c+=1
#             break
# print(c)

# 13--------

# from ipaddress import *
# net = ip_network("235.86.56.0/255.255.248.0", 0)
# c = 0
# for ad in net:
#     if bin(int(ad))[2:].count("1") - bin(int(ad))[2:].count("0") >= 2:
#         c +=1
# print(c)

# 14---------
# for x in range(1, 2031):
#     s1 = ""
#     s = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
#     while s != 0:
#         s1 += str(s % 6)
#         s //= 6
#     sm = 0
#     for i in s1:
#         sm += int(i)
#     if sm == 300:
#         print(x)

# 15---------


# for a in range(300):
#     c = 0
#     for x in range(1, 1000):
#         if ():
#             c+=1
#     if c == 999:
#         print(a)

# 16-----------
# f = [1] * 21100
# for n in range(21000, 1, -1):
#     if n > 20024:
#         f[n] = n
#     if n <= 20024:
#         f[n] = 3 * f[n+1]
# print((f[2022] + f[2021])/f[2024])
# кучи______________
# heap = 273
# @lru_cache(None)
# def gameres(x):
#     if x >= heap:
#         return 0
#     nextcodes = [gameres(x+2), gameres(x+5), gameres(x*4)]
#     negative = [i for i in nextcodes if i <= 0]
#     if negative:
#         return -max(negative)+1
#     else: return -max(nextcodes)
#
# for i in range(1, heap):
#     if gameres(i) == -1:
#         print("19)", i)
# for i in range(1, heap):
#     if gameres(i) == 2:
#         print("20)", i)
# for i in range(1, heap):
#     if gameres(i) == -2:
#         print("21)", i)
# def f(x, y):
#     if x > y or x == 9:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+2, y) + f(x+3, y) + f(x*2, y)
# print(f(3, 15)*f(15, 25))

# def div(x):
#     d = set()
#     for i in range(2, int(x**0.5)+1):
#         if x % i == 0:
#             # if
#             d.add(i)
#             d.add(x//i)
#     return sorted(d)
#
# for x in range(800001, 800100):


# n = 600001
# cnt = 0
#
# while cnt != 5:
#     for i in range(17, n, 10):
#         if n % i == 0:
#             print(n, i)
#             cnt +=1
#             break
#     n +=1



    # d = div(x)
    # if d:
    #     m = max(d) + min(d)
    #     if m % 10 == 4:
    #         print(x, m)

# from itertools import product
#
# alph = "0123456789abcdefg"
# print(len(alph))
# c = 0
# words = product(alph, repeat = 5)
# for w in words:
#     word = "".join(w)
#     if word[0] != "0" and word.count("3") == 1:
#         if (word.count("d") + word.count("e") + word.count("f") + word.count("g")) <= 3:
#             c+=1
#
# print(c)