f = open('17 (4).txt')
g = [int(i) for i in f]
f.close()
count = 0
max_sum = 0
for i in range(len(g) - 1):
    for j in range(i+1, len(g)):
        if (g[i] + g[j]) % 10 == 0:
            count += 1
            max_sum =max(max_sum, (g[i] + g[j]))
print(count, max_sum)