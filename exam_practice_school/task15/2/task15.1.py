#15 для какого наибольшего а
for a in range(200, 0, -1):
    count = 0
    for x in range(300):
        for y in range(300):
            if (((y + 2*x) != 48) or (a < x) or (x < y)):
                count += 1
    if count == 300 * 300:
        print(a)
        