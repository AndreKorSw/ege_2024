with open('24_demo (2).txt') as f:
    f = f.readline()
c = 1
mx = 0
for i in range(len(f)-1):
    if f[i] == f[i+1] == "X":
        c += 1
    else:
        mx = max(mx, c)
        c = 1
print(mx)