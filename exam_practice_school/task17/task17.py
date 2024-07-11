

#17
f = open('17.txt')
g = [int(i) for i in f]
f.close()
count = 0
min_3 = 1000000
max_sum = -1000000
for i in g:
    if str(i)[-1] == "3":
        if 99 < abs(i) < 1000:
            min_3 = min(min_3, i)
for i in range(len(g)-1):
    d = [g[i]**2, g[i+1]**2]
    if ((999 < abs(g[i]) < 10000) and not (999 < abs(g[i + 1]) < 10000)) or (not (999 < abs(g[i]) < 10000) and (999 < abs(g[i + 1]) < 10000)):
        if sum(d) % min_3 == 0:
            count += 1
            max_sum = max(max_sum, sum(d))
print(count, max_sum)