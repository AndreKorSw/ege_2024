for i in range(100, 1000):
    x = str(i)
    s1 = int(x[0])*int(x[1])
    s2 = int(x[1])*int(x[2])
    res = str(max(s1, s2)) + str(min(s1,s2))
    if res == "205":
        print(i)
        break