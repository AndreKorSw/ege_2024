# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
# Например маске 123*4?5 соответствуют числа 123405 и 12300405.
# — оответствуют маске *31*65?;
# — делятся на 31 и 2031 без остатка;
# — количество делителей числа является результатом любой степени двойки.
#25
from fnmatch import  *
# найдем все степени двойки в отдельном цикле
stepeni_dvoiki = []
for i in range(1, 20):
    stepeni_dvoiki.append(2 ** i)
for i in range(0, 10**9, 31*2031):# если нужно чтобы делилось на два числа одновременно то перемножим их
    if fnmatch(str(i), '*31*65?'):
        cnt_del = 0
        for j in range(1, int(i**0.5)+ 1):
            if i % j == 0:
                cnt_del += 2
        if cnt_del in stepeni_dvoiki:
            print(i, i // 2031)
