# print("x y z w")
# for x in  range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not(((not(x) or z) == (y and not(w))) <= (z and y)):
#                     print(x, y, z, w)
from itertools import permutations


# def summ_(x):
#     return str(x.count("1") % 2)
#
#
# # for i in range(1, 100):
#     s = bin(i)[2:]
#     s += summ_(s)
#     s += summ_(s)
#     if int(s,2) > 55:
#         print(int(s, 2))
#         break
#
# from itertools import product
# alph = sorted(["А", "Л", "Г", "О", "Р", "И", "Т", "М"])
# words = product(alph, repeat = 4)
# for i, j in enumerate(words):
#     w = "".join(j)
#     print(w)
#     if w[0] == "Г" and w[1] == "О":
#         print(i+1)
#         break

# f = open("107_9 (3).csv")
# g = [list(map(int, i.split(","))) for i in f]
# q = 0
# for u in g:
#     if all(n[0] + n[1] > n[2] for n in permutations(u, 3)):
#         q += 1
# print(q)
# s = 49 ** 6 + 7 ** 19 - 21
# x = ""
#
# while s != 0:
#     x += str(s%7)
#     s //= 7
# print(x.count('0'))

# for a in range(100, 0, -1):
#     c = 0
#     for x in range(1, 100):
#         if (120 % a == 0) and ((x % a != 0) <= ((x % 18 == 0) <= (x % 24 != 0))):
#             c += 1
#     if c == 99:
#         print(a)

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 0:
#         return n + f(n - 3)
#     if n % 3 > 0:
#         return n + f(n - (n % 3))
# print(f(26))

# from fnmatch import *
# for i in range(0, 10**9, 3127):
#     if fnmatch(str(i), "12*93?1?"):
#         print(i)
f = open("26_59821.txt")
n = int(f.readline())
detali = []
for i in f:
    shlif, pokras = i.split()[0], i.split()[1]
    detali.append([int(shlif), int(pokras)])
print(sorted(detali))