f = open('27A_17619.txt')
n = 198
mx = 0
s = [int(i) for i in f]
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for m in range(k + 1, n):
                mx = max((s[j] - s[i]) + (s[m] - s[k]), mx)
print(mx)
