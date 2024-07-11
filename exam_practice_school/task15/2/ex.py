#координатная плоскость
#для какого наибольшего а
for a in range(200, 0, -1):
    count = 0
    for x in range(300):
        for y in range(300):
            if ((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <= 9)):
                count += 1
    if count == 300*300:
        print(a)
        break