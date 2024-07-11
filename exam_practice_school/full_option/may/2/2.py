# print("X Y Z W")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and y) and (x and(z <= w))):
#                     print(x, y, z, w)
from functools import lru_cache

# print(oct(int("00011011011010010", 2)))
# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля). По этому числу строится новое число по следующим правилам.
#
# Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# Наименьшая из полученных трёх сумм удаляется.
# Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
# Укажите наибольшее число, при обработке которого автомат выдает число 57.


# for i in range(1000, 10000):
#     s = str(i)
#     s1 = int(s[0]) + int(s[1])
#     s2 = int(s[2]) + int(s[1])
#     s3 = int(s[2]) + int(s[3])
#     d = sorted([s1, s2, s3])[1:]
#     res = str(d[0]) + str(d[1])
#     if int(res) == 57:
#         print(i)

# from turtle import *
# tracer(0)
# Назад 10
#
# Повтори 3 [Вперед 14 Направо 90 Вперед 18 Направо 90]
#
# Поднять хвост
#
# Вперед 2 Направо 90 Назад -4 Налево 90
#
# Опустить хвост
#
# Повтори 9 [Назад -2 Налево 60 Вперед 10 Направо 120]
# m = 20
# pd()
#
# backward(10*m)
# for i in range(3):
#     forward(14*m)
#     right(90)
#     forward(18*m)
#     right(90)
# pu()
# forward(2*m)
# right(90)
# backward(-4*m)
# left(90)
# pd()
# for i in range(9):
#     backward(-2*m)
#     left(60)
#     forward(10*m)
#     right(120)
#
# pu()
# #прорисовка осей координат
# for x in range(-50, 50):
#     goto(x*m, 0)
#     pd()
#     pencolor("red")
# pu()
# for y in range(-50, 50):
#     goto(0, y*m)
#     pd()
#     pencolor("red")
# # done()
# # for x in range(-25, 25):
# #     for y in range(-20, 30):
# #         goto(x*m, y*m)
# #         dot(3)
# # done()
# #
# f = open("6__3yr40.csv")
#
# g =[list(map(int, i.split(","))) for i in f]
# c = 0
# for i in g:
#     nechet = []
#     bols50 = []
#     mens50 = []
#     for j in i:
#         if j % 2 != 0:
#             nechet.append(j)
#         if j < 50:
#             mens50.append(j)
#         if j > 50:
#             bols50.append(j)
#     if (sum(nechet) % 7 == 0) and (len(mens50) > len(bols50)):
#         c+=1
# print(c)
# ПОКА нашлось (92) ИЛИ нашлось (252) ИЛИ нашлось (222) ИЛИ нашлось (7777)
#
#    ЕСЛИ нашлось (92)
#
#       ТО заменить (92, 25)
#
#    КОНЕЦ ЕСЛИ
#
#    ЕСЛИ нашлось (252)
#
#       ТО заменить (252, 7)
#
#    КОНЕЦ ЕСЛИ
#
#    ЕСЛИ нашлось (222)
#
#       ТО заменить (222, 79)
#
#    КОНЕЦ ЕСЛИ
#
#    ЕСЛИ нашлось (7777)
#
#       ТО заменить (7777, 29)
# for n in range(200, 850):
#     s = "9" + "2" * n
#     while "92" in s or "252" in s or "222" in s or "7777" in s:
#         if "92" in s:
#             s = s.replace("92", "25", 1)
#         if "252" in s:
#             s = s.replace("252", "7", 1)
#         if "222" in s:
#             s = s.replace("222", "79", 1)
#         if "7777" in s:
#             s = s.replace("7777", "29", 1)
#     if s[-2:] == "79":
#
#         print(s)
#         print(n)

# for a in range(300):
#     c = 0
#     for x in range(1000):
#         if ((x % 3 != 0) <= (x % 7 != 0)) or (x + a > 120):
#             c+=1
#     if c == 1000:
#         print(a)
#         break
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n < 15:
#         return n
#     if n >= 15:
#         return 2*f(n-3) + 4 + f(n-1)
#
# @lru_cache(None)
# def g(i):
#     if  i >= 99:
#         return 1+2*i
#     if i < 99:
#         return i * g(i+2) + g(i*2)
# print(f(52) - g(88))

for x in "0123456789abcd":
    s = (int(f'9{x}9{x}', 14) + int(f'a{x}90', 14))
    if s % 8 == 0:
        print(s // 8)

# f = open("17__1srlh.txt")
# g = [int(i) for i in f]
# max3 = max([i for i in g if str(i)[-1] == "3"])
# c = 0
# mx = -1000000
# for i in range(len(g)-1):
#     if ((g[i] ** 2 + g[i+1] ** 2) >= max3) and (str(g[i])[-1] == "3" or  str(g[i+1])[-1] == "3"):
#         c+=1
#         mx = max(mx, (g[i] ** 2 + g[i+1] ** 2))
# print(c, mx)

# def f(x, y):
#     if x > y or x == 16:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x+2, y) + f(x+3, y) + f(x**2, y)
# print(f(2, 33))
#
# s = open("24_M1__42nc9 (1).txt").readline()
# d = {x: 0 for x in sorted(set(s))}#словарь, в котором в качестве ключа у нас буква,
# # а в качестве значения - количество раз сколько она встречается по определенному условию
# for i in range(len(s)-2):
#     if s[i] == s[i+1]:#если два рядом стоящих символа равны между собой
#         d[s[i+2]] += 1#то к значению той буквы, что стоит за этой парой, добавляем единицу
# #выводим букву и количество раз, сколько она встречается в файле
# print([(x,s.count(x)) for x in d.keys() if d[x] == max(d.values())])

# Число называется избыточным, если оно строго меньше суммы своих собственных делителей (то есть всех положительных делителей,
# отличных от самого числа). Определите количество избыточных чисел из диапазона [5; 50000].
# c = 0
# for i in range(5, 50001):
#     dividers = []
#     for j in range(1, i+1):
#         if i % j == 0:
#             dividers.append(i//j)
#     if i < (sum(set(dividers))):
#         c+=1
#
# print(c)


# На вход программы подаётся натуральное число N, а затем N целых чисел. Необходимо определить максимальную сумму непрерывной подпоследовательности элементов.
#
# Входные данные: Даны два входных файла: файл A и файл B, каждый из которых содержит в первой строке количество чисел N           7
# (1 ≤ N ≤ 10)  . Каждая из следующих N строк содержит целое число, по модулю не превышающее 104  .
#
# В ответе укажите два числа через пробел: сначала значение искомой суммы для файла А, затем для файла B.
# f = open("27A_09_3__3knhj (1).txt")
