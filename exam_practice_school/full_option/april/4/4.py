# s = 9**18 + 3 ** 54 - 9
# x = ''
# while s != 0:
#     x += str(s%3)
#     s //= 3
# print(x.count(("2")))

# alph =  "0123456789abcd"
# for x in alph:
#     s = int(f"1{x}563", 14) + int(f"871{x}3", 14)
#     if s % 24 == 0:
#         print(s//24)


# for a in range(1, 1000):
#     c = 0
#     for x in range(300):
#         for y in range(300):
#             if ((x +2*y < a) or (y > x) or (x > 60)):
#                 c+=1
#     if c == 90000:
#         print(a)
#         break
# p1,p2,q1,q2 = 30, 45, 40, 55
# P = [i / 10 for i in range(p1 * 10, p2*10+1)]
# Q = [i / 10 for i in range(q1 * 10, q2*10+1)]
# A = set()
# def f(x, a):
#     return (((x not in A) <= (x not in P)) and ((x in Q) <= (x in A)))
# for x in range(30, 900):
#     if not f(x, A):
#         A.add(x)
# print(A)

# p1, p2, q1, q2 = 5, 30, 14, 23
# P = [i / 10 for i in range(p1 *10, p2* 10)]
# Q= [i / 10 for i in range(q1 *10, q2* 10)]
# a = set([i / 10 for i in range(50, 301)])
# def f(x, a):
#     return ((x in P) == (x in Q)) <= (not(x in a))
# for x in [i / 10 for i in range(50, 301)]:
#     if f(x,a):
#         a.remove(x)
# print(sorted(a))

# P = [i for i in range(5,31)]
# Q = [i for i in range(14,24)]
# A = [i for i in range(5,31)]
# for x in range(5,31):
#     if (((x in P) == (x in Q)) <= (not(x in A))) == True:
#         A.remove(x)
# print(sorted(A))

# from fnmatch import *
# for x in range(0, 10**8, 1991):
#     if fnmatch(str(x), "3?1*57"):
#         print(x, x// 1991)
def f(x, y, flag):
    if x > y:
        return 0
    if x == y:
        return 1
    elif flag:
        return f(x+1, y, True)+f(x*2, y, True)
    else:
        return f(x+1, y, False)+f(x*2, y, False)
print(f())