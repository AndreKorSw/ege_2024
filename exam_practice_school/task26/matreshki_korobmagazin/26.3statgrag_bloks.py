f = open("26.5.txt")
n = int(f.readline())
dlina_st = 7
korobki = sorted([int(i) for i in f], reverse = True)
bloks = []
while len(korobki) != 0:
    kuda_kladem  = [korobki[0]] #итоговый подарок и кладем сюда самую большую коробку
    for i in range(1, len(korobki)):
       if min(kuda_kladem) - korobki[i] >= dlina_st:
           kuda_kladem.append(korobki[i])
    bloks.append(kuda_kladem)
    korobki.sort(reverse=True)
print(len(bloks), len(bloks[0]))