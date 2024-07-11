# Предприятие производит оптовую закупку некоторых изделий A и B, на которую выделена определённая сумма денег. У поставщика есть в наличии партии этих изделий различных модификаций по различной цене. На выделенные деньги необходимо приобрести как можно больше изделий A независимо от модификации. Если у поставщика закончатся изделия A, то на оставшиеся деньги необходимо приобрести как можно больше изделий B. Известны выделенная для закупки сумма, а также количество и цена различных модификаций данных изделий у поставщика. Необходимо определить, сколько будет закуплено изделий B и какая сумма останется неиспользованной.
#
# Входные данные.
#
# Задание 26
#
# Первая строка входного файла содержит два целых числа: N  — общее количество партий изделий у поставщика и M  — сумма выделенных на закупку денег (в рублях). Каждая из следующих N строк описывает одну партию и содержит два целых числа (цена одного изделия в рублях и количество изделий в партии) и один символ (латинская буква A или B), определяющий тип изделия. Все данные в строках входного файла отделены одним пробелом.
#
# В ответе запишите два целых числа: сначала количество закупленных изделий типа B, затем оставшуюся неиспользованной сумму денег.

f = open("26 (1).txt")
colvo, money = map(int, f.readline().split())
load = []
quantity_B = 0
extra_money = 0
for i in f:
    one_price, quantity, type_izd = int(i.split()[0]), int(i.split()[1]), i.split()[2]
    load.append([type_izd, int(one_price), int(quantity), ])
load.sort(reverse=False, key = lambda x: (x[0], x[1], x[2]))
print(load)

for i in range(len(load)):
    if money - load[i][1] < 0:
        break
    for j in range(load[i][2]):
        if money - load[i][1] >= 0:
            money = money - load[i][1]
            if load[i][0] == 'B':
                quantity_B +=1
print(quantity_B, money)