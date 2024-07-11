# print("x y z w u")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 for u in range(2):
#                     if not(((z <= w) and (y == (not(x)))) <= (u == (y or z))):
#                         print(x, y, z, w, u)

# for n in range(1, 1000):
#     x = bin(n)[2:]
#     s1 = x + x[-1]
#     s1 += str(s1.count("1") % 2)
#     if int(s1, 2) > 105:
#         print(int(s1, 2))
#         break
# Заметим, что чётных и нечётных цифр в восьмеричной системе счисления 4 и 4 соответственно. Найдём количество пятизначных чисел, начинающихся с нечётной цифры: 4
# 288. Найдём количество пятизначных чисел, начинающихся с чётной цифры (при этом учтем, что число не может начинаться с нуля): 3 216. Таким образом, получаем ответ: 504.
#
#  
# import itertools
# alphabet = "01234567"
# chet = "0246"
# nechet = "1357"
# ar = itertools.permutations(alphabet, 5) #Размещение
# for w in ar:
#     if
# f = open("24_58327.txt")
# g = f.readline().split()[0]
# c = 1
# mx = 1
# for i in range(1, len(g)):
#     if g[i-1] >= g[i]:
#         c += 1
#     else:
#         mx = max(mx, c)
#         c = 1
# print(mx)
# from fnmatch import *
# for i in range(0, 10**8, 2023):
#     if fnmatch(str(i), "3?1*57"):
#         print(i, i//2023)
# f = open("27881.txt")
# disk_capacity, num_users = map(int, f.readline().split())
# files = sorted(map(int, f))
# max_num_users = 0
# max_file = 0
# cur_capacity = 0
# for file in files:
#     if cur_capacity + file <= disk_capacity:
#         cur_capacity += file
#         max_file = max(max_file, file)
#         max_num_users += 1
#     else:
#         print(max_num_users, disk_capacity - cur_capacity + max_file)
#         break

# from random import shuffle
# s = list('7'*40 + '9' * 40 + '4' * 50)
# # shuffle(s)
# s = ''.join(s)
# while '49' in s or '97' in s or '47' in s:
#     if '47' in s:
#         s = s.replace('47', '74', 1)
#     elif '97' in s:
#         s = s.replace('97', '79', 1)
#     elif '49' in s:
#         s = s.replace('49', '94', 1)
# print(s[24] + s[70] + s[104])