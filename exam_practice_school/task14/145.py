# В системе счисления с основанием p выполняется равенство 32 · 14  =  xy2. Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p. Определите значение числа yxp и запишите это значение в десятичной системе счисления.
for p in range(100): #58522
    for x in range(p):
        for y in range(p):
            s = (3 * p + 2) * (p + 4)
            r = x * p ** 2 + y * p + 2
            if s == r:
                print(y * p + x)