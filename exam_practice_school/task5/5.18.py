for i in range(1, 10000):
    s = bin(i)[2:][:-1]
    if i % 2 != 0:
        s += '10'
    else:
        s += "01"
    if int(s, 2) == 2017:
        print(i)
        break