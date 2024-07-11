f = open('17 (6).txt')
g = [int(i) for i in f]
f.close()
count = 0
max_19 = 0
max_sum = -90000
for i in range(len(g)):
    if abs(g[i]) % 100 == 19:
        max_19 = max(max_19, g[i])
for i in range(len(g) - 2):
    d = [g[i], g[i + 1], g[i + 2]]
    h = [x for x in d if len(str(abs(x))) == 4]
    if len(h) == 2 and sum(d) > max_19 and any(x % 3 == 0 for x in d):
        count += 1
        max_sum = max(max_sum, sum(d))
print(count, max_sum)

