f = open("")

s, n = map(int, f.readline().split())
m = 0
k = 0
for i in range(n):
    kpd = int(f.readline())
    if kpd > 79:
        k += 1
        m = max(kpd, m)
print(k, m)