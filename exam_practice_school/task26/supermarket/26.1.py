f = open("")
n = int(f.readline())
pokupki = [int(s) for s in f]
pokupki.sort(reverse = True)
print(sum(pokupki) - sum(pokupki[0:n//4])*0.5)# сумма всех покупок - размер скидки на самую дорогую четверть

pokupki.sort()
print(sum(pokupki) - sum(pokupki[0:n//4])*0.5)# размер скидки на самую дешевую четверть