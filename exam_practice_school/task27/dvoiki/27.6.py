f = open()
n = int(f.readline())
kr14, kr7, kr2, nerk = 0,0,0,0
for s in f:
    x = int(s)
    if x % 14 == 0:
        kr14 += 1
    elif x % 7 == 0:
        kr7  +=  1
    elif x % 2 == 0:
        kr2 += 1
    else:
        nerk +=1

print(n * (n-1)//2 - (kr7*kr2 + kr14*(n - kr14) + (kr14*(kr14 - 1) // 2)))
