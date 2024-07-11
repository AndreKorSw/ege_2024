for n in range(0, 1000000):
    r = bin(n)[2:]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    if int(r, 2) > 97:
        print(n)
        break