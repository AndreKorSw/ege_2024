#для какого наименьшего а
for a in range(200):
    count = 0
    for x in range(300):
        for y in range(300):
            if (2 * x + 3 * y > 30) or (x + y <= a):
                count +=1

    if count == 300*300:
        print(a)
        break