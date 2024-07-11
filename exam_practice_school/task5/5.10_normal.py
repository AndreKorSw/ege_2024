for n in range(1000, 10000):
    s=str(n)
    k1 = int(s[0]) * int(s[1])
    k2 = int(s[2]) * int(s[3])
    first = str(max(k1, k2))
    second = str((min(k1, k2)))
    s1 = first + second
    if s1=="124":
        print(n)
        break