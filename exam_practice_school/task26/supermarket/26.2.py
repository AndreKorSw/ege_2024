#каждый третий товар бесплатно
# минимальную цену которую заплатил бы покупатель изначально,
# если бы бесплатным был бы 3й товар в любой покупке из 3х предметов,
# а затем цену которую он заплатил

f = open('')
n = int(f.readline())
pokupki = [int(i) for i in f]
pokupki.sort(reverse = True)
print(sum(pokupki) - sum(pokupki[:n//3]))# сумма всех покупок - размер скидки на самую дорогую четверть
sum_pokupok = sum(pokupki)


for i in range(2, len(pokupki), 3):
    sum_pokupok -= pokupki[i]
print(sum_pokupok)
