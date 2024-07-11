f = open("26.2txt")
n, k = int(f.readline()), int(f.readline())
a = sorted([list(map(int, i.split())) for i in f])
for x in range(k):
    t = [a[0]]# сэмулируем заполнение первой ячейка, t это первая ячейка
    a.pop(0)

    for j in range(100):
        mn = [10000000000000000000, 0]
        dl = -1
        for i in range(len(a)):
            if (a[i][0] > t[-1][1]) and (a[i][0] < mn[0]):
                mn = a[i]
                dl = i
        if dl > 1:
            t.append(mn)
            a.pop(dl)
print(n - len(a))