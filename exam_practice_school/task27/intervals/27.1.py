f = open()
n = int(f.readline())
a = [int(i) for i in f]
kr13, nekr, cnt = 0,0,0
for i in range(5, n):
    if a[i - 5] % 13 == 0:
        kr13 += 1
    else:
        nekr += 1
    #подсчитываем пары
    if a[i] % 13 == 0:
        cnt += kr13 + nekr
    else:
        cnt += kr13
print(cnt)
