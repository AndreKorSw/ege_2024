f = open("")
n = int(f.readline())
T = int(f.readline())
s = 0
a= []
for i in range(n):
    opasnost, vremia = map(int, f.readline().split())
    a.append((opasnost, vremia))
    s+= opasnost

sr = s/n
super_virus = []
virus = []

for i in range(n):
    if a[i][0] < sr:
        super_virus.append(a[i][1])
    else:
        virus.append(a[i][1])
super_virus.sort()
virus.sort()
total_time = 0
while total_time <= T:
    if  total_time + super_virus[i] + virus[i] > T:
        print('last virus to delete', i)#используем его в ответе
    total_time += super_virus[i] + virus[i]
    i += 1
print(2249+2250)
print(sum(super_virus[2249]))