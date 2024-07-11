# 4Cx415 + x62A13
alph = '0123456789abcde'
for x in alph:
    f = int(f'4C{x}4', 15) + int(f'{x}62A', 13)
    if f%121==0:
        print(f//121)
        break