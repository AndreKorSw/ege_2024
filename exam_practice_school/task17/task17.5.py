f = open('17 (5).txt')
g = [int(i) for i in f]
f.close()
# medium_val = sum(g)/len(g)
s = 0
n = 0
for i in range(len(g)):
    if (g[i] % 2 == 1):
        s += g[i]
        n += 1
medium_val = s / n
count = 0
max_sum = 0
for i in range(len(g) - 1):
    if ((g[i] % 5  == 0) or (g[i+1] % 5  == 0)) and ((g[i] < medium_val)  or (g[i+1] < medium_val)):
        count += 1
        max_sum = max(max_sum, g[i] + g[i + 1])
print(count, max_sum)
