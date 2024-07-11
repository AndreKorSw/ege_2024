# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((x or not(y)) <= (z == (x and  y)) or not(w)):
#                     print(x, y, z, w)
#
#
# for n in range(10, 1000):
#     s = "1" + n * "4"
#     while "14" in s or "444" in s or "22444" in s:
#         if "14" in s:
#             s = s.replace("14", "22", 1)
#         if "444" in s:
#             s = s.replace("444", "1", 1)
#         if "22444" in s:
#             s = s.replace("22444", "411", 1)
#
#     if s.count("1") != 0 and s.count("2") <= 50:
#         print(n)
# print(bin(185))
# print(bin(179))
#
for n in range(171, 10090):
    s = bin(n)[2:]
    s += str(s.count("1") % 2) + str(s.count("1") % 2)
    if int(s,2) % 2 == 0:
        print(int(s, 2))
# from itertools import product
#
# s = "0123456789"
#
# words = product(s, repeat = 8)
