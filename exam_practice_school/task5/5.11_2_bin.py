for n in range(1, 1000):
    r=bin(n)[2:]

    if r.count("1")%2==0:
        r+="0"
    else:
        r+="1"

    if r.count("1") % 2 == 0:
        r += "0"
    else:
        r += "1"

    if int(r, 2)>97:
        print(int(r, 2))
        break