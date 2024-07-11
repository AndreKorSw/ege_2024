alph = "0123456789*****"
c = 0
for x1 in alph:
    for x2 in alph:
        for x3 in alph:
            for x4 in alph:
                for x5 in alph:
                    res = x1 + x2 + x3 + x4 + x5
                    if res.count("8") == 1 and res[0] != "0" and res.count("*") <= 2:
                        c += 1
print(c)