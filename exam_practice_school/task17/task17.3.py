f = open('17 (3).txt')
g = [int(i) for i in f]
f.close()
count = 0
max_dvy_9 = 0
for i in range(len(g) - 1):
    for j in range(i + 1, len(g)):
        if (g[i] + g[j]) % 9 == 0:
            count += 1
            max_dvy_9 = max(max_dvy_9, (g[i] + g[j]))
print(count, max_dvy_9)