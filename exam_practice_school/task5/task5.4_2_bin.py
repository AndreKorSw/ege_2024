for n in range(96, 10000):
    r=bin(n)[2:]
    if r.count("1")==r.count("0"):
        r+=r[-1]
    elif r.count("1") > r.count("0"):
        r+="0"
    else:
        r+="1"

    if r.count("1")==r.count("0"):
        r+=r[-1]
    elif r.count("1") > r.count("0"):
        r+="0"
    else:
        r+="1"

    if r.count("1")==r.count("0"):
        r+=r[-1]
    elif r.count("1") > r.count("0"):
        r+="0"
    else:
        r+="1"

    if int(r, 2)%4==0:
        print(n)
        break
