#17
f = open('17 (2).txt')
g = [int(i) for i in f]
f.close()
max_15 = 0
max_sum = 0
count = 0
for i in range(len(g)):
    if g[i] % 100 == 15:
        max_15 = max(max_15, g[i])
for i in range(len(g) - 2):
    d = [g[i], g[i + 1], g[i + 2]]
    c = 0
    for x in d:
        if 999 < x < 10000:
            c += 1
    if c == 1 and sum(d) >= max_15:
        count += 1
        max_sum = max(max_sum, sum(d))
print(count, max_sum)
