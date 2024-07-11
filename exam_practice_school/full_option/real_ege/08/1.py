# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((y <= (not(x <= z))) or w):
#                     print(x, y, z, w)
# mx = 0
# for n in range(1, 13):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = "10" + s
#     else:
#         s = "1" + s + "01"
#
#     mx = max(mx, int(s, 2))
# # print(mx)
# from itertools import product
#
# alph =  sorted("косуф")
# words = product(alph, repeat = 5)
# for i, j in enumerate(words):
#     j = "".join(j)
#     if j.count("у") == 2 and j.count("ф") == 0:
#         print(i+1, j)
#
# f = open('09_17550.csv')
# g = [list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     povt = []
#     nepovt = []
#     for j in i:
#         if i.count(j) > 1:
#             povt.append(j)
#         else:
#             nepovt.append(j)
#     if len(set(i)) == 4 and (sum(povt))**2 > (sum(nepovt))**2:
#         c+=1
# print(c)

# s = '8'* 83
# while '111' in s or '88888' in s:
#     if '111' in s:
#         s = s.replace("111", '88', 1)
#     else:
#         s = s.replace("88888", "8", 1)
# print(s)
#
# from ipaddress import ip_network
# c = 0
# net = ip_network("112.160.0.0/255.240.0.0", 0)
# for ad in net:
#     if bin(int(ad))[2:].count("1") % 3 != 0:
#         c +=1
# print(c)

# for x in range(1, 2031):
#     s = 7 **91 + 7 **160 - x
#     s1 = ""
#     while s != 0:
#         s1 += str(s%7)
#         s//=7
#     if s1.count("0") == 70:
#         print(x)
# b = range(70,91)
# for a in range(1, 1000):
#     c = 0
#     for x in range(1, 1000):
#         if (x % a == 0) or ((x in b) <= (x % 22 != 0)):
#             c += 1
#     if c == 999:
#         print(a)

# f = [1] * 2026
#
# for n in range(2026):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = 2 * n * f[n-1]
# print(((f[2024]//16-f[2023])//f[2022]))

# f = open('17_17558.txt')
# g = [int(i) for i in f]
# mx = 0
# c = 0
# kr32 = sum([int(i) for i in g if i % 32 ==0])
# for i in range(len(g) - 1):
#     if g[i] < 0 or g[i+1] < 0 and (g[i] + g[i+1]) < kr32:
#         c += 1
#         mx = max(mx, g[i] + g[i+1])
# print(c, mx)
#
# def f(x, y):
#     if x > y:
#         return 0
#     elif x == y:
#         return 1
#     else:
#         return f(x+1, y) + f(x+2, y) + f(x+3, y)
#
# print(f(5,7) * f(7,11))