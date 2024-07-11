# значение м оканчивается на 8
n = 700001
cnt = 0
while cnt != 5:
    for i in range(2, n):
        if n % i == 0:
            if str((i + n // i))[-1] == "8":
                print(n, i + n // i)
                cnt +=1
            break
    n += 1
