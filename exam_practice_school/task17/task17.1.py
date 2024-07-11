f = open("")
g = [int(i) for i in f]
f.close()
count = 0
max_13 = -1000000
min_sum = 100000
for i in g:
    if  i > max_13  and str(i)[-2:] == "13":
        max_13 = i
for i in range(len(g) - 2):
    d = [g[i], g[i+1], g[i+2]]
    c = 0
    for x in d:
        if 99 < abs(x) < 1000:
            c+=1

    if c == 2 and sum(d) < max_13:
        count += 1
        min_sum = min(min_sum, sum(d))
print((count, min_sum))

# f = open("17.22.txt")
# g = [int(i) for i in f]
# min_double = min([x for x in g if str(x)[-2] == str(x)[-1]])
#
# cnt = 0
# max_pair = 0
# for i in range(len(g)-1):
#     if (g[i] % 7 == 0 and g[i+1] % 7 != 0) or (g[i] % 7 != 0 and g[i+1] % 7 == 0):
#         if (str(g[i])[-1] == str(g[i+1])[-2]) or (str(g[i])[-2] == str(g[i+1])[-1]):
#             if g[i]**2 + g[i+1] **2 <= min_double**2:
#                 cnt+=1
#                 max_pair = max(max_pair, g[i]**2 + g[i+1]**2)
#
# print(cnt, max_pair)