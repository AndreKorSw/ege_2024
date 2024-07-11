# for n in range(1, 100):
#     s = bin(n)[2:]
#     if n % 3 == 0:
#         s += s[-3:]
#     else:
#         s += bin(3*(n%3))[2:]
#     if int(s, 2) < 100:
#         print(n)
# from itertools import permutations
# alph = "полина"
# con = "плн"
# v = "оиа"
# c = 0
# words = permutations(alph)
# for w in words:
#     word = "".join(w)
#     flag= 0
#     for i in range(len(word)-1):
#         if (word[i] in v and word[i+1] in v) or (word[i] in con and word[i+1] in con):
#             flag = 1
#     if flag == 1:
#         continue
#     else:
#         c+=1
# print(c)
#
# f = open("9_58322.csv")
# g = [list(map(int, i.split(","))) for i in f]
#
# c= 0
# for i in g:
#     d = sorted(i)
#     if d[-1] ** 2 > d[0]*d[1]*d[2] or (d[3]-d[2] == d[2]-d[1] and d[2]-d[1] == d[1]-d[0]):
#         c+=1
# print(c)

# for a in range(300, 1, -1):
#     c = 0
#     for x in range(300):
#         if ((120%a == 0) and ((x % a != 0) <= ((x % 18 == 0) <= (x% 24 !=0)))):
#             c+= 1
#     if c == 300:
#         print(a)

# def f(x, y, flag):
#     if x> y:
#         return 0
#     if x == y:
#         return 1
#     elif flag:
#         return f(x+1, y, True) + f(x+2, y, True) + f(x*2, y, False)
#     else:
#         return f(x+1, y, True) + f(x+2, y, True)
#
# print((f(1, 11, True)))
