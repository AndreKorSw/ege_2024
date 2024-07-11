#Для какого наименьшего неотрицательного целого числа А
for a in range(1000):
    count = 0
    for x in range(1000):
        # x & 25 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)
        if (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0)):
            count += 1
    if count == 1000:
        print(a)
        break