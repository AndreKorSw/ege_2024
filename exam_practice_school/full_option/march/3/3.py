# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x and (not y)) or (y == z) or (not w)):
#                     print(x, y, z, w)
# def f(s):
#     return sum(list(map(int, str(s))))
# for n in range(1, 100):
#     s = bin(n)[2:]
#     summa = f(s)
#     s = s + str(summa % 2)
#     summa = f(s)
#     s = s + str(summa % 2)
#     if int(s, 2) > 93:
#         print(int(s, 2))
#         break
# from itertools import product
# alph = "УЧЕНИК"
# words = product(alph, repeat = 5)
# cnt = 0
# for w in words:
#     word = "".join(w)
#     if word[0] == "У" and word[-1] =="К":
#         cnt += 1
# print(cnt)

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# for i in range(1000):
#     s = ">" + 39 * "0" + i * "1" + 39 * "2"
#     while ">1" in s or ">0" in s or  ">2" in s:
#         if ">2" in s:
#             s = s.replace(">2", "2>", 1)
#         if ">1" in s:
#             s = s.replace(">1", ">22", 1)
#         if ">0" in s:
#             s = s.replace(">0", "1>", 1)
#
#     d = [i for i in s if s.isdigit()]
#     if is_prime(sum(d)):
#         print(i)
#         break
