b = list(range(50, 70))
for a in range(1, 100):
    c = 0
    for x in range(1, 100):
        if ((x % a == 0) or ((x in b) <= (x % 21 != 0))):
            c += 1
    if c == 99:
        print(a)
