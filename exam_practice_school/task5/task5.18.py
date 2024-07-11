for i in range(1, 1000):
    s = str(bin(i)[2:])
    if i % 2 == 0:
        s = '10' + s
    else:
        s = "1"+ s +'01'
    if int(s, 2) > 616:
        print(i)
        break
