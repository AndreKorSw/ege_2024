#наибольшее колво коробок для упаковки однго подарка и максимальную длинну самой маленокой коробки
f = open('')
n = int(f.readline())
korobki = [int(s) for s in f]
podarok = [korobki.sort(reverse=True)[0]]#кладем самую большую коробку
for i in range(1, len(korobki)):
    if podarok[-1] - korobki[i] >= 3:
        podarok.append(korobki[i])

print(len(podarok), min(podarok))