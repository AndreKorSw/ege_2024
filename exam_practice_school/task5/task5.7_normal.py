for n in range(1, 1000000):
    s = str(n)
    s1 = sum([int(i) for i in s if int(i) % 2 == 0])
    s2 = sum([int(s[i]) for i in range(0, len(s), 2)])
    if abs(s2 - s1) == 27:
        print(n)
        break
