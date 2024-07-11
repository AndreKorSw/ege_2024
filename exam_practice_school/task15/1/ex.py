#побитовая конъюнкция
for a in range(0, 1000):
    count = 0
    for x in range(0, 1000):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x& a != 0))):
            count += 1
    if count == 1000:
        print(a)
        break

