for i in range(10000, 100000):
    s = str(i)
    k1 = int(s[0]) + int(s[2]) + int(s[4])
    k2 = int(s[1]) + int(s[3])
    first = str(min(k1, k2))
    second = str(max(k1, k2))
    res = first + second
    if res == '621':
        print(i)
        break
