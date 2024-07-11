# две четные и две нечетные не стоят рядом
from itertools import product
alph = "01234567"
chet = "0246"
nechet = '1357'
words = product(alph,  repeat = 7)
c = 0
for w in words:
    if (len(set(w)) == 7) and  (w[0] != "0")  and ((w[0] in chet and w[1] in nechet and w[2] in chet and w[3] in nechet and w[4] in chet and w[5] in nechet and w[6] in chet)
                           or (w[0] in nechet and w[1] in chet and w[2] in nechet and w[3] in chet and w[4] in nechet and w[5] in chet and w[6] in nechet)):
        c+=1
print(c)