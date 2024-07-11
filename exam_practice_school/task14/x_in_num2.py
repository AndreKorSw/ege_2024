alph ="0123456789abcdefgh"
for x in alph:
    f = int(f'28{x}2', 18) + int(f'93{x}5', 12)
    if f%133==0:
        print(f//133)
        break