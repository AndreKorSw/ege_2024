# c = 0
# for a in range(1, 100):
#     k = 0
#     for x in range(1,1000):
#         if ((not(x % a == 0)) <= ((x % 6 == 0) <= (not(x % 9 == 0)))):
#             k+=1
#     if k == 999:
#         print(a)
#

# for a in range(1, 300):
#     k = 0
#     for x in range(1,1000):
#         if ((x & 29 != 0) <= ((x & 12 == 0) <= (x & a !=0))):
#             k+=1
# print(cnt, max_pair)


# from ipaddress import ip_network
# net = ip_network("106.184.0.0/255.248.0.0")
# c = 0
# for ip in net:
#     b = bin(int(ip))[2:]
#     if b.count("1") % 2 != 0:
#         c+=1
# print(c)
#     if k == 999:
#         print(a)

# def f(x, y):
#     if x > y or x == 11 or  x == 12:
#         return 0
#     if x == y:
#         return 1
#
#     else:
#         return (f(x+1, y) + f(x+2, y) + f(x*3, y))
#
# print(f(1, 9) * f(9, 30))

# f = open()
# g = [int(i) for i in f]
# max_sum =0
# min_double = 0
# for i in range(len(g)):
#     if str(g[i])[-2] == str(g[i])[-1]:
#         min_double = min(min_double, i)
#
# cnt = 0
# max_pair = 0
# for i in range(len(g)-1):
#     if (g[i] % 7 == 0 and g[i+1] % 7 != 0) or (g[i] % 7 != 0 and g[i+1] % 7 == 0):
#         if g[i]**2 + g[i+1] **2 <= min_double**2:
#             cnt+=1
#             max_pair = max(max_pair, g[i]**2 + g[i+1]**2)
#

# from ipaddress import ip_network
# ip_net = ip_network("106.184.0.0/255.248.0.0.", 0)
# c=0
# for ip in ip_net:
#     if bin(int(ip))[2:].count("1") % 2 != 0:
#         c+=1
# print(c)

