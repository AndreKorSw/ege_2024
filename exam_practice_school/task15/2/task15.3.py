#15 сколько существует целых значений числа а
res = 0
for a in range(200):
    count = 0
    for x in range(300):
        for y in range(300):
            if ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6)):
                count += 1
    if count == 300*300:
        res +=1
print(res)