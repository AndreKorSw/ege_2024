# В отчетности театра о проданных местах на концерт возможно просмотреть информацию о ряде места и его номере.
# Наша задача определить ряд с наименьшим номером, в котором существуют два свободных соседних места, при условии, что справа и слева от них места уже проданы
# . Ответ запишите без разделителей: сначала номер ряда, затем наименьшее из мест такой пары.
#
# Входные данные:
#
# Первая строка - количество проданных мест. Следующие строки: ряд и номер места.

f = open("26 (7).txt")
n = int(f.readline())
mesta = []
for i in f:
    row, place = map(int, i.split())
    mesta.append([row, place])

mesta.sort()
for i in range(len(mesta)):
    if mesta[i][0] == mesta[i+1][0] and mesta[i+1][1] - mesta[i][1] == 3:#если номер ряда одинаковый разница в местах составляет 3
        print(mesta[i][0], mesta[i][1] + 1)
